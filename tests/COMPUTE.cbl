       IDENTIFICATION DIVISION.
       PROGRAM-ID. ComputeExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SUM1         PIC 9(4) VALUE 100.
       01 COUNT1      PIC 9(2) VALUE 5.
       01  TOTAL       PIC 9(4).
       01  AVERAGE     PIC 9(4)V9(2). 

       PROCEDURE DIVISION.
       BEGIN.
           COMPUTE TOTAL ROUNDED AVERAGE = SUM1 / COUNT1
           END-COMPUTE.

           DISPLAY "Total: " TOTAL.
           DISPLAY "Average: " AVERAGE.

           STOP RUN.
