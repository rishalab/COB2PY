       IDENTIFICATION DIVISION.
       PROGRAM-ID. ThreeDArrayDemo.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  EMPLOYEE-TABLE.
           05  EMPLOYEE-RECORD OCCURS 2 TIMES.
               10  ADDRESS-RECORD OCCURS 3 TIMES.
                    15  ZIP-CODE OCCURS 3 TIMES PIC 9(5).
        01 GROUP-2.
            05 IDX1      PIC 9 VALUE 1.
        PROCEDURE DIVISION.
            DISPLAY '3D Array Example:'.

            MOVE 12345 TO ZIP-CODE(1, 1, 1).
            MOVE 67890 TO ZIP-CODE(1, 1, 2).

            MOVE 54321 TO ZIP-CODE(2, 2, 1).
            MOVE 98765 TO ZIP-CODE(2, 2, 2).
            MULTIPLY IDX1 OF GROUP-2 BY IDX1.

            MULTIPLY ZIP-CODE(1, 1, IDX1 OF GROUP-2) BY ZIP-CODE(2, 2, 1).
           DISPLAY 'Employee 1, Address 1, Zip Code 1: ' ZIP-CODE(1, 1, 3).
           DISPLAY 'Employee 1, Address 1, Zip Code 2: ' ZIP-CODE(1, 1, 2).

           DISPLAY 'Employee 2, Address 2, Zip Code 1: ' ZIP-CODE(2, 2, 1).
           DISPLAY 'Employee 2, Address 2, Zip Code 2: ' ZIP-CODE(2, 2, 2).

           STOP RUN.