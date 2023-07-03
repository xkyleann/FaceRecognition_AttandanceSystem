# Face Recognition Attandence System  | AGH Software Studio Project | Instruction 
- This project aims to create a face recognition attendance system using Python and OpenCV. The system will detect and recognize faces in real-time and keep track of attendance.
-  [FaceRecognition.zip](https://drive.google.com/file/d/1H5VArBx0FVuSUGGIQmN7Hvn5l0OB6fka/view)

## Requirements
- To run this project, you need the following:
* Python 3.x
* OpenCV library
* Numpy library
* Face recognition library
* Webcam or camera for real-time face detection

## Installation
**1.** Install Python from the official website: [Python.org](https://www.python.org/)

**2.** Install OpenCV library by running the following command in your command prompt or terminal:
```pyhton
pip install opencv-python
```

**3.** Install Numpy library by running the following command:
```pyhton
pip install numpy
```

**4.** Install Face recognition library by running the following command:
```pyhton
pip install face_recognition
```


## Running the System
**1.** Download the project code from the Drive: [FaceRecognition.zip](https://drive.google.com/file/d/1H5VArBx0FVuSUGGIQmN7Hvn5l0OB6fka/view)

**2.** Extract the downloaded ZIP file to a folder on your computer.

**3.** Open a command prompt or terminal and navigate to the project folder.

**4.** Add links to the database with [serviceaccountkey](https://github.com/Etutku/SS2023_Ko_Kuczera_Gayda_SpreadSheet/blob/main/FaceRecognitionAttandanceSysytem/serviceAccountKey.json), and add all images to run [Encode Generator](https://github.com/Etutku/SS2023_Ko_Kuczera_Gayda_SpreadSheet/blob/main/FaceRecognitionAttandanceSysytem/EncodeGenerator.py). 
 - The links to the database should be added to: [AddToDatabase](https://github.com/Etutku/SS2023_Ko_Kuczera_Gayda_SpreadSheet/blob/main/FaceRecognitionAttandanceSysytem/AddDataToDatabase.py), [Encode Generator](https://github.com/Etutku/SS2023_Ko_Kuczera_Gayda_SpreadSheet/blob/main/FaceRecognitionAttandanceSysytem/EncodeGenerator.py) and [main.py](https://github.com/Etutku/SS2023_Ko_Kuczera_Gayda_SpreadSheet/blob/main/FaceRecognitionAttandanceSysytem/main.py)

**5.** Add people with [AddToDatabase](https://github.com/Etutku/SS2023_Ko_Kuczera_Gayda_SpreadSheet/blob/main/FaceRecognitionAttandanceSysytem/AddDataToDatabase.py).

**6.** Run the following command to start the attendance system [main.py](https://github.com/Etutku/SS2023_Ko_Kuczera_Gayda_SpreadSheet/blob/main/FaceRecognitionAttandanceSysytem/main.py):
```pyhton
python main.py
```
**7.** The webcam or camera will be activated, and you'll see a live video feed with face detection and recognition.

**8.** The system will automatically detect and recognize faces. It will display the recognized names on the screen and mark attendance in a CSV file.

**9.** Press 'Q' on your keyboard to stop the attendance system.

## Further Steps  ( with using another database)
**Step 1 Set up Firebase**
* Create a Firebase account at [firebase.google.com] (firebase.google.com) if you don't have one already.
* Because of this is completed project, existed firebase would be using.
* If new firebase needed, set up a new Firebase project for your face recognition attendance system.
* Enable Firebase Authentication and create an authentication method that suits your requirements (e.g., email/password, Google, etc.)
* Enable Firebase Realtime Database and Firebase Storage.

**Step 2 Set up Development Environment**
* Install the necessary software and libraries (mentioned in  the Installation)
* Set up a virtual environment for your project to manage dependencies.

**Step 3 Collect and preprocess face images**
* Use a webcam or camera to capture face images of individuals whose attendance you want to track.
* Save  images in a directory on your local system.

**Step 4 Adding Firebase to the System**
* Load the pre-trained face recognition model. [FaceRecognition.zip](https://drive.google.com/file/d/1H5VArBx0FVuSUGGIQmN7Hvn5l0OB6fka/view)
* Initialize the Firebase SDK.
*  Implement functions to detect and recognize faces in real-time.
* Connect to the Firebase Realtime Database and create the necessary data structure to store attendance information.
* Store the recognized face along with the current timestamp in the database when a face is detected.

**Step 5 Deploy and Test the System**
* Deploy the system desired platform  (PyCharm)
* Verify that the attendance data is being stored correctly in the Firebase Realtime Database.
* Ensure that the user interface displays the attendance information accurately.

**Step 6 Firebase Storage** 
* If you want to store the captured face images, set up Firebase Storage.
* Implement functionality to upload the captured images to Firebase Storage.
* Store the image URLs or references in the Firebase Realtime Database along with the attendance data.

## Troubleshooting
- If you encounter any errors during installation or running the system, make sure you have installed all the required libraries correctly.
- Check if your webcam or camera is properly connected and working.
- Make sure the faces you want to recognize are well-lit and clear in the camera feed.
- Ensure that the names and encodings in the attendance_system.py file are accurate and match the individuals you want to recognize.

## Conclusion 
With this face recognition attendance system, you can easily track attendance by leveraging the power of computer vision. Remember to comply with privacy and data protection regulations when using such systems.

Enjoy using the face recognition attendance system!
