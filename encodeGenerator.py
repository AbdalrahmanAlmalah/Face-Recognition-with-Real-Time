import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db ,storage
cred = credentials.Certificate("Key.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://attendance-db-548be-default-rtdb.firebaseio.com/",
    "storageBucket":"attendance-db-548be.appspot.com"
})     
#Importing People Images
folderPath="Images"
pathList=os.listdir(folderPath)
imgList=[]
peopleIds=[]
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    os.path.splitext(path)[0]
  #  print(os.path.splitext(path)[0])
    peopleIds.append(os.path.splitext(path)[0]) 

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    
def findEncoding(imgList):
    encodeList=[]
#COVERT IMG COLOR 
    for img in imgList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("ENCODING....")
encodeListKnown = findEncoding(imgList)   
encodeListKnownIds=[encodeListKnown,peopleIds]
print(encodeListKnown)
print("ENCODING COMPLETE")
file = open("EncodeFile.p","wb")
pickle.dump(encodeListKnownIds,file)
file.close()
print("File Saved :)")