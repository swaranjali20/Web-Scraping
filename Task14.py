from bs4 import BeautifulSoup
import json
import requests
from task13 import scrape_movie_details

def actor():
    with open("movies.json", 'r') as file:
        data=json.load(file)
        # print(data)
    movie_url_list=[]
    for i in data:
        # print(i)
        movie_url_list.append(i['urls'])
        # print(movie_url_list)
    lis=[]
    for i in range(20):
        # print(i)
        lis.append(scrape_movie_details(movie_url_list[i]))
        # print(lis)
    
    fin_dict={}
    for i in lis:
        # print(i)
        for j in i["cast"]:
            # print(i)
            if j not in fin_dict:
                fin_dict.update({j:[]})
                # print(fin_dict)
    
    

    for i in fin_dict:
        # print(i)
        for j in lis:
            # print(j)
            if i in j["cast"]:
                for k in j["cast"]:
                    # print(k)
                    if i==k:
                        continue
                    fin_dict[i].append(k)
                    break
                    # print(fin_dict)
        
    with open('AllActorData.json',  'w') as file:
        json.dump(fin_dict, file, indent=4)
    
    
    

actor()