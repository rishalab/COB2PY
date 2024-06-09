       IDENTIFICATION DIVISION.
       PROGRAM-ID. DIVIDE-EXAMPLE.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 DIVIDEND PIC 9(3) VALUE 100.
       77 DIVISOR PIC 9(2) VALUE 5.
       77 RESULT PIC 9(3) VALUE 50.
       77 RESUL PIC 9(3) VALUE 200.
       77 RESU PIC 9(3) VALUE 10.
       77 RE PIC 9(3) VALUE 25.
       77 REMAINDE PIC 9(2).
       
       PROCEDURE DIVISION.
           DIVIDE DIVIDEND into DIVISOR
           GIVING RESULT
           REMAINDER REMAINDE.
           
           DISPLAY "Result of division: " RESULT
           DISPLAY "Remainder: " REMAINDE.

           DIVIDE DIVIDEND into DIVISOR
           GIVING RESULT.
           DISPLAY "Result of division: " RESULT.

           DIVIDE DIVIDEND BY DIVISOR
           GIVING RESULT
           REMAINDER REMAINDE.
           
           DISPLAY "Result of division: " RESULT " " RE.
           DISPLAY "Remainder: " REMAINDE.

           DIVIDE DIVIDEND BY DIVISOR
           GIVING RESULT.
           DISPLAY "Result of division: " RESULT.


           divide DIVIDEND into resu RESUL.
           display resu " " RESUL " " DIVIDEND.

           STOP RUN.
