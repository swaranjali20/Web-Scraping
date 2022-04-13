import json
def movie_directors():
    file2=open("task5.json","r")
    h=json.load(file2)

    list=[]
    for i in h:
        if i ["Original Language:"]not in list:
            list.append(i["Original Language:"])
        
    dict8={}
    list9=[]
    for k in list:
        # print(k)
        i=0
        count=0
        while i<len(h):
            
            if k==h[i]["Original Language:"]:
                
                count=count+1
            i=i+1
        dict8.update({k:count})
    list.append(dict8)
    with open("task6.json","w")as file:
        json.dump(dict8,file,indent=4)
movie_directors()

