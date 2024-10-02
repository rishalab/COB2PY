IDENTIFICATION DIVISION.
PROGRAM-ID. GoToMultipleLabels.

DATA DIVISION.
WORKING-STORAGE SECTION.
    01 identifier   PIC 9 VALUE 2.

PROCEDURE DIVISION.
    GO TO procedureName1 procedureName2 procedureName3 DEPENDING ON identifier.
    STOP RUN.

procedureName1.
    DISPLAY 'Executing procedureName1'.
    STOP RUN.

procedureName2.
    DISPLAY 'Executing procedureName2'.
    STOP RUN.

procedureName3.
    DISPLAY 'Executing procedureName3'.
    STOP RUN.
