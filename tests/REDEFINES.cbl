       IDENTIFICATION DIVISION.
       PROGRAM-ID. RedefinesExample.
       DATA DIVISION.
       WORKING-STORAGE SECTION.

     
       01 EMPLOYEE-RECORD.
          05 EMPLOYEE-NAME                PIC X(30).
          05 EMPLOYEE-NUMBER              PIC X(10).
          05 SALARY                       PIC 9(8)V99.
          05 DATE-HIRED.
             10 YEAR-HIRED                PIC 9(4).
             10 MONTH-HIRED               PIC 9(2).
             10 DAY-HIRED                 PIC 9(2).

       
       01 EMPLOYEE-NUMBER-DETAILS REDEFINES EMPLOYEE-RECORD.
          05 EMPLOYEE-NAME-DUMMY          PIC X(30). 
          05 EMP-NUMBER-FIELDS.
             10 DEPARTMENT-CODE           PIC X(4).
             10 EMPLOYEE-ID               PIC X(6).
          05 SALARY-DUMMY                 PIC 9(8)V99. 
          05 DATE-HIRED-DUMMY.
             10 YEAR-DUMMY                PIC 9(4).
             10 MONTH-DUMMY               PIC 9(2).
             10 DAY-DUMMY                 PIC 9(2).

       
       01 RAW-EMPLOYEE-DATA REDEFINES EMPLOYEE-RECORD PIC X(50).

       PROCEDURE DIVISION.
       BEGIN.
           
           MOVE "John Doe                 " TO EMPLOYEE-NAME.
           MOVE "D001123456" TO EMPLOYEE-NUMBER.
           MOVE 75000.25 TO SALARY.
           MOVE 2023 TO YEAR-HIRED.
           MOVE 09 TO MONTH-HIRED.
           MOVE 15 TO DAY-HIRED.

           
           DISPLAY "Employee Name: " EMPLOYEE-NAME.
           DISPLAY "Employee Number: " EMPLOYEE-NUMBER.
           DISPLAY "Department Code: " DEPARTMENT-CODE.
           DISPLAY "Employee ID: " EMPLOYEE-ID.
           DISPLAY "Year Hired: " YEAR-HIRED.
           DISPLAY "Salary: " SALARY.

           
           DISPLAY "Raw Employee Data: " RAW-EMPLOYEE-DATA.

           STOP RUN.
