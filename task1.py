from bs4 import BeautifulSoup
import requests
import os.path
import json
import re
# import pprint

def scrap_top_list():
    if os.path.exists("movies.json")==True:
        with open("movies.json","r") as file:
	        read=file.read()    
        data=json.loads(read)
        return(data)
    else:
        url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
        sample=requests.get(url)
        soup=BeautifulSoup(sample.text,"html.parser")
        main_div=soup.find_all("table",class_="table")
        movie_ranks=[]
        movie_names=[]
        no_of_Reviews=[]
        movie_urls=[]
        movie_ratings=[]
        year_of_realease=[]
        for tr in main_div:
            for i in tr.find_all('tr')[1:]:
                movie_rank = i.find("td", class_="bold").text
                movie_ranks.append(movie_rank)

                movie_name = i.find("a", class_="unstyled articleLink").text.strip() 
                
                name=movie_name
                movie_name=re.split('(\d+)',name)
                year_of_realease.append(movie_name[-2])
                

                names=movie_name[0]
                namename=names.replace("(","")
                movie_names.append(namename)
                
                
                movie_review= i.find("td",class_="right hidden-xs").get_text()
                no_of_Reviews.append(movie_review)
            

                movie_rating = i.find("span",class_="tMeterScore").get_text()
                movie_ratings.append(movie_rating)
                

                url=i.find("a",class_="unstyled articleLink")['href']
                movie_url="https://www.rottentomatoes.com"+url
                movie_urls.append(movie_url)
                
        
        Top_Movies=[]
        details={'position':'','Rating':'','Name':'','year':"",'url':'','movie_Reviews':''}
        for i in range(0,len(movie_ranks)):
            details['position']=str(movie_ranks[i])
            details['Rating']=str(movie_ratings[i])
            details['Name']=str(movie_names[i])
            details['year']=str(year_of_realease[i])
            details['urls']=movie_urls[i]
            details['movie_Reviews']=str(no_of_Reviews[i])
            Top_Movies.append(details.copy())
        with open("movies.json","w")as file:
            data=json.dump(Top_Movies,file,indent=4)
        return Top_Movies   

# print(scrap_top_list)  
   
   
# pprint.pprint(scrap_top_list())
task1data=scrap_top_list()


# from random import randint
# num_acc = 0
# num_rand = 0
# acc = 0
# while True:
#     x = randint(0, 10)
#     num_rand += 1
#     if acc + x > 63:
#         print(' Discarding: ', x)
#         continue
#     else:
#         print('Considering: ', x)
#         num_acc += 1
#         acc += x
#         if acc == 63:
#             break
# print('%s numbers were generated, but only %s numbers were considered to reach the %s threshold' % (num_rand, num_acc, acc))





