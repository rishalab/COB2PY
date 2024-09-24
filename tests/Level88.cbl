       IDENTIFICATION DIVISION.
       PROGRAM-ID. IntervalExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 my-number PIC 9(3) VALUE 0.

          88 is-low-range       VALUE IS 0 THRU 49 ,42 89 51 THRU 55.
          88 is-mid-range       VALUE 50 THRU 79.
          88 is-high-range      VALUE 80 THRU 100.

          88 is-multiple-of-5   VALUE 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 
          55, 60, 65, 70, 75, 80, 85, 90, 95, 100.

       PROCEDURE DIVISION.
       MAIN-PARA.
           DISPLAY "Enter a number (0-100): "
           ACCEPT my-number

           
           STOP RUN.