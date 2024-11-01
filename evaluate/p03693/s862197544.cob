      IDENTIFICATION DIVISION.
      PROGRAM-ID. 064A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP PIC X(10).
      01 INP2.
       03 R PIC 9(1).
       03 G PIC 9(1).
       03 B PIC 9(1).
      01 SHO PIC 9(3).
      01 AMA PIC 9(1).
      
      PROCEDURE DIVISION.
      ACCEPT INP.
      UNSTRING INP DELIMITED BY " "
      INTO R G B.
      
      DIVIDE INP2 BY 4 GIVING SHO REMAINDER AMA.
      IF AMA = 0
        DISPLAY "YES"
      ELSE
        DISPLAY "NO"
      END-IF.
	  STOP RUN.      
      
