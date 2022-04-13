# from task1 import scrap_top_list
# import json
# data=scrap_top_list()
# def group_by_decade(movies):
#     moviedec={}
#     list1=[]
#     for index in movies:
#         mod=index["year"]%10
#         decade=index["year"]-mod
#         if decade not in list1:
#             list1.append(decade)
#     list.sort()
#     for i in list1:
#         moviece_list=[]
#         for x in movies:
#             if x["year"]>=i and x["year"]<=i+10:
#                 moviece_list.append(x)
#                 moviedec[i]=moviece_list
#                 with open("task_3.json","w")as k:
#                     json.dump(moviedec,k,indent=4)
# group_by_decade(data)

from task1 import scrap_top_list
import json
name=scrap_top_list()
def group_by_decade(name):
    movisedec={}
    list1=[]
    for index in name:
        mod=int(index["year"])%int(10)
        decode=int(index["year"])-int(mod)
        if decode not in list1:
            list1.append(decode)
    
    list1.sort()
    for i in list1:
        movies_list=[]
        for x in name:
            if int(x["year"])>=i and int(x["year"])<=i+10:
                movies_list.append(x)
                movisedec[i]=movies_list
                with open("naini.json","w")as file:
                    json.dump(movisedec,file,indent=4)
group_by_decade(name)

