import requests
import json

#กำหนดค่า Line Notify
url = 'https://notify-api.line.me/api/notify'
# Line Notify Token
token = 'Token here'
headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':'Bearer ' +token }

#ดึงข้อมูล COVID-19
covid19_url = 'https://covid19.th-stat.com/api/open/today'
covid19_r = requests.get(covid19_url)
covid19_data = json.loads(covid19_r.content)

#ทดสอบแสดงผล
""" print("สรปุยอดผู้ติดเชื้อ COVID-19 ประจำวันที่ ", covid19_data["UpdateDate"], "\n")
print("ยอดรวมผู้ติดเชื้อ จำนวน: ", covid19_data["Confirmed"])
print("รักษาหายแล้วจำนวน: ", covid19_data["Recovered"])
print("ยังรักษาตัวอยู่ที่ โรงพยาบาล จำนวน: ", covid19_data["Hospitalized"])
print("เสียชีวิตแล้ว จำนวน: ", covid19_data["Deaths"])
print("ติดเชื่อเพิ่มเติม จำนวน: ", covid19_data["NewConfirmed"])
print("หายดีเพิ่มเติม จำนวน: ", covid19_data["NewRecovered"])
print("เข้ารับการรักษาเพิ่มเติม จำนวน: ", covid19_data["NewHospitalized"])
print("เสียชีวิตเพิ่มเติม จำนวน: ", covid19_data["NewDeaths"]) """

# จัดเรียงข้อมูล 
#ข้อมูลล่าสุด ผู้ติดเชื้อ COVID-19
msg = (
    "\n"
    + "สรปุยอดผู้ติดเชื้อ COVID-19 ประจำวันที่ "+ covid19_data["UpdateDate"]+ "\n"
    + "ติดเชื้อเพิ่มเติม จำนวน: "+ str(covid19_data["NewConfirmed"])+" คน"+ "\n"
    + "หายดีเพิ่มเติม จำนวน: "+ str(covid19_data["NewRecovered"])+" คน"+ "\n"
    + "เข้ารับการรักษาเพิ่มเติม จำนวน: "+ str(covid19_data["NewHospitalized"])+" คน"+"\n"
    + "เสียชีวิตเพิ่มเติม จำนวน: "+ str(covid19_data["NewDeaths"])+" คน"+ "\n"
    + "ยอดรวมผู้ติดเชื้อ จำนวน: "+ str(covid19_data["Confirmed"])+" คน"+ "\n"
    + "รักษาหายแล้ว จำนวน: "+ str(covid19_data["Recovered"])+" คน"+ "\n"
    + "ยังรักษาตัวอยู่ที่ โรงพยาบาล จำนวน: "+ str(covid19_data["Hospitalized"])+" คน"+ "\n"
    + "รวมผู้ที่เสียชีวิต จำนวน: "+ str(covid19_data["Deaths"])+" คน"+ "\n"
)

#ส่งข้อมูลไปยัง Line Notify
r = requests.post(url, headers=headers, data= {'message':msg})
print(r.text)
