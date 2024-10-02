       IDENTIFICATION DIVISION.
       PROGRAM-ID. SignExample.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       
       01 num. 
       02 ws-number1       PIC S9(5) SIGN IS LEADING SEPARATE CHARACTER
         VALUE -12345 .
          88 state56 VALUE +5.
       02 ws-number2       PIC S9(5) VALUE -12345 .
       02 ws-number3       PIC S9(5) SIGN IS TRAILING VALUE -12345 .
       02 ws-number4       PIC S9(5) SIGN IS LEADING VALUE -12345 .

       PROCEDURE DIVISION.

           DISPLAY "Trailing Separate Character: " ws-number1.
           DISPLAY "No Sign Specified: " ws-number2.
           DISPLAY "Trailing Embedded Sign: " ws-number3.
           DISPLAY "Leading Embedded Sign: " ws-number4.
           DISPLAY "NUM group: " num.

           STOP RUN.
