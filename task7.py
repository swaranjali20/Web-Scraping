import json

def final (text):
    return " ".join(text.split())

def movie_directors():
    file2=open("task5.json","r")
    h=json.load(file2)

    list=[]
    for i in h:
        x=final(i["Director:"])
        # print(x)

        if x not in list:
            list.append(x)
        
    dict8={}
    list9=[]
    for k in list:
        # print(k)
        i=0
        count=0
        while i<len(h):
            
            if k==final(h[i]["Director:"]):
                
                count=count+1
            i=i+1
        dict8[k]=count
    # list.append(dict8)
    print(dict8)
    with open("task7.json","w")as file:
        json.dump(dict8,file,indent=4)
movie_directors()

