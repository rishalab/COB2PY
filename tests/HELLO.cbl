       IDENTIFICATION DIVISION.
       PROGRAM-ID. DisplayTest.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NAME PIC X(20) VALUE 'John Doe'.
       01 WS-AGE  PIC 99 VALUE 30.
       01 WS-ADDR PIC X(30) VALUE '123 Main St, Anytown'.

       PROCEDURE DIVISION.
       DISPLAY "Hello, World!".
       DISPLAY "Name:" WS-NAME.
       DISPLAY "Age:" WS-AGE.
       DISPLAY "Address:" WS-ADDR.
       DISPLAY "Combined Info:" WS-NAME WS-AGE WS-ADDR.
       DISPLAY "Name and Age:", WS-NAME "Age:" WS-AGE.
       DISPLAY "Result: " "Success!".
       DISPLAY "Result at Line:" AT LINE 10 "This is line 10".
       DISPLAY "Result with no newline" WITH NO ADVANCING "Next sentence follows".
       DISPLAY "Result upon Console:" UPON CONSOLE "This is on console".
       STOP RUN.
