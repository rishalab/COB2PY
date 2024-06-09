       IDENTIFICATION DIVISION.
       PROGRAM-ID. MULTIPLY-EXAMPLE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 A PIC 9(4) VALUE 5.
       77 B PIC 9(4) VALUE 10.
       77 C PIC 9(8) VALUE 0.
       77 D PIC 9(8) VALUE 0.
       77 E PIC 9(4) VALUE 2.
       
       PROCEDURE DIVISION.
           MULTIPLY A  BY B GIVING C D.
           DISPLAY 'Result of A * B giving C: ' C.
           DISPLAY 'Result of A * B giving D: ' D.
           multiply a by e b 
           DISPLAY e " " b.
           STOP RUN.
       