       IDENTIFICATION DIVISION.
       PROGRAM-ID. BILLING.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77  NAME     PIC A(30).
       77  UNITS    PIC 9(4).
       77  BILL     PIC 9(6).

       PROCEDURE DIVISION.
           DISPLAY "Customer Name: "
           ACCEPT NAME

           DISPLAY "Units Consumed: "
           ACCEPT UNITS

           IF UNITS <= 100
               COMPUTE BILL = UNITS * 5
           ELSE IF UNITS <= 200
               COMPUTE BILL = 100 * 5 + (UNITS - 100) * 7
           ELSE
               COMPUTE BILL = 100 * 5 + 100 * 7 + (UNITS - 200) * 10
           END-IF.

           DISPLAY "-----------------------------"
           DISPLAY "Customer: " NAME
           DISPLAY "Units:    " UNITS
           DISPLAY "Bill:     Rs" BILL
           DISPLAY "-----------------------------"
           STOP RUN.