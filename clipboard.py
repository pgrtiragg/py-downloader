import threading
import pyperclip

class ClipboardWatcher(threading.Thread):
    urls = set()
    def __is_youtube_url(self,url):
        if 'https://www.youtube.com/watch?v=' in url:
            return True
        return False

    def __init__(self):
        super(ClipboardWatcher, self).__init__()

        self._stopping = False

    def run(self):
        recent_value = ""
        pyperclip.copy('')

        while not self._stopping:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value and self.__is_youtube_url(tmp_value):
                recent_value = tmp_value
                if recent_value not in self.urls:
                    self.urls.add(recent_value)
                    print(recent_value)

    def stop(self):
        self._stopping = True

    def get_urls(self):
        return self.urls