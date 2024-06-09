       IDENTIFICATION DIVISION.
       PROGRAM-ID. MultiplyExample.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 A PIC 9(4) VALUE 10.
       77 B PIC 9(4) VALUE 5.
       77 C PIC 9(4) VALUE 0.
       77 D PIC 9(4) VALUE 15.
       77 E PIC 9(4) VALUE 3.
       77 F PIC 9(4) VALUE 0.
       77 G PIC 9(4) VALUE 8.
       77 H PIC 9(4) VALUE 4.
       77 I PIC 9(4) VALUE 0.
       77 J PIC 9(4) VALUE 7.
       77 K PIC 9(4) VALUE 6.
       77 L PIC 9(4) VALUE 0.
       77 M PIC 9(4) VALUE 12.
       77 N PIC 9(4) VALUE 3.
       77 O PIC 9(4) VALUE 0.
       77 P PIC 9(4) VALUE 0.
       
       PROCEDURE DIVISION.
           MULTIPLY A BY B.
           DISPLAY 'A * B = ' B.

           MULTIPLY D BY E GIVING F.
           DISPLAY 'D * E giving F = ' F.

           MULTIPLY G BY H GIVING I.
           DISPLAY 'G * H giving I = ' I.

           MULTIPLY J BY K GIVING L.
           DISPLAY 'J * K giving L = ' L.

           MULTIPLY M BY N GIVING O P.
           DISPLAY 'M * N giving O = ' O ' and P = ' P.

           STOP RUN.
