import time
import threading
import pyperclip
import youtube_dl


def is_youtube_url(url):
    if 'https://www.youtube.com/watch?v=' in url:
        return True
    return False


class ClipboardWatcher(threading.Thread):
    urls = set()

    def __init__(self):
        super(ClipboardWatcher, self).__init__()

        self._stopping = False

    def run(self):
        recent_value = ""
        pyperclip.copy('')

        while not self._stopping:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value and is_youtube_url(tmp_value):
                recent_value = tmp_value
                if recent_value not in self.urls:
                    self.urls.add(recent_value)
                    print(recent_value)

    def stop(self):
        self._stopping = True

    def get_urls(self):
        return self.urls


def main():
    watcher = ClipboardWatcher()
    watcher.start()
    while True:
        try:
            # print "Waiting for changed clipboard..."
            time.sleep(1)
        except KeyboardInterrupt:
            watcher.stop()            
   ydl_opts = { 'format': '137+140',
 'writesubtitles':True, 
'postprocessors': [{ 'key': 'FFmpegSubtitlesConvertor', 'format':'srt'}]

}

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(watcher.get_urls())

            break


if __name__ == "__main__":
    main()
