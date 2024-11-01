IDENTIFICATION                   DIVISION.
PROGRAM-ID.                      ABC_056_A.
ENVIRONMENT                      DIVISION.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 INP    PIC X(3).
    01 a      PIC X(1).
    01 b      PIC X(1).
PROCEDURE                        DIVISION.
MAIN.
    ACCEPT INP.

    UNSTRING INP
    DELIMITED BY SPACE
    INTO a b.

    IF a = 'H' THEN
        DISPLAY b
    ELSE
        IF b = 'H' THEN
            DISPLAY 'D'
        ELSE
            DISPLAY 'H'
        END-IF
    END-IF.

    STOP RUN.
