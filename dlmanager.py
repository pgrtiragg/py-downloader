import youtube_dl


class manager():
    def __init__(self):
        super().__init__()

    def start(self,links):
        ydl_opts = {
                'format': '137+140',
                'writesubtitles': True,
                'postprocessors': [{
                    'key': 'FFmpegSubtitlesConvertor',
                    'format': 'srt'

                }]
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(links)

