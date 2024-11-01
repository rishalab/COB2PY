IDENTIFICATION                   DIVISION.
PROGRAM-ID.                      ABC_071_A.
ENVIRONMENT                      DIVISION.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 INP    PIC X(14).
    01 x      PIC 9(4).
    01 a      PIC 9(4).
    01 b      PIC 9(4).

PROCEDURE                        DIVISION.
MAIN.
    ACCEPT INP.

    UNSTRING INP
    DELIMITED BY SPACE
    INTO x a b.

    SUBTRACT x FROM a.
    SUBTRACT x FROM b.

    IF a < b THEN
        DISPLAY 'A'
    ELSE
        DISPLAY 'B'
    END-IF.

    STOP RUN.
