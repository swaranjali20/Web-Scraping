import requests
from bs4 import BeautifulSoup
from Task12 import movie_cast
import json
# list=[]
def scrape_movie_details(link):
    cast=(movie_cast(link))
    # print(cast)
    CastMovieName={}
    url=requests.get(link)
    # print(url)
    soup=BeautifulSoup(url.text,"html.parser")
    # print(soup)
    CastMovieName["movie name"]=soup.find("h1").text
    # print(CastMovieName)
    main=soup.find("div",class_="panel-body content_body")
    # print(main)
    InforTable=main.find("ul",class_="content-meta info")
    # print(x)
    RowTable=InforTable.find_all("li",class_="meta-row clearfix")
    # print(RowTable)
    for i in RowTable:
        # print(i)
        CastMovieName[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())        
        # print(CastMovieName)
    CastMovieName["cast"]=cast
    # print(CastMovieName)
    with open("CastMovieData.json","w") as f:
        json.dump(CastMovieName,f,indent=2)
    return CastMovieName
    
        
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")