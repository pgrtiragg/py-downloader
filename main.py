from  dlmanager import manager
from clipboard import ClipboardWatcher
import time
def main():
    watcher = ClipboardWatcher()
    watcher.start()
    while True:
        try:
            # print "Waiting for changed clipboard..."
            time.sleep(1)
        except KeyboardInterrupt:
            watcher.stop()
            mgr=manager(watcher.get_urls())
            mgr.start()
            break


if __name__ == "__main__":
    main()