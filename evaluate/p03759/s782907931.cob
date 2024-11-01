IDENTIFICATION                   DIVISION.
PROGRAM-ID.                      ABC_058_A.
ENVIRONMENT                      DIVISION.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 INP    PIC X(11).
    01 a      PIC S9(3).
    01 b      PIC S9(3).
    01 c      PIC S9(3).
PROCEDURE                        DIVISION.
MAIN.
    ACCEPT INP.

    UNSTRING INP
    DELIMITED BY SPACE
    INTO a b c.

    IF b - a = c - b THEN
        DISPLAY "YES"
    ELSE
        DISPLAY "NO"
    END-IF.

    STOP RUN.
