       IDENTIFICATION DIVISION.
       PROGRAM-ID. PerformVarmple.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 I PIC 9(02) VALUE 0.
       01 J PIC 9(02) VALUE 0.
       01 K PIC 9(02) VALUE 0.
       01 L PIC 9(02) VALUE 0.

       PROCEDURE DIVISION.
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 10
               AFTER J FROM 1 BY 1 UNTIL J > 5
               DISPLAY 'Value of I: ' I ', Value of J: ' J
           END-PERFORM.
            PERFORM VARYING K FROM 1 BY 1 UNTIL K > 10
               DISPLAY 'Value of K: ' K 
           END-PERFORM.
                      DISPLAY 'HI'

           STOP RUN.
