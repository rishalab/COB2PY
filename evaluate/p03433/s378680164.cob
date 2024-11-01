      IDENTIFICATION DIVISION.
      PROGRAM-ID. 088A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 N PIC 9(5).
      01 A PIC 9(4).
      01 SHO PIC 9(3).
      01 AMA PIC 9(3).
      01 ANS PIC 9(3).
      
      PROCEDURE DIVISION.
      ACCEPT N.
      ACCEPT A.
      DIVIDE N BY 500 GIVING SHO REMAINDER AMA.
      IF A >= AMA
         DISPLAY "Yes"
      ELSE
         DISPLAY "No"
      END-IF.
      STOP RUN.