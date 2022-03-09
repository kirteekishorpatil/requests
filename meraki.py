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
course_no_1=int(input("enter your number do you want in id"))
print(var1[course_no_1-1]["name"])
idd=var1[course_no_1-1]["id"]
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
point=int(input("enter the point"))
for k in list1:
    if k["parent_exercise_id"]==k["id"]:
        print(list1[point-1]["name"])
        num=(list1[point-1]["id"])
        break










    
       
       












 
# 

    
    
    
        
# 






#




        
       
        
         
    
    
        





    
    

    










                
                
            








            
            
                
                    


















