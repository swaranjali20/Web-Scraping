# from bs4 import BeautifulSoup
# import json 
# import requests
# import pprint
# def name():
#     adventure_url="https://www.rottentomatoes.com/m/black_panther_2018"
#     adventure_api=requests.get(adventure_url)
#     # print(adventure_api)    
#     j=0
#     list=[]
 
#     while j<len(adventure_url):
#         adventure_api=requests.get(adventure_url)
#         htmlcontent = adventure_api.content
#         soup = BeautifulSoup(htmlcontent,"html.parser")
#         cast_div=soup.find("div",class_="castSection")
#         a2=cast_div.findAll("div",recursive=False)

#         dict={}
    
#         for i in a2:
        
#             a2=i.find("div",class_="media-body")
        
#             list.append(a2.a.span.get_text().strip())
    
    
#     with open("Task12.json","w") as f:
#         json.dump(list,f,indent=2)
#     return list
# data=name()

# #         my_dict={}
# #         for i in a2:
# #             a2=i.find("div",class_="media-body")
# #             my_dict[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").text.strip()
        
# #         list.append(my_dict)

# #         j=j+1

# #     with open("task5.json","w")as f:
# #         json.dump(list,f,indent=4)
# #     pprint.pprint(list)
# # name()

# def name():
#     raw="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
# # print(raw)
#     i=0
#     list=0
#     while i<len(raw):
#         # print(raw)
#         adventure_api=requests.get(raw)
#         htmlcontent = adventure_api.content
#         soup = BeautifulSoup(htmlcontent,"html.parser")
#         cast_div=soup.find("ul",class_="content-meta info")
#         print(cast_div)
#         a2=cast_div.findAll("li",class_="meta-row clearfix")






# name()



from bs4 import BeautifulSoup
import json
import requests



def movie_cast(movie_url):
    cast_list=[]
    data=requests.get(movie_url)
    soup=BeautifulSoup(data.text,"html.parser")
    main=soup.find_all("div",class_="panel-body content_body")
    section=main[1].find("div",class_="castSection")
    all=section.find_all("div",class_="cast-item")
    for i in all:
        cast_list.append(i.find("span")["title"])
    # return cast_list
    with open("CastData.json","w") as f:
        json.dump(cast_list,f,indent=3)
    return cast_list    

data=movie_cast("https://www.rottentomatoes.com/m/black_panther_2018")