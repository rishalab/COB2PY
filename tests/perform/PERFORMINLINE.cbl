       IDENTIFICATION DIVISION.
       PROGRAM-ID. InlinePerformExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A PIC 9(02) VALUE 0.

       PROCEDURE DIVISION.
           PERFORM
               DISPLAY 'This is an inline PERFORM statement'
               MOVE 5 TO A
               DISPLAY 'Value of A after MOVE: ' A
               ADD 1 TO A
               DISPLAY 'Value of A after ADD: ' A
           END-PERFORM.

           STOP RUN.
