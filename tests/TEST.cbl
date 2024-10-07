       IDENTIFICATION DIVISION.
       PROGRAM-ID. ProcedureRangePerformExample.
       PROCEDURE DIVISION.
           PERFORM PROCEDURE-1 THRU PROCEDURE-3.
           PERFORM PROCEDURE-2.
           DISPLAY 'udiuviudflob'
           STOP RUN.
           EXIT.
       PROCEDURE-1.
           DISPLAY 'This is PROCEDURE-1'.
           EXIT.
       PROCEDURE-2.
           DISPLAY 'This is PROCEDURE-2'.
           EXIT.
       PROCEDURE-3.
           DISPLAY 'This is PROCEDURE-3'.
           EXIT.