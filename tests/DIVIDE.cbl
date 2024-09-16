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
       01 H PIC 9(2) VALUE 50.
       01 I PIC 9(3).
       01 J PIC 9(3) VALUE 12.
       01 K PIC 9(3).
       01 L PIC 9(3).
       01 GROUP-1.
            05 NUM1 .
                10 NUM3  PIC 99V99 VALUE 3.
            05 NUM4 PIC 9(4) VALUE 2.
       01 GROUP-2.
            05 NUM1.
                10 NUM5 PIC 99V99 VALUE 11.
            05 NUM2 PIC 99V99 VALUE 12.

       PROCEDURE DIVISION.
           DISPLAY 'DIVIDE A INTO B.: A= ' NUM3 '  ,B= ' NUM5 'kjoioh' NUM2.

           DIVIDE NUM3 INTO NUM5 ROUNDED NUM2 .
           DISPLAY 'DIVIDE A INTO B.: NUM3= ' NUM3  '  ,NUM5= ' NUM5 'kjj' NUM2.
           DISPLAY 'DIVIDE D INTO C GIVING J: C= ' C ' ,D= 'D ', J= ' J.

            DIVIDE D INTO C GIVING J K  ROUNDED REMAINDER H.
           DISPLAY 'DIVIDE D INTO C GIVING J: C= ' C ' ,D= 'D ', J= ' J.

           DISPLAY 'DIVIDE E BY F GIVING I .: E= ' E ' ,F= 'F ', I= ' I.
           DIVIDE E BY F GIVING I REMAINDER H.
           DISPLAY 'DIVIDE E BY F GIVING I.: E= ' E ' ,F= 'F ', I= ' I.

           DISPLAY 'DIVIDE G INTO H GIVING K REMAINDER L: G= ' G ', H= ' H ', K= ' K ', L= ' L.
           DIVIDE G INTO H  GIVING K ROUNDED REMAINDER L.
           DISPLAY 'DIVIDE G INTO H GIVING K REMAINDER L: G= ' G ', H= ' H ', K= ' K ', L= ' L.

           STOP RUN.
           