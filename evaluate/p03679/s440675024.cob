IDENTIFICATION                   DIVISION.
PROGRAM-ID.                      ABC_065_A.
ENVIRONMENT                      DIVISION.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 INP    PIC X(32).
    01 X      PIC 9(10).
    01 A      PIC 9(10).
    01 B      PIC S9(10).
PROCEDURE                        DIVISION.
MAIN.
    ACCEPT INP.

    UNSTRING INP
    DELIMITED BY SPACE
    INTO X A B.

    SUBTRACT A FROM B.

    IF B <= 0 THEN
        DISPLAY "delicious"
    ELSE
        IF B <= X THEN
            DISPLAY "safe"
        ELSE
            DISPLAY "dangerous"
        END-IF
    END-IF.

    STOP RUN.
