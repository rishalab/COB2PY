       IDENTIFICATION DIVISION.
       PROGRAM-ID. ATCODER.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  indata PIC X(100).
       01  k PIC 9(08).
       01  x PIC 9(08).
       01  r PIC 9(08).
       PROCEDURE DIVISION.
        ACCEPT indata

        UNSTRING indata DELIMITED BY SPACE INTO k x.

        MULTIPLY 500 BY k GIVING r
        IF r >= x THEN
          DISPLAY "Yes"
        ELSE
          DISPLAY "No"
        END-IF

       STOP RUN.
