import requests
import json

def Get_datas(luogu_id):
    difficulty = [0 for i in range(50)]

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42' ,
    }

    url = f'https://www.luogu.com.cn/user/{luogu_id}?_contentOnly=1' 

    res = requests.get(url = url , headers = headers).text
    datas = json.loads(res)['currentData']
    name = datas['user']['name']
    try:
        datas = datas['passedProblems']
        for i in datas:
            tmp = i['difficulty']
            difficulty[tmp] += 1
    except:
        pass
    return (difficulty[:8] , name)
