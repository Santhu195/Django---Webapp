import requests
import json

def get_rest(c_id):
    api_token = '0c3e9be2aa9cf4b320d1e24f2a36a5bb'
    api_url_base = 'https://developers.zomato.com/api/v2.1/search?entity_id='+str(c_id)+'&entity_type=city&sort=rating'
    headers = {'user-key': api_token}
    response = requests.get(url =api_url_base, headers=headers)
    p = response.json()
    #parsed = json.loads(response.content)
    #print(p)
    name = []
    url=[]
    pic = []
    dic= {}

    for i in p['restaurants']:
        rest_details = i['restaurant']
        name.append(rest_details['name'])
        url.append(rest_details['url'])
        pic.append(rest_details['thumb'])
    for i in range(len(name)):
        dic[i] = {
            'name':name[i],
            'url':url[i],
            'pic':pic[i],
            }      
    return dic


