       IDENTIFICATION DIVISION.
       PROGRAM-ID. PerformUntilExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A PIC 9(02) VALUE 1.

       PROCEDURE DIVISION.
           PERFORM UNTIL A > 10
               DISPLAY 'Value of A: ' A
               MULTIPLY 2 BY A
           END-PERFORM.
           DISPLAY 'HI'
           STOP RUN.
