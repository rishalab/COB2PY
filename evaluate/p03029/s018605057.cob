       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       01  a1 PIC S9(08).
       01  a2 PIC S9(08).
       01  a3 PIC S9(08).
       01  r1 PIC S9(08).
       01  r2 PIC S9(08).
       01  r3 PIC S9(08).
       01  r pic S9(08).
       01  g pic S9(08).
       01 disp pic X(20).
       PROCEDURE DIVISION.
        ACCEPT indata.
        
        UNSTRING indata DELIMITED BY SPACE INTO a1 a2.
        COMPUTE a2 = a2 + (a1 * 3)
        divide a2 by 2 giving g

        MOVE g to disp
        DISPLAY disp


       STOP RUN.
