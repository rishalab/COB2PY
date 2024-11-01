       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       01  a1 PIC 9(08).
       01  a2 PIC 9(08).
       01  r pic 9(08).
       01 disp pic X(10).
       PROCEDURE DIVISION.
        ACCEPT indata.
        
        UNSTRING indata DELIMITED BY SPACE INTO a1 a2.

        COMPUTE r = a1 * a2

        IF a1 < 10 AND a2 < 10 THEN
          MOVE r to disp
          DISPLAY disp
        ELSE
          DISPLAY "-1"
        END-IF


       STOP RUN.
