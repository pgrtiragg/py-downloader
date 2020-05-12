import youtube_dl
import json

class manager():
    links=None
    def __init__(self):
        super().__init__()
    
    def __putque(self,links):
         lista=list()
         for i in links:             
             lista.append({"link":i,"finished":False})
         with open('lista.json','a') as f:     
             json.dump(lista,f,indent=2)

    def start(self,links):
        self.links=links
        ydl_opts = {
                'format': '137+140',
                'writesubtitles': True,
                'postprocessors': [{
                    'key': 'FFmpegSubtitlesConvertor',
                    'format': 'srt'

                }]
            }
        self.__putque(links)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(self.links)

                try:
                    ydl.download(self.links)
                except youtube_dl.utils.DownloadError as err :
                    print('formato solicitado no existe')
