
# from typing import container
import requests
from bs4 import BeautifulSoup
import pprint
import random
import json
import time
import os.path


def task_1():
    # print(task_1)
    file_name="home/swaranjali/Desktop/webscriping/movies.json"
    # print(file_name)
    file_exists=os.path.exists(file_name)
    # print(file_exists)
    if file_exists==True:   
        with open (file_name,"r")as jsonfile:
            data=jsonfile.read()
            print(data)
            pobj=json.load(data)
        return pobj
    else:
        response=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
        soup=BeautifulSoup(response.text,"html.parser")   
        tab=soup.find("table",class_="table")
        movies=tab.find_all("tr")
        # print(movies)
        sr_list=[]
        title_list=[]
        rating_list=[]
        reviewscount_list=[]
        link_list=[]
        year_list=[]
        base="https://www.rottentomatoes.com"
        # print(base)
        for k in range (1,len(movies)) :
            # print(k)    
            tag=movies[k].find_all("td")
            # print(tag)

            sr=(tag[0]).text.strip()
            sr_list.append(sr)    
            # print(sr_list)  
            rating=(tag[1]).text.strip()
            rating_list.append(rating)
            # print(rating_list)
            title=(tag[1]).text.strip  ()
            Name=" " 
            for i in title:
                if i=="(":# can also use alpha() and isdigit() for detecting if elements of a strip()
                    break
                else:
                    Name=Name+i
            title_list.append(Name)

            r=len(title)-(len(title)-5)
            print(r)
            title=title[::-1]
            s=""
            for i in range(r):
                if title[i]=="("or title[i]==")":
                    print(title)
                    pass
                else:
                    s+=title[i] 
            year=s[::-1]
            year_list.append(year)

            link=base+(tag[2]).a["href"].strip()
            link_list.append(link) 

            no_of_reviews=(tag[3]).text.strip()
            reviewscount_list.append(no_of_reviews)  

        Top_Movies=[]
        for i in range (len(sr_list)):
            info={}
            info["position"]=sr_list[i]
            info["name"]=title_list[i]
            info["year"]=year_list[i]
            info["rating"]=rating_list[i]
            info["no_of_reviews"]=reviewscount_list[i]
            info["url"]=link_list[i]
            Top_Movies.append(info)
        with open(file_name,"w")as jsonfile:
            json.dump(Top_Movies,jsonfile,indent=2)
        with open(file_name,"r")as jsonfile:
            data=jsonfile.read()
            pobj=json.loads(data)
        return pobj
movie=task_1()
def task_6(movies_list):
    url_list=[]
    for i in movies_list:
        url_list.append(i["movie URL"])
    return url_list
url_list=task_6(movie)
def final(text):
    return" ".join(text.split())
def task_8(urlist):
    f=[]
    for movie_url in urlist:
        random_sleep=random.randint(1,3)
        id=movie_url[33:]
        file_name="/home/swaranjali/Dekstop/webscriping/task_8.py"+id+".json"
        file_exists=os.path.exists(file_name)
        if file_exists==True:
            with open(file_name,"r")as jsonfile:
                data=jsonfile.read()
                p=jsonfile.loads(data)
                f.append(p)
        else:
            time.sleep(random_sleep)
            response =requests.get(movie_url)
            soup=BeautifulSoup(response.text,"html.parser")
            title=(soup.find("h1")).text
            container=soup.find("div",class_="panel-body content_body")
            sub_container = container.find("ul",class_="content-meta info")
            all=sub_container.find_all("li",class_="meta-row clearfix")
            details={}
            for i in all:
                details[(i.find("div",class_="meta-label subtle")).text]=final((i.find("div",class_="meta-value")).text.strip())
            details["Name:"]=title
            with open(file_name,"w")as jsonfile:
                json.dump(details,jsonfile,indent=2)
            with open(file_name,"r")as jsonfile:
                data=jsonfile.read()
                p=json.load(data)
                f.append(p)
    return f
pprint.pprint(task_8(url_list[:1]))
            
  

                                                                                                                                                