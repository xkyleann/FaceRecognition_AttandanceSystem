import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

#Load Firebase credentials and initialize the app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-b9b88-default-rtdb.europe-west1.firebasedatabase.app/",
    'storageBucket': "facerecognition-b9b88.appspot.com"
})

#Set the folder path where the images are stored
folderPath = 'Images'

#Get the list of file paths in the folder
pathList = os.listdir(folderPath)
print(pathList)

#Initialize empty lists to store images and student IDs
imgList = []
studentIds = []

#Iterate over each file in the folder
for path in pathList:
    #Read the image file
    image = cv2.imread(os.path.join(folderPath, path))
    h, w, c = image.shape

    #Assert that the image has the correct size
    assert h == 185, "an image " + path + " should be 185px*185px"
    assert w == 185, "an image " + path + " should be 185px*185px"

    #Get the file extension
    x = os.path.splitext(path)[1]
    #Assert that the image is in .png format
    assert x == ".png", "an image " + path + " should be in .png format"

    #Append the image and student ID to the respective lists
    imgList.append(image)
    studentIds.append(os.path.splitext(path)[0])

    #Upload the image to Firebase storage
    fileName = os.path.join(folderPath, path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        #Convert the image to RGB format
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #Encode the face in the image
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
#Get the encodings for the known images
encodeListKnown = findEncodings(imgList)
#Combine the encodings with the corresponding student IDs
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

#Save the encodings and student IDs to a pickle file
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")