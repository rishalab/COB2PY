       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       PROCEDURE DIVISION.
        ACCEPT indata.
        
         IF indata = "SUN" THEN
           DISPLAY "7"
         END-IF
         IF indata = "MON" THEN
           DISPLAY "6"
         END-IF
         IF indata = "TUE" THEN
           DISPLAY "5"
         END-IF
         IF indata = "WED" THEN
           DISPLAY "4"
         END-IF
         IF indata = "THU" THEN
           DISPLAY "3"
         END-IF
         IF indata = "FRI" THEN
           DISPLAY "2"
         END-IF
         IF indata = "SAT" THEN
           DISPLAY "1"
         END-IF


       STOP RUN.
