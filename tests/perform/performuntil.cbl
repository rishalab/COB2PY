       IDENTIFICATION DIVISION.
       PROGRAM-ID. PerformUntilExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A PIC 9(02) VALUE 0.

       PROCEDURE DIVISION.
           PERFORM UNTIL A > 10
               DISPLAY 'Value of A: ' A
               ADD 1 TO A
           END-PERFORM.
           DISPLAY 'HI'
           STOP RUN.
