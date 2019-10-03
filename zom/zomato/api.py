import requests
import json
import pprint
from .models import rst

def get_rest(c_id):
    api_token = '0c3e9be2aa9cf4b320d1e24f2a36a5bb'
    api_url_base = 'https://developers.zomato.com/api/v2.1/search?entity_id='+str(c_id)+'&count=5&entity_type=city&sort=rating'
    headers = {'user-key': api_token}
    response = requests.get(url =api_url_base, headers=headers)
    p = response.json()
    #parsed = json.loads(response.content)
    #pprint.pprint(p)
    address=[]
    pic=[]
    name=[]
    url=[]
    for i in p['restaurants']:
        new = i['restaurant']
        address.append(new['location']['address'])
        name.append(new['name'])
        pic.append(new['thumb'])
        url.append(new['url'])
    
    for j in range(len(name)):
        d = rst.objects.count()
        if d == 5:
            if rst.objects.filter(name=name[j],img=pic[j],adress=address[j],url=url[j]).exists():
                break
            else:
                ab = rst.objects.update(name=name[j],img=pic[j],adress=address[j],url=url[j])
         
        else:
            ab = rst.objects.create(name=name[j],img=pic[j],adress=address[j],url=url[j])
            ab.save()



