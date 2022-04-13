from task1 import task1data
import json
import pprint
from bs4 import BeautifulSoup
import requests
def get_movie_list_details(movies):
    # print(movies)
    j=0
    list4=[]
    while j<len(movies):
        
        newurl=movies[j]["urls"]
        # print(newurl)

        x=requests.get(newurl)
        soup=BeautifulSoup(x.text,"html.parser")
        movie_find_2=soup.find("ul",class_="content-meta info")
        movie_find_3=movie_find_2.find_all("li",class_="meta-row clearfix")

        my_dict={}
        for i in movie_find_3:
            my_dict[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").text.strip()
        
        list4.append(my_dict)

        j=j+1

    with open("task5.json","w")as f:
        json.dump(list4,f,indent=4)
    # pprint.pprint(list4)
    return list4
pprint.pprint(get_movie_list_details(task1data))
        