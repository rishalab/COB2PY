       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       01  n PIC 9(08).
       01  m PIC 9(08).
       PROCEDURE DIVISION.
        ACCEPT n
        ACCEPT m

         IF n = 1 THEN
           IF m = 2 THEN
                  DISPLAY "3"
           END-IF
           IF m = 3 THEN
                  DISPLAY "2"
           END-IF
         END-IF

         IF n = 2 THEN
           IF m = 1 THEN
                  DISPLAY "3"
           END-IF
           IF m = 3 THEN
                  DISPLAY "1"
           END-IF
         END-IF

         IF n = 3 THEN
           IF m = 2 THEN
                  DISPLAY "1"
           END-IF
           IF m = 1 THEN
                  DISPLAY "2"
           END-IF
         END-IF


       STOP RUN.
