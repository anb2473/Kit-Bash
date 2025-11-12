import utils
from config import MIN_WIDTH, MIN_HEIGHT
import threading
import time
import queue
import sys

# msvcrt is Windows-only; used for non-blocking console input
try:
    import msvcrt
except Exception:
    msvcrt = None

win_valid_event = threading.Event()
result_queue = queue.Queue(maxsize=1)

class WinValidator:
    def __init__(self):
        utils.clear_terminal()
    
    def validate(self):
        self.width, self.height = utils.get_win_size()
        if not self.validate_win_size():
            self.interupt()

    def validate_win_size(self):
        self.width, self.height = utils.get_win_size()
        return self.width >= MIN_WIDTH and self.height >= MIN_HEIGHT

    def check_user_override(self):
        """Prompt user for Y/N in a way that can be interrupted by win_valid_event.
        On Windows we use msvcrt to poll keypresses. If msvcrt isn't available
        we fall back to blocking input (best-effort).
        """
        utils.clear_terminal()
        prompt = "Your screen might be too small to use KitBash, do you wish to override? [Y/N] "
        sys.stdout.write(prompt)
        sys.stdout.flush()

        if msvcrt is None:
            try:
                ans = input().strip().lower()
                return ans.startswith("y")
            except (EOFError, KeyboardInterrupt):
                return False

        buf = []
        while not win_valid_event.is_set():
            if msvcrt.kbhit():
                ch = msvcrt.getwch()
                if ch in ("\r", "\n"):
                    sys.stdout.write("\n")
                    ans = "".join(buf).strip().lower()
                    return ans.startswith("y")
                if ch == "\x08":  # backspace
                    if buf:
                        buf.pop()
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()
                else:
                    buf.append(ch)
                    sys.stdout.write(ch)
                    sys.stdout.flush()
            else:
                time.sleep(0.05)
        return False
    
    def event_listener(self, target, name="listener"):
        # Poll the target until it returns True or another listener wins.
        try:
            while not win_valid_event.is_set():
                found = False
                try:
                    found = target()
                except Exception:
                    # If the target raises, surface it as a payload so main
                    # can handle/log it and stop other listeners.
                    try:
                        result_queue.put_nowait((name, sys.exc_info()[1]))
                    except queue.Full:
                        pass
                    win_valid_event.set()
                    break

                if found:
                    try:
                        result_queue.put_nowait((name, found))
                    except queue.Full:
                        pass
                    win_valid_event.set()
                    break

                time.sleep(0.05)
        except Exception as exc:
            try:
                result_queue.put_nowait((name, exc))
            except queue.Full:
                pass
            win_valid_event.set()

    def interupt(self):
        # Start both listeners. Each will attempt to publish the winner to
        # result_queue (first-writer wins) and set win_valid_event.
        win_size_listener = threading.Thread(target=self.event_listener, args=(self.validate_win_size, "win_size"))
        user_overide_listener = threading.Thread(target=self.event_listener, args=(self.check_user_override, "user_override"))

        win_size_listener.start()
        user_overide_listener.start()

        # Wait until one signals success
        win_valid_event.wait()

        # Get winner (if any)
        winner = None
        try:
            winner = result_queue.get_nowait()
        except queue.Empty:
            winner = (None, None)

        # Join children's threads with a short grace period
        win_size_listener.join(timeout=1.0)
        user_overide_listener.join(timeout=1.0)

        # Fallback: if threads still alive, mark them daemon so process can exit
        if win_size_listener.is_alive() or user_overide_listener.is_alive():
            win_size_listener.daemon = True
            user_overide_listener.daemon = True

        # If winner carried an exception, re-raise it here to surface errors
        name, payload = winner
        if isinstance(payload, Exception):
            raise payload

if __name__ == "__main__":
    validator = WinValidator()
