import youtube_dl
import json

class manager():
    links=None
    def __init__(self,links):
        self.links=links
        self.__putque(links)
        
    
    def __putque(self,links):
         lista=self.__getque()
         for i in links:  
             if not self.__checkque(i,lista):
                lista.append({"link":i,"finished":False})
         with open('lista.json','w') as f:     
             json.dump(lista,f,indent=2)

    def __getque(self):
        with open('lista.json') as json_file:
            data = json.load(json_file)
        return data

    def __updatequeue(self):
        pass
    
    def __checkque(self,valor, lista):
        for i in lista:
            if valor == i['link']:
                return True

    def start(self):
        
        ydl_opts = {
                'format': '137+140',
                'writesubtitles': True,
                'postprocessors': [{
                    'key': 'FFmpegSubtitlesConvertor',
                    'format': 'srt'

                }]
            }
#        self.__putque(links)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download(self.links)
                except youtube_dl.utils.DownloadError as err :
                    print('formato solicitado no existe')
