# a="nutan"
# print(a[0:2])

# from task1 import task1data
# import os
# import json
# import requests
# import random
# import time
# import pprint
# from bs4 import BeautifulSoup
# url_list=[]
# for i in task1data:
#     url_list.append(i["movie_urls"])


                                                                                                                                                                                                    




















# movie_detailsLst()






from task1 import task1data
import os 
import json
import requests
import random
import time
import pprint       
from bs4 import BeautifulSoup
url_list=[]
for i in task1data:
    url_list.append(i["movie_urls"])
def text_file(ulist):
    last=[]
    time_sleep=random.randint(1,3)
    for i in ulist:
        id=i[33:]
        if os.path.exists("/home/vinaata/Desktop/vaishnavi_webscrapping/"+id+".json")==True:
            with open("/home/vinaata/Desktop/vaishnavi_webscrapping/"+id+".json","r") as movieDataFile:
                data=movieDataFile.read()
                final=json.loads(data)
            last.append(final)
        else:
            final={}
            time.sleep(time_sleep)
            LinkData=requests.get(i)
            soup=BeautifulSoup(LinkData.text,"html.parser")
            final["name"]=soup.find("h1").text
            main=soup.find("ul",class_="content-meta info")
            all=main.find_all("li",class_="meta-row clearfix")
            for i in all:
                final[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.strip()
            with open("/home/vinaata/Desktop/vaishnavi_webscrapping/"+id+".json","w") as file:
                json.dump(final,file,indent=2)
            last.append(final)
    return last
pprint.pprint(text_file(url_list))