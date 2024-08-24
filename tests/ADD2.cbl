IDENTIFICATION DIVISION.
       PROGRAM-ID. DetailedRedefinesExample2.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 RECORD-AREA2.
           05 EMP-NAME       PIC X(20).
           05 EMP-DATA.
               10 EMP-ID     PIC 9(5).
               10 EMP-SALARY PIC 9(5)V99.
               10 EMP-GENDER PIC X(1).
               10 EMP-ADDRESS OCCURS 10 TIMES.
                   15 EMP-AGE PIC 99.
                   15 EMP-CHILD PIC 9(05).
                10 EMP-ADDRESS2.
                   15 EMP-AGE PIC 99.
                   15 EMP-CHILD PIC 9(05).
       01 RECORD-AREA3.
           05 EMP-NAME       PIC X(20).
           05 EMP-DATA.
               10 EMP-ID     PIC 9(5).
               10 EMP-SALARY PIC 9(5)V99.
               10 EMP-GENDER PIC X(1).
               10 EMP-ADDRESS.
                   15 EMP-AGE PIC 99.
                   15 EMP-CHILD PIC 9(05).
                10 EMP-ADDRESS2.
                   15 EMP-AGE PIC 99.
                   15 EMP-CHILD PIC 9(05).
       
       PROCEDURE DIVISION.
           MOVE 'JOHN SMITH          ' TO EMP-NAME OF RECORD-AREA2
           MOVE '00001' TO EMP-ID OF RECORD-AREA3
           MOVE 0005000 TO EMP-SALARY  OF RECORD-AREA2
           MOVE 'M' TO EMP-GENDER  OF RECORD-AREA2
       
           DISPLAY "Employee Name: " EMP-NAME  OF RECORD-AREA2
           DISPLAY "Employee ID: " EMP-ID  OF RECORD-AREA2
           DISPLAY "Employee Salary: " EMP-SALARY  OF RECORD-AREA2
           DISPLAY "Employee Gender: " EMP-GENDER  OF RECORD-AREA2
           DISPLAY EMP-AGE OF EMP-ADDRESS2 OF RECORD-AREA2
       
           STOP RUN.