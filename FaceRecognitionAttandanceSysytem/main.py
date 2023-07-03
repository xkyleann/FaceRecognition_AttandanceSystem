import cv2
import cvzone
import os
import face_recognition
import pickle
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

#Load Firebase credentials and initialize the app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-b9b88-default-rtdb.europe-west1.firebasedatabase.app/",
    'storageBucket': "facerecognition-b9b88.appspot.com"
})
#Time limit in seconds
timelimit=60

#Access the storage bucket
bucket = storage.bucket()

#Open the camera of the device
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#Load background image
imgBackground = cv2.imread('graphics/background.png')

#Paths for different mode images
folderModePath = 'graphics/Modes'
modePathList = os.listdir(folderModePath)

#List to store the loaded mode images
imgModeList = []

#Initialize the mode type
modeType = 0

file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds

#Load the mode images and append them to the list
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

#Initialize variables for face recognition
modeType = 0
counter = 0
id = -1
imgStudent = []

if(timelimit<15):
    timelimit=15

while True:
    #Read the frame from the camera
    success, img = cap.read()

    #Resize and convert the frame to RGB
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    #Perform face detection on the current frame
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    #Update the background image with the current frame
    imgBackground[157:157 + 480, 63:63 + 640] = img

    #Get the current time and display it on the background image
    now = datetime.now()
    cv2.rectangle(imgBackground,(782,80),(1010,110),(255,255,255),-1)
    cv2.putText(imgBackground, now.strftime('%Y-%m-%d %H:%M:%S'), (782, 103),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 85, 1), 2)

    #Update the background image based on the mode type
    if modeType == 1:
        imgBackground[156:156 + 333, 768:768 + 455] = imgModeList[modeType]
    else:
        imgBackground[526:526 + 111, 768:768 + 455] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            #Compare the face encodings with the known encodings
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            #Get the index of the best match
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                #Extract the face location coordinates
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                #Draw a rectangle around the face
                bbox = 63 + x1, 157 + y1, x2 -x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

                #Get the student ID of the matching face
                id = studentIds[matchIndex]

                if counter == 0:
                    #counter = 1 when face is matching
                    counter = 1
                    modeType = 1

        if counter != 0:
                if counter == 1:
                    #Retrieve the student information from the database
                    studentInfo = db.reference(f'Students/{id}').get()
                    if studentInfo!=None:
                        print(studentInfo)

                        #Retrieve the student image from the storage bucket
                        blob = bucket.get_blob(f'Images\{id}.png')
                        array = np.frombuffer(blob.download_as_string(), np.uint8)
                        imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                        #Update the attendance data
                        datetimeObject = datetime.strptime(studentInfo['last_attendance_time'],
                                                          "%Y-%m-%d %H:%M:%S")
                        secondsElapsed = (datetime.now()-datetimeObject).total_seconds()
                        print(secondsElapsed)
                        if secondsElapsed > timelimit:
                            #Increase the total attendance count
                            ref = db.reference(f'Students/{id}')
                            studentInfo['total_attendance'] +=1
                            ref.child('total_attendance').set(studentInfo['total_attendance'])
                            #Update the last attendance time
                            ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                        else:
                            modeType = 3
                            counter = 0
                            imgBackground[526:526 + 111, 768:768 + 455] = imgModeList[modeType]
                            #cv2.rectangle(imgModeList[1],(38,35),(200,297),(0,0,0),-1)
                            cv2.rectangle(imgBackground, (800, 180), (1200, 470), (255, 255, 255), -1)
                            cv2.rectangle(imgBackground, (1140, 80), (1200, 115), (255, 85, 1), -1)
                            #imgModeList[1] = imgModeList[1]


                if modeType != 3:

                    if 5 < counter < 20:
                        modeType = 2

                        imgBackground[526:526 + 111, 768:768 + 455] = imgModeList[modeType]

                    if counter <= 10 and studentInfo!=None:
                        cv2.putText(imgBackground, str(studentInfo['total_attendance']), (1152, 103),
                                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)

                        cv2.putText(imgModeList[1], str("ID : "+id), (260, 109),
                                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (21, 21, 21),2)

                        cv2.putText(imgModeList[1], str("Name : "+studentInfo['name']), (50, 297),
                                    cv2.FONT_HERSHEY_DUPLEX, 0.7, (21, 21, 21), 2)

                        #cv2.putText(imgBackground, str(id), (1013, 325),
                        #            cv2.FONT_HERSHEY_DUPLEX, 1, (21, 21, 21), 1)

                        #cv2.putText(imgBackground, str(studentInfo['name']), (1013, 260),
                        #            cv2.FONT_HERSHEY_DUPLEX, 1, (21, 21, 21), 1)

                        imgModeList[1][38:38 +185, 35:35 +185] = imgStudent

                    counter += 1

                    if counter >= 20:
                        cv2.putText(imgModeList[1], str("ID : " + id), (260, 109),
                                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)

                        cv2.putText(imgModeList[1], str("Name : " + studentInfo['name']), (50, 297),
                                    cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 2)
                        counter = 0
                        modeType = 0
                        studentInfo = []
                        imgStudent = []
                        #imgBackground[156:156 + 333, 768:768 + 455] = imgModeList[modeType]
                        #cv2.rectangle(imgBackground,(156,489),(768,1223),(0,0,0),-1)

    else:
        if(id!=-1):
            cv2.putText(imgModeList[1], str("ID : " + id), (260, 109),
                        cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)

            cv2.putText(imgModeList[1], str("Name : " + studentInfo['name']), (50, 297),
                        cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 2)
            cv2.rectangle(imgBackground, (1140, 80), (1200, 115), (255, 85, 1), -1)
            cv2.rectangle(imgBackground, (800, 180), (1200, 470), (255, 255, 255), -1)
        modeType = 0
        counter = 0

    cv2.imshow("Face Recognition", imgBackground)
    cv2.waitKey(1)