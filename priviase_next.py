import requests
import json
url1=requests.get("https://api.merakilearn.org/courses") 
var1=url1.json()
with open("course.json","w")as f:
    json.dump(var1,f,indent=4)
serial_no=1
for i in var1:
    print(serial_no,i["name"],i["id"])
    serial_no=serial_no+1
course_no_1=int(input("enter the sirial number do you want........."))
print(var1[course_no_1-1]["name"])
idd=var1[course_no_1-1]["id"]

np=input("what do you want privious(p).... or next(n).......")
if np=="p":
    url1=requests.get("https://api.merakilearn.org/courses") 
    var1=url1.json()
    with open("course.json","w")as f:
        json.dump(var1,f,indent=4)
    serial_no=1
    for i in var1:
        print(serial_no,i["name"],i["id"])
        serial_no=serial_no+1
    course_no_1=int(input("enter the sirial number do you want........."))
    print(var1[course_no_1-1]["name"])
    idd=var1[course_no_1-1]["id"]
    np2=input("what do you want privious(p)......or next(n)....")
    if np2=="p":
        url2=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
        var2=url2.json()
        with open("topic.json","w")as h:
            json.dump(var2,h,indent=5)
            serial_no2=1
            list1=[]
            list2=[]
        for j in var2["course"]["exercises"]:
            if j["parent_exercise_id"]==None:
                print(serial_no2,j["name"])
                print("      ",serial_no2,j["slug"])
                serial_no2+=1
                list1.append(j)
                list2.append(j)
                continue
            if j["parent_exercise_id"]==j["id"]:
                print(serial_no2,j["name"])
                serial_no2+=1
                new_no=1
                list1.append(j)
            for t in var2["course"]["exercises"]:
                if j["parent_exercise_id"]!=j["id"]:
                    print("       ",new_no,j["name"])
                    new_no+=1
                    list2.append(j)
                    break
        with open("topic1.json","w")as f:
            json.dump(list1,f,indent=4)
        point=int(input("enter the parents.....no"))
        for k in list1:
            if k["parent_exercise_id"]==k["id"]:
                print(list1[point-1]["name"])
                num=(list1[point-1]["id"])
                break
        var=[]
        var3=[]
        new_no1=1
        for n in list2:
            if n["parent_exercise_id"]==num:
                print("    ",new_no1,n["name"])
                var.append(n["name"])
                var3.append(n["content"])
                new_no1+=1
else:
    url2=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
    var2=url2.json()
    with open("topic.json","w")as h:
        json.dump(var2,h,indent=5)
        serial_no2=1
        list1=[]
        list2=[]
    for j in var2["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_no2,j["name"])
            print("      ",serial_no2,j["slug"])
            serial_no2+=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(serial_no2,j["name"])
            serial_no2+=1
            new_no=1
            list1.append(j)
        for t in var2["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print("       ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
    point=int(input("enter the parents.....no"))
    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[point-1]["name"])
            num=(list1[point-1]["id"])
            break
    var=[]
    var3=[]
    new_no1=1
    num=0
    for n in list2:
        if n["parent_exercise_id"]==num:
            print("    ",new_no1,n["name"])
            var.append(n["name"])
            var3.append(n["content"])
            new_no1+=1
np2=input("what do you want privious(p)......or next(n)....")
if np2=="p":
    url2=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
    var2=url2.json()
    with open("topic.json","w")as h:
        json.dump(var2,h,indent=5)
        serial_no2=1
        list1=[]
        list2=[]
    for j in var2["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_no2,j["name"])
            print("      ",serial_no2,j["slug"])
            serial_no2+=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(serial_no2,j["name"])
            serial_no2+=1
            new_no=1
            list1.append(j)
        for t in var2["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print("       ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
    point=int(input("enter the parents.....no"))
    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[point-1]["name"])
            num=(list1[point-1]["id"])
            break
    var=[]
    var3=[]
    new_no1=1
    for n in list2:
        if n["parent_exercise_id"]==num:
            print("    ",new_no1,n["name"])
            var.append(n["name"])
            var3.append(n["content"])
            new_no1+=1
else:
    point1=int(input("enter the chiled.....no"))
    new_no2=1
    for s in range(0,len(var)):
        if point1==new_no2:
            print(var[s])
            print(var3[s])
        new_no2+=1

questions_no = int(input("choose the specific questions no :- "))
question=questions_no-1
print(var[question])
while questions_no > 0 :

# Here a taking user input in a previous or next

    next_question = input("do you next question or previous question n/p :- ")
    if questions_no == len(var):
        print("next page")
    if next_question == "p" :
        if questions_no == 1:
            print("no more questions")
            break
        # else:
        elif questions_no > 0:
            questions_no = questions_no  -1
            print(var[questions_no])
    elif next_question == "n":
        if questions_no < len(var):
            index = questions_no + 1
            print(var[index-1])
            question = question + 1
            questions_no = questions_no + 1 
            if question == (len(var)-1) :
                print("next page")
                break
