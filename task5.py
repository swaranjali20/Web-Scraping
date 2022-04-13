# from task1 import task1data
# import json
# from bs4 import BeautifulSoup
# import requests

# # scrapped=task1data()
# def get_movie_list_details(movies):
    
#     j=0
#     list4=[]
#     while j<len(movies):
#         newurl=movies[j]["urls"]
#         url=newurl
#         x=requests.get(url)
#         soup=BeautifulSoup(x.text,"html.parser")
#         movie_find_2=soup.find("ul",class_="content-meta info")
#         movie_find_3=movie_find_2.find_all("li",classs_="meta-row clearfix")
#         my_dict={}
#         for i in movie_find_3:
#             alldata=i.find("div",class_="meta_label subtitle").get_text().strip()
#             allvalue=i.find-all("div",class_="meta_value").get_text().replace("\n",'')
#             my_dict.update({alldata:allvalue})
#         list4.append(my_dict)

#         j+=1
#         print(my_dict)
#     with open("Task5.json","w")as f:
#             json.dump(list4,f,indent=4)
#     return list4
# get_movie_list_details(task1data)



# from task1 import task1data
# import pprint
# import json
# from bs4 import BeautifulSoup
# import requests
import pprint

# def get_movie_list_details(movies):
#     j=0
#     list4=[]
#     while j<len(movies):
#         newurl=movies[j]["urls"]
#         x=requests.get(newurl)
#         soup=BeautifulSoup(x.text,"html.parser")
#         main=soup.find("ul",class_="content-meta info")
#         all=main.find-all("li",class_="meta-row clearfix")
#         my_dict={}

#         for i in all:
#             my_dict[i.find("div",class_="meta-label subtle").get_text().strip()]=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
#         title=soup.find("h1")
#         my_dict["name"]=title.text
#         list4.append(my_dict)
#         j+=1
        
#     with open("task5.json","w")as f:
#         json.dump(list4,f,indent=4)
#     return list4
# # pprint.pprint(get_movie_list_details(task1data[:10]))
# t5=get_movie_list_details(task1data)

from task1 import task1data
import json
from bs4 import BeautifulSoup
import requests
# scrapped=scrap_top_list
# pprint.pprint(task1data)
def get_movie_list_details(movies):
    j=0
    list4=[]
    while j<len(movies):
        # newurl=movies[j]["movie_url"]
        newurl=movies[j]["urls"]
        # print(newurl)
        # url=newurl
        x=requests.get(newurl)
        soup=BeautifulSoup(x.text,"html.parser")
        movie_find_2=soup.find("ul",class_="content-meta info")
        movie_find_3=movie_find_2.find_all("li",class_="meta-row clearfix")
        # title=soup.find("h1")

        # print(movie_find_2)
        # print(movie_find_3)
        my_dict={}
        for i in movie_find_3:
            # my_dict[movie_find_2[i].get_text().strip()]=movie_find_3[i].get_text().strip()
            my_dict[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
            # alldata=i.find("div",class_="content-meta info")
            # allvalue=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
            # my_dict.update({alldata:allvalue})

        my_dict["name"]=movies[j]["Name"]
        list4.append(my_dict)

        j=j+1
        
    with open("task5.json","w")as f:
        json.dump(list4,f,indent=4)
    # pprint.pprint(list4)
    return list4
pprint.pprint(get_movie_list_details(task1data))
# pprint.pprint(task1data)



