       IDENTIFICATION DIVISION.
       PROGRAM-ID. ExhibitExample3.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 GROUP-1.
           02 myName   PIC X(20) VALUE 'Alice'.
       01 age      PIC 99 VALUE 30.

       PROCEDURE DIVISION.
           EXHIBIT NAMED myName OF GROUP-1 1.

           STOP RUN.
