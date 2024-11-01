       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       01  indata2 PIC X(100).
       01  a1 PIC 9(08).
       01  a2 PIC 9(08).
       01  r pic S9(08).
       01 disp pic Z(10)9.
       PROCEDURE DIVISION.
        ACCEPT indata.
        ACCEPT indata2.
        
        UNSTRING indata DELIMITED BY SPACE INTO a1.

         IF a1 >= 3200 THEN
           DISPLAY indata2
         ELSE
           DISPLAY "red"
         END-IF


       STOP RUN.
