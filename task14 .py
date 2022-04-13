from bs4 import BeautifulSoup 
import json
import requests
from Task13 import task1data

def actor():
    # print(movie_list)
    with open('movies.json', 'r') as file:
        data=json.load(file)
        print(data)
    movie_url_list=[]
    for i in data:
        movie_url_list.append(i['urls'])
        # print(movie_url_list)
    lis=[]
    for i in range(20):
        lis.append(task1data(movie_url_list[i]))
    
    fin_dict={}
    for i in lis:
        for j in i["cast"]:
            if j not in fin_dict:
                fin_dict.update({j:[]})
    
      

    for i in fin_dict:
        for j in lis:
            if i in j["cast"]:
                for k in j["cast"]:
                    if i==k:
                        continue
                    fin_dict[i].append(k)
        
    with open('task14.json',  'w') as file:
        json.dump(fin_dict, file, indent=4)
    
actor()