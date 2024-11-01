IDENTIFICATION                   DIVISION.
PROGRAM-ID.                      ABC_078_A.
ENVIRONMENT                      DIVISION.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 INP    PIC X(3).
    01 X      PIC X(1).
    01 Y      PIC X(1).

PROCEDURE                        DIVISION.
MAIN.
    ACCEPT INP.

    UNSTRING INP
    DELIMITED BY SPACE
    INTO X Y.

    IF X < Y THEN
        DISPLAY '<'
    ELSE
        IF X = Y THEN
            DISPLAY '='
        ELSE
            DISPLAY '>'
        END-IF
    END-IF.

    STOP RUN.
