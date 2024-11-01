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
       01 disp pic Z(20)9.
       PROCEDURE DIVISION.
        ACCEPT indata.
        
        UNSTRING indata DELIMITED BY SPACE INTO a1.
        if a1 = 3 or a1 = 5 or a1 = 7 then 
         DISPLAY "YES"
        else
         DISPLAY "NO"
        end-if

       STOP RUN.
