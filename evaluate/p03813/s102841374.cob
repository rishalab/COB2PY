identification division.
PROGRAM-ID.                      ABC_053_A.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 x       PIC 9(4).

PROCEDURE                        DIVISION.
    ACCEPT x.

    IF x < 1200 THEN
        DISPLAY "ABC"
    ELSE
        DISPLAY "ARC"
    END-IF.

    STOP RUN.
