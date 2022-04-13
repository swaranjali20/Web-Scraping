from task1 import scrap_top_list
import json

data=scrap_top_list()

def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    return movie_dict
s=group_by_year(data)
f=open("task2.json","w")
f.write(json.dumps(s,indent=4))
f.close()