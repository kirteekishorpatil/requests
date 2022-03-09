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