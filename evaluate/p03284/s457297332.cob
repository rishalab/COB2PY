PROGRAM-ID.                      ABC_105_A.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 INP     PIC X(7).
    01 N       PIC 9(3).
    01 K       PIC 9(3).
    01 ans     PIC X(3).

    01 d       PIC 9(3).
    01 r       PIC 9(3).

PROCEDURE                        DIVISION.
    ACCEPT INP.

    UNSTRING INP
    DELIMITED BY SPACE
    INTO N K.

    DIVIDE K INTO N GIVING d REMAINDER r.

    IF ZERO = r
        DISPLAY ZERO
    ELSE
        DISPLAY 1
    END-IF.

    STOP RUN.
