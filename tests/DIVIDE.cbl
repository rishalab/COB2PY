       IDENTIFICATION DIVISION.
       PROGRAM-ID. ExampleProgram.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A PIC 9(2) VALUE 10.
       01 B PIC 9(2) VALUE 23.
       01 C PIC 9(2) VALUE 10.
       01 D PIC 9(2) VALUE 5.
       01 E PIC 9(2) VALUE 10.
       01 F PIC 9(2) VALUE 5.
       01 G PIC 9(2) VALUE 11.
       01 H PIC 9(2) VALUE 5.
       01 I PIC 9(3).
       01 J PIC 9(3).
       01 K PIC 9(3).
       01 L PIC 9(3).
       
       PROCEDURE DIVISION.

           DIVIDE A INTO B.
           DISPLAY 'DIVIDE A INTO B.: A= ' A '  ,B= ' B.

           DIVIDE D INTO C GIVING J.
           DISPLAY 'DIVIDE D INTO C GIVING J: C= ' C ' ,D= 'D ', J= ' J.

           DIVIDE E BY F GIVING I.
           DISPLAY 'DIVIDE E BY F GIVING I.: E= ' E ' ,F= 'F ', I= ' I.

           DIVIDE G INTO H GIVING K REMAINDER L.
           DISPLAY 'DIVIDE G INTO H GIVING K REMAINDER L: G= ' G ', H= ' H ', K= ' K ', L= ' L.

           STOP RUN.