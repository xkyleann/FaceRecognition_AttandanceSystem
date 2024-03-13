# Acceptance Criteria [Updated]
--------------------------------------------------------------------------------------------------------------------------------------------------
1. **As a User** I want database that will automatically upload data to the face recognition system up-to-date so that I don't need to manually input them again.
      - **Priority** --> 1
      - [X] User must have an account for Firebase website.
      - [X] User must create a real-time database on the Firebase website.
      - [X] User must download a private key file from the website and add it to the program directory.
      - [X] User must add Admin SDK configuration provided by Firebase to the python file that is connected to the real-time database.
--------------------------------------------------------------------------------------------------------------------------------------------------

2.  **As a User** I want to be able to add people's details and make modification to my database so that the database would include people and data necessary for my purpose of using this system. 
      - **Priority** --> 1
      - [X] Personal data must be in JSON format where key is the ID number and value is another key-value pair where kes are the field names (ex) name, DOB, etc) and values are personal details of each person.
      - [X]  ID number is a compulsory key identifying each person in the database.
      - [X]  User can choose types of information (field) in the database but name is compulsory for operation of the system.
      - [X] If the name is not present the program will show an error and won't add that person
      - [X] User cannot have more than one person in the database with the same ID number. In such case, the program will count them as one person and the last occurence will be stored.
      - [X] User cannot have more than one person in the database with the same ID number. In such case, the program will count them as one person and the last occurence will be stored.
--------------------------------------------------------------------------------------------------------------------------------------------------

3.  **As a User** I want to be able to add pictures of people in my database so that they would be recognized by the software.
      - **Priority** --> 1
      - [x] All pictures must be 185px*185px.
      - [X] Picture must be identical to the person.
      - [X] User must add pictures into the separate directory in the program.
      - [X] The name of the picture should be the same as person's ID number.
      - [X] If the picture is in the wrong fomat then the program will show an error.
      - [X] The picture should be in .png format.
--------------------------------------------------------------------------------------------------------------------------------------------------
4.  **As a User** I want to be able to change pictures of people in my database so that it would be up-to-date in case of any changes in appearance.
      - **Priority** --> 2
      - [X] The picture has to be the same size as the previous one  (185px*185px).
      - [x] The new picture should have the same name as the old one which is person's ID number.
      - [X] If the picture is in the wrong fomat then the program will show an error.
--------------------------------------------------------------------------------------------------------------------------------------------------
5.  **As a User** I want to be able to remove a person from my database in case someone is not part of the organization, school, or etc any more so that the system wouldn't recognize them anymore.
      - **Priority** --> 2
      - [X] All the information about the person must be removed from the database.
      - [X] Picture must be removed from the directory as well.
      - [X] The system shouldn't recognize removed person anymore.
--------------------------------------------------------------------------------------------------------------------------------------------------
6.  **As a User** I want to be able to use webcam real-time so that the system will compare images and people's face to verify the identity for attendance.
      -**Priority** --> 1
      - [X] The real-time webcam will be shown on the left side of the system.
      - [X] The system will compare people's face with pictures from database.
      - [X] Pictures from database are linked with people's ID number.
--------------------------------------------------------------------------------------------------------------------------------------------------
7. **As a User** I want to be able to see personal details of on the screen when someone takes the attendance so that I get to know his/her details without checking their ID card.
      - **Priority** --> 3
      - [x] ID, name, profile picture and total attendance should be displayed on the screen.
      - [x] On the right side of the system, above details must be displayed once the system recognizes the face.
      - [x] These details should only be displayed if the attendance is taken after the time limit set by the system.
--------------------------------------------------------------------------------------------------------------------------------------------------
8. **As a User** I want to be able to view total attendance of a person till the current time on the screen when someone takes the attendance so that I don't have to access my database to check everytime.
      - **Priority** --> 2
      - [x] Personal details must have a variable that stores total attendance days.
      - [x] The number of total attendance is updated each time there is a new attendance of that person.
      - [x] The number includes the current attendance.
--------------------------------------------------------------------------------------------------------------------------------------------------
9. **As a User** I want to be able to set the time limit after which one person can be marked again so that it can fit my purpose for using this software.
      - **Priority** --> 2
      - [x] Personal details in python file must have a variable that stores last attendance time in a format of YYYY-MM-DD hh:mm:ss
      - [x] Before the user changes the time limit it is set to one minute as a default.
      - [x]  The time limit can be changed by the user from 15 seconds to infinity. If User tries to set the time limit to less than 15 second the program will change it to 15 seconds.

--------------------------------------------------------------------------------------------------------------------------------------------------
10. **As a User** I want the system to show attendance status of the person taking the attendance so that he/she knows whether the attendance has been taken or not.
      - **Priority** --> 2
      - [x] There should be 4 modes: 'Active', 'Marked', displayed information about a person recently marked and 'Already marked'. 
      - [x] 'Active' mode should appear when there is no face detected in the camera.
      - [x] 'Marked' mode should appear when someone was detected and the attendance was added.
      - [x]  Information about the person should appear after marked mode and be displayed for a few seconds.
      - [x]  Information about the peson include: ID, name, profile picture and total attendance.

--------------------------------------------------------------------------------------------------------------------------------------------------
11. **As a User** I want a notification to appear if someone has already took attendance within the time limit so that there is no duplicate attendance saved in the database.
      - **Priority** --> 3
      - [x] System will check the current time and compare to the last attended time of the person when taking an attendance.
      - [x] If the time from the last presence is less than the time limit the notification should appear.
      - [x] The system should display "Already marked".
      - [x] The system shouldn't count this as a new attendance.
-------------------------------------------------------------------------------------------------------------------------------------------------   
12. **As a User** I want to have the attendance system that automatically update my attendance database when someone checks the attendance so that I don't need to manually fill in attendance sheets which will save time and reduce the risk of errors. 
      - **Priority** --> 1
      - [x]  The system updates the total number of attendance when the person is present.
      - [x]  If the time from the last presence is less than the time limit the total attendance won't be changed.
--------------------------------------------------------------------------------------------------------------------------------------------------
13. **As a User** I want to be able to view data about specific person in my database so that I can find the information I'm currently looking for.
      - **Priority** --> 1
      - [x] All of the information added previously by the user can be viewed on Firebase.
      - [x] The information when was the last time someone was present and the total attendence can also be viewed
--------------------------------------------------------------------------------------------------------------------------------------------------
14. **As a User** I want to be able to see when was the last time someone was present so that I don't have to check it manually.
      - **Priority** --> 2
      - [x] The information is stored in a format "YYYY-MM-DD hh:mm:ss".
      - [x] The date is updated each time a that person is present.
      - [x] The information isn't updated if the time between the previous one and the current attendance is less than the time limit.
--------------------------------------------------------------------------------------------------------------------------------------------------
15. **As a User** I want to be able to see how many people are in my database so that I don't have to count them manually.
      - **Priority** --> 3
      - [x] The number is updated each time a new person is added to the database.
      - [x] The number is updated each time a person is removed from the database.
      - [x]  If the duplicate ID exists, the system will only count one of them. 

--------------------------------------------------------------------------------------------------------------------------------------------------
16. **As a User** I want to see what the current time is so that I know when my attendence is taken.
      - **Priority** --> 3
      - [x]  The clock should show what is the current date and time.
  
