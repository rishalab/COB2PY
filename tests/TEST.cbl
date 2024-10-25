       IDENTIFICATION DIVISION.
       PROGRAM-ID. GoToDependingExample.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       1 CHOICE PIC 9(4) VALUE 10.
       PROCEDURE DIVISION.

       MAIN-PROCEDURE.
           MOVE 2 TO CHOICE.
           GO TO INIT-PROC MAIN-PROC END-PROC DEPENDING ON CHOICE.

       INIT-PROC.
           DISPLAY "In INIT-PROC.".

       MAIN-PROC.
           DISPLAY "In MAIN-PROC.".
           GO TO INIT-PROC.
           STOP RUN.

       END-PROC.
           DISPLAY "In END-PROC."
           STOP RUN.
