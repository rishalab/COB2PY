       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       PROCEDURE DIVISION.
        ACCEPT indata.
        
         IF indata = "Sunny" THEN
           DISPLAY "Cloudy"
         END-IF
         IF indata = "Cloudy" THEN
           DISPLAY "Rainy"
         END-IF
         IF indata = "Rainy" THEN
           DISPLAY "Sunny"
         END-IF


       STOP RUN.
