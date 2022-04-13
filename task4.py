import json
import requests
from bs4 import BeautifulSoup


def scrap_movie_details(link):
    dic={}

    link_data=requests.get(link)
    soup=BeautifulSoup(link_data.text,"html.parser")
    dic["name"]=soup.find("h1").text

    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    dic["Bio"]=movie_bio
    
    main = soup.find("div",class_="panel-body content_body")
    sub=main.find("ul",class_="content-meta info")
    all=sub.find_all("li",class_="meta-row clearfix")
 
    for i in all:
        dic[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").text.strip()
    print(dic)
    with open ("task4.json","w") as f:
        json.dump(dic,f,indent=4)
    ("https://www.rottentomatoes.com/m/black_panther_2018")

scrap_movie_details