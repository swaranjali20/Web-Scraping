from task5 import data2
print(data2)

import pprint
import os
from bs4 import BeautifulSoup
import json
import requests
# from task12 import ullist
from task1 import task1data
# print(ullist)

def task13(movies):
    if os.path.exists("/home/swaranjali/Desktop/webscriping/task13.json")==True:
        with open("/home/swaranjali/Desktop/webscriping/task13.json","r")as file:
            data=file.read()
            print(data)
            t13=json.loads(data)
        return t13
    else:
        final=[]
        for k in range(len(movies)):
            cast_list=[]
            x=requests.get(movies[k]["urls"])
            soup=BeautifulSoup(x.text,"html.parser")
            main=soup.find("div",class_="castSection")
            all=main.find_all("div",class_="cast-item")
            for i in all:
                cast_list.append(i.find("span")["title"])
            with open("/home/swaranjali/Desktop/webscriping/task5.json","r") as file:
                data=file.read()
                fdata=json.loads(data)
                fdata[k]["cast"]=cast_list
                final.append(fdata)
                # print(cast_list)
            # final.append(fdata)
        with open ("task13.json","w")as file:
            json.dump(final,file,indent=4)
        return final
pprint.pprint(task13(task1data))



