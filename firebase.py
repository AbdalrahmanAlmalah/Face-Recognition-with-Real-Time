import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("Key.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://attendance-db-548be-default-rtdb.firebaseio.com/"
})     
ref=db.reference('people')
data = {
    "082114":
        {
            "name":"Abdalrahman Alamalah",
            "major":"AI",
            "Starting_year":2023,
            "total_attendance":1,
            "last_attendance_time":"2023-12-11 00:54:34" 
        
        
        
        },
        "182156":
        {
            "name":"Hazem Darwish",
            "major":"AI",
            "Starting_year":2021,
            "total_attendance":30,
            "last_attendance_time":"2023-1-11 08:30:11" 
        
        
        
        },
        "963852":
        {
            "name":"Elon musk",
            "major":"software",
            "Starting_year":2000,
            "total_attendance":8,
            "last_attendance_time":"2022-11-2 03:30:10" 
        
        
        
        }



}
for key,value in data.items():
    ref.child(key).set(value)