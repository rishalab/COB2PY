       IDENTIFICATION DIVISION.
       PROGRAM-ID. PerformTimesExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 COUNTER PIC 9(02) VALUE 0.

       PROCEDURE DIVISION.
           PERFORM 10 TIMES
               DISPLAY 'This    will be displayed 10 times'
               ADD 1 TO COUNTER
               DISPLAY 'Counter: ' COUNTER
           END-PERFORM.
            DISPLAY 'Counter: ' COUNTER
           STOP RUN.
