from task1 import task1data
import requests
from bs4 import BeautifulSoup
# import pprint
import json
# import random
# import time
import os
            
url_list=[]
for i in task1data:
    # print(i)
    url_list.append(i["urls"])
    # print(url_list)
def text_file(ulist):
    # print(text_file)
    last=[]
    for i in ulist:
    #     print(i)
        id=i[33:]
        # print(id)
        if os.path.exists(id+".json")==True:
            with open (id+".json","r")as movieDataFile:
                data=movieDataFile.read()
                # print(data)
                final=json.loads(data)
                # print(final)
            last.append(final)
            # print(last)
        else:
            final={}
            LinkData=requests.get(i)
            # print(LinkData)
            soup=BeautifulSoup(LinkData.text,"html.parser")
            # print(soup)
            final["name"]=soup.find("h1").text
            # print(final)
            main=soup.find("ul",class_="content-meta info")
            # print(main)
            all=main.find_all("li",class_="meta-row clearfix")
            # print(all)
            for i in all:
                # print(all)
                final[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").text.strip()
                # print(final) 
                with open(id+".json","w")as file:
                    json.dump(final,file,indent=4)
                last.append(final)
                # print(last)
        
        # return last
text_file(url_list)




# from requests.sessions import _Data
# from task1 import task1data
# import requests
# from bs4 import BeautifulSoup
# import pprint
# import json
# import random
# import time
# import os
# import json
# import requests

# from bs4 import BeautifulSoup
# import os
# def scrap_movie_details(link):
    # print(link)
    # id=link[33:]
    # print(id)
#     if os.path.exists("/home/swaranjali/Desktop/webscrapping/"+id+".json")==True:
#                 with open("/home/swaranjali/Desktop/webscrapping/"+id+".json","r") as movieDataFile:
#                     data=movieDataFile.read()
#                     final=json.loads(data)
#     else:
#                 final={}
#                 LinkData=requests.get(link)
#                 soup=BeautifulSoup(LinkData.text,"html.parser")
#                 final["name"]=soup.find("h1").text
#                 main=soup.find("ul",class_="content-meta info")
#                 all=main.find_all("li",class_="meta-row clearfix")
#                 for i in all:
#                     final[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.strip()
#                 with open("/home/swaranjali/Desktop/webscrapping/"+id+".json","w") as file:
#                     json.dump(final,file,indent=2)
#     return final
# scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")
