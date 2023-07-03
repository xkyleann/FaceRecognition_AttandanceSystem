#Add Admin SDK to connect with Firebase real-time database
#Create the database reference
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

#Initialize a credential from a JSON certificate keyfile(serviceAccountKey.py)
#Initialize and return a new App instance
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-b9b88-default-rtdb.europe-west1.firebasedatabase.app/",
    'storageBucket': "facerecognition-b9b88.appspot.com"
})

#Create reference path to the database
ref = db.reference('Students')

#Personal details in a dictionary format(json)
data = {
    "1":
        {
            "address":"someaddress"
        },
    "2":
        {
            "phone number":"000-000-000",
            "address":"someaddress"
        },
    "0000":
        {
            "name": "Elon Musk",
            "date_of_birth": "1971-06-28",
            "address": "USA",
            "phone_number": "999 000 000",
            "email": "someemail@gmail.com"
        },
    "412398":
        {
            "name": "Malgorzata Kuczera",
            "date_of_birth": "2002-04-18",
            "address": "Kraków, ul. Warszawska 24",
            "phone_number": "000 000 100",
            "email": "mkuczera@student.agh.edu.pl"
        },
    "414151":
        {
            "name": "Edibe Tutku Gayda",
            "date_of_birth": "2002-06-12",
            "address": "Krakow, Biprostal",
            "phone_number": "+48 001 000 000",
            "email": "gayda@student.agh.edu.pl"
        },
    "414147":
        {
            "name": "Eunseo Ko",
            "date_of_birth": "2001-01-13",
            "address": "aleja Adama Mickiewicza 30",
            "phone_number": "497 284 303",
            "email": "eunseo@student.agh.edu.pl"
        },
    "11":
        {
            "name": "test attendance",
            "date_of_birth": "2002-06-19",
        },
    "22":
        {
            "name":"name",
            "address": "some address",
            "date_of_birth": "2002-06-20",
        },
    "33":
        {
            "name":"somename1",
            "address":"someaddress1"
        }
}

#Count total number of people in the database (doesn't count duplicate ID)
total = len(data)
print("\nTotal number of people in the database : " + str(total)+"\n")


for key, value in data.items():
    check = True

    #Check if the name is present
    if "name" not in value and check==True:
        print("\n[Error!!!] The name field doesn't exists for ID " + key )
        check = False

    if check == True:
        #Get the information from firebase
        studentInfo = db.reference(f'Students/{key}').get()

        if studentInfo != None:
            #Check if total attendance and last attendance time is present and setting default values
            if('total_attendance' not in studentInfo):
                value["total_attendance"]=0
            else:
                total=studentInfo['total_attendance']
                value["total_attendance"]=total

            if ('last_attendance_time' not in studentInfo):
                value["last_attendance_time"] = "2000-01-01 01:00:00"
            else:
                time=studentInfo['last_attendance_time']
                value["last_attendance_time"]=time
        else:
            value["total_attendance"] = 0
            value["last_attendance_time"] = "2000-01-01 01:00:00"

        #Send data to database
        ref.child(key).set(value)


#Remove a person from database
data2 = ref.get()
if data2 is not None:
    ids = data2.keys()

    for id in ids:
        if(id not in data):
            ref.child(id).delete()

else:
    print("\nNo data in the specified location.")



#Remove Image from storage in Firebase
folderPath = "Images"
pathList = [os.path.join(folderPath, path) for path in os.listdir(folderPath)]

bucket = storage.bucket()
blobs = bucket.list_blobs()

removedFiles = set()

for blob in blobs:
    filePath = blob.name

    if filePath not in pathList:
        removedFiles.add(filePath)

for filePath in removedFiles:
    blob = bucket.blob(filePath)
    blob.delete()
    print("\nImage[" + filePath + "] was not found in the program. \n It has been deleted from firebase storage.")


#Get all pictures from directory
folderPath = 'Images'
pathList = os.listdir(folderPath)
ImagesNames=[]
for path in pathList:
    ImagesNames.append(os.path.splitext(path)[0])


#Check if person has picture
data3 = ref.get()
if data3 is not None:
    ids = data3.keys()
    print()
    for id in ids:
        if(id not in ImagesNames):
            print("\n[Warning!!!] Person with ID " + id + " does not have a picture and will not be detected by the program!")
    print()
    for picture in ImagesNames:
        if(picture not in data3):
            print("\n[Warning!!!] The picture " + picture + ".png does not have a corresponding person in database!")