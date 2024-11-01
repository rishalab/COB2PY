      IDENTIFICATION DIVISION.
      PROGRAM-ID. 056A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP PIC X(3).
      01 A   PIC X(1).
      01 B   PIC X(1).
      
      PROCEDURE DIVISION.
      ACCEPT INP.
      UNSTRING INP DELIMITED  BY " "
      INTO 	A
      		B.

      IF A = "H" 
         IF B = "H"
      	    DISPLAY "H"
         ELSE
      	    DISPLAY "D"
      	 END-IF
      ELSE
      	 IF B = "H"
      	    DISPLAY "D"
         ELSE
			DISPLAY "H"
         END-IF
      END-IF.
      
      STOP RUN.