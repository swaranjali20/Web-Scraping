import json

file=open("task5.json","r")
var=json.load(file)
# print(var)

def get_lang_count(var):
    list1=[]
    list2=[]  

    for i in var:
        # print(i)
        file1=i["Genre:"].split()
        # print(file1)

        # print(file1)
        for j in file1:
            # print(j)
            if j[-1]==",":
                j=j[:-1]
                # print(j)
        list2.append(j)
    for i in list2:
        # print(i)
        if i not in list1:
            list1.append(i)
    # print(list1)
    dict={}
    for l in list1:
        # print(l)
        count=0
        h=0
        while h <len(list2):
            # print(h)
            if l==list2[h]:
                count+=1
            h+=1
        dict.update({l:count})
    # print(dict)

    with open("task11.json","w") as file:
        json.dump(dict,file,indent=4)

get_lang_count(var)