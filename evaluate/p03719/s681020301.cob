IDENTIFICATION                   DIVISION.
PROGRAM-ID.                      ABC_061_A.
ENVIRONMENT                      DIVISION.
DATA                             DIVISION.
WORKING-STORAGE                  SECTION.
    01 INP    PIC X(14).
    01 A      PIC S9(3).
    01 B      PIC S9(3).
    01 C      PIC S9(3).

PROCEDURE                        DIVISION.
MAIN.
    ACCEPT INP.

    UNSTRING INP
    DELIMITED BY SPACE
    INTO A B C.

    IF A <= C AND C <= B THEN
        DISPLAY "Yes"
    ELSE
        DISPLAY "No"
    END-IF.

    STOP RUN.
