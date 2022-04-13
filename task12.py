from bs4 import BeautifulSoup
import json 
import requests
import pprint
ullist=[]
with open("/home/swaranjali/Desktop/webscriping/movies.json","r") as file:
    data=file.read()
    last=json.loads(data)

for i in last:
    ullist.append(i["urls"])

def name(url_list):
    dic={}
    for i in url_list:
        list=[]
        adventure_api=requests.get(i)
        htmlcontent = adventure_api.text
        soup = BeautifulSoup(htmlcontent,"html.parser")
        title = soup.find('h1').text
        list=[] 
        cast_div=soup.find("div",class_="castSection")
        a2=cast_div.find_all("div",class_="cast-item")

        for k in a2:
            list.append(k.find("span")["title"])
        dic[title]=list
    
    with open("task12.json","w")as file:
            json.dump(dic,file,indent=4)

pprint.pprint(name(ullist))


