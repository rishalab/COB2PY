       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  INDATA PIC X(100).
       01  VARN PIC 9(03).
       01  VARM PIC 9(03).
       PROCEDURE DIVISION.
           ACCEPT INDATA

           UNSTRING INDATA
           DELIMITED BY SPACE
           INTO VARN VARM.
         IF VARN = VARM THEN
                 DISPLAY "Yes"
         ELSE
                 DISPLAY "No"
         END-IF

       STOP RUN.
