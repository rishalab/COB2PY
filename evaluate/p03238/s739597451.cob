       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       01  a1 PIC 9(08).
       01  a2 PIC 9(08).
       01  a3 PIC 9(08).
       01  r pic 9(08).
       01  g pic 9(08).
       01  r2 pic 9(08).
       01 disp pic X(21).
       PROCEDURE DIVISION.
        ACCEPT a1.
        if a1 = 1 then
         display "Hello World"
        else
         ACCEPT a2
         ACCEPT a3
         compute r = a3 + a2
         MOVE r to disp
         DISPLAY disp
        END-IF
        

       STOP RUN.
