

# import json
# with open("task12.json","r")as file:
#     data=json.load(file)




# import json
# with open("task12.json","r")as f:
#     data = json.load(f)

# def analyse_movie_actors(data):
#     actors_dic = {}
#     for dic in data:
#         if "tittle" in dic:
#             actors = dic["tittle"]
#             if actors not in actors_dic:
#                 actors_dic = dic["tittle"]
#                 actors_dic[actors] = 1
#             else:
#                 actors_dic[actors] += 1
#         else:
#             continue
#     with open("web15.json","w+") as file6:
#         json.dump(actors_dic,file6,indent = 4)
# analyse_movie_actors(data)




# import json,pprint

# f=open("task12.json","r")
# load_data=json.load(f)
# f.close()

# def analyse_actors(movie_list):
#     dic={}
#     dic2={}
#     list=[]
#     for movie in movie_list:
#         # print(movie)
#         list.append(movie)
#     # print(list)
#     for i in list:
#         # print (i["Name"])
#         dic["Name"]=i["Name"]
#     print(dic)
    
#         cast= (movie["cast"])
#         for i in cast:
#             name=(i["Imdb_Id"])
#             if name in dic:
#                 dic[name]+=1
#             else:
#                 dic[name]=1
#     for i in dic:
#         for movie in movie_list:
#             cast=movie["cast"]
#             for j in cast:
#                 if i== (j["movie_Id"]) and i not in dic2:
#                     dic2[i]={"Name":j["Name"],"num_movies":dic[i]}
#     f=open('imdb_list_15.json','w')
#     json.dump(dic2,f,indent=4)
#     f.close()
#     with open ("task15.json","w")as file:
#         json.dump(dic2,file,indent=4)

#     return dic2
# task15=analyse_actors(load_data)
# pprint.pprint(task15)





import json,pprint

f=open("task12.json","r")
load_data=json.load(f)
f.close()

def analyse_actors(movie_list):
    dic={}
    dic2={}
    list1=[]
    list2=[]
    for movie in movie_list:
        list1.extend(movie_list[movie])
    print(list(set(list1)))
    for a in list1:
        final = {"Actor": a, "Movies": 0}
        for m in movie_list:
            if a in movie_list[m]:
                final['Movies']+=1
        list2.append(final)
    pprint.pprint(list2)
    with open ('task15.json','w') as file:
        json.dump(list2,file,indent=4)

task15=analyse_actors(load_data)