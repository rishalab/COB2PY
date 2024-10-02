       IDENTIFICATION DIVISION.
       PROGRAM-ID. DecimalSignExample.
       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 num-decimal. 
       02 ws-decimal1       PIC S9(5)V99 SIGN IS LEADING SEPARATE CHARACTER
          VALUE -1234.56.
          88 state56 VALUE +5.
       02 ws-decimal2       PIC S9(5)V99 VALUE -1234.56.
       02 ws-decimal3       PIC S9(5)V99 SIGN IS TRAILING VALUE -1234.56.
       02 ws-decimal4       PIC S9(5)V99 SIGN IS LEADING VALUE -1234.56.

       PROCEDURE DIVISION.

           DISPLAY "Leading Separate Character: " ws-decimal1.
           DISPLAY "No Sign Specified: " ws-decimal2.
           DISPLAY "Trailing Embedded Sign: " ws-decimal3.
           DISPLAY "Leading Embedded Sign: " ws-decimal4.
           DISPLAY "NUM group: " num-decimal.

           STOP RUN.
