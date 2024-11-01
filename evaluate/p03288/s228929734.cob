IDENTIFICATION                   DIVISION.
PROGRAM-ID.                      ABC_104_A.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 R       PIC 9(4).

PROCEDURE                        DIVISION.
    ACCEPT R.

    IF R < 1200 THEN
        DISPLAY "ABC"
    ELSE
        IF R < 2800 THEN
            DISPLAY "ARC"
        ELSE
            DISPLAY "AGC"
        END-IF
    END-IF.

    STOP RUN.
