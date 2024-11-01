       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       01  a1 PIC 9(08).
       01  a2 PIC 9(08).
       01  a3 PIC 9(08).
       01  r pic 9(08).
       PROCEDURE DIVISION.
        ACCEPT indata.
        
        UNSTRING indata DELIMITED BY SPACE INTO a1 a2 a3.

        COMPUTE r = a1 + a2 + a3

         IF r >= 22 THEN
           DISPLAY "bust"
         ELSE
           DISPLAY "win"
         END-IF


       STOP RUN.
