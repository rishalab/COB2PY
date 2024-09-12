       IDENTIFICATION DIVISION.
       PROGRAM-ID. Access2DArray.
       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 EMPLOYEE-TABLE.
           05 EMPLOYEE-RECORD OCCURS 5 TIMES.
              10 EMP-NAME   PIC X(20).
              10 EMP-DETAILS.
                 15 EMP-ADDRESS OCCURS 3 TIMES.
                    20 STREET-NAME    PIC X(30).
                    20 CITY           PIC X(20).
                    20 ZIP-CODE       PIC 9(5).

       01 EMP-INDEX      PIC 9 VALUE 1.
       01 ADDR-INDEX     PIC 9 VALUE 2.

       PROCEDURE DIVISION.
       BEGIN.
           MOVE "John Doe" TO EMP-NAME(EMP-INDEX)
           MOVE "123 Elm Street" TO STREET-NAME(EMP-INDEX, ADDR-INDEX)
           MOVE "New York" TO CITY(EMP-INDEX, ADDR-INDEX)
           MOVE 10001 TO ZIP-CODE(EMP-INDEX, ADDR-INDEX)

           DISPLAY "Employee Name: " EMP-NAME(EMP-INDEX)
           DISPLAY "Street: " STREET-NAME(EMP-INDEX, ADDR-INDEX)
           DISPLAY "City: " CITY(EMP-INDEX, ADDR-INDEX)
           DISPLAY "Zip Code: " ZIP-CODE(EMP-INDEX, ADDR-INDEX).

           STOP RUN.
