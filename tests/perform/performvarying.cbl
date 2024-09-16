       IDENTIFICATION DIVISION.
       PROGRAM-ID. PerformVaryingExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 I PIC 9(02) VALUE 0.

       PROCEDURE DIVISION.
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
               DISPLAY 'Value of I: ' I
           END-PERFORM.
           DISPLAY 'HI'
           STOP RUN.
