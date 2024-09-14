       IDENTIFICATION DIVISION.
       PROGRAM-ID. ADD-EXAMPLE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A PIC 9(4) VALUE 1000.
       01 B PIC 9(4) VALUE 2000.
       01 C PIC 9(4) VALUE 0000.
       01 D PIC 9(4) VALUE 0000.
       01 E PIC 9(4) VALUE 0000.
       01 F PIC X(4) VALUE "ABCD".
       01 GROUP-1.
          05 NUM1 .
             10 NUM3  PIC 9V99 VALUE 20.
          05 NUM2 PIC 9(4) VALUE 20.
       01 GROUP-2.
          05 NUM1.
             10 NUM5 PIC 9(5) VALUE 20.
          05 NUM2 PIC 9(4) VALUE 40.
       
       PROCEDURE DIVISION.
           ADD NUM5 OF NUM1 OF GROUP-2 NUM2 OF GROUP-2 TO A B .
           DISPLAY NUM5.
           STOP RUN.
       