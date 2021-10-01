
import requests



def searchmus(artist,title):
    
    request = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')

    tek = request.status_code

    if tek==200:
        rq =  request.json()
        
        matni = str(rq['lyrics'])
        matni = matni.replace('\n\n', '\n')
        return matni + '\n'
    else:
        javob = "❗️So'rovda xatolik!!\nIltimos tekshirib qaytadan kiriting\n"
        return javob

