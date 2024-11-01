 IDENTIFICATION DIVISION.
 PROGRAM-ID. 042A. 
 DATA DIVISION.
 WORKING-STORAGE SECTION.
  01 INP.
    03 A      PIC 9(1).
    03 FILLER PIC X.
    03 B      PIC 9(1).
    03 FILLER PIC X.
    03 C      PIC 9(1).
  01 COUNT5   PIC 9(1) VALUE ZERO.
  01 COUNT7   PIC 9(1) VALUE ZERO.
       
 PROCEDURE DIVISION.
 
  ACCEPT INP.
      
  IF A = 5 
      ADD 1 TO COUNT5
      ELSE
      IF A = 7
      	ADD 1 TO COUNT7
        ELSE
        CONTINUE
      END-IF
  END-IF.
      
  IF B = 5 
      ADD 1 TO COUNT5
      ELSE
      IF B = 7
      	ADD 1 TO COUNT7
        ELSE
        CONTINUE
      END-IF
  END-IF.
      
  IF C = 5 
      ADD 1 TO COUNT5
      ELSE
      IF C = 7
      	ADD 1 TO COUNT7
        ELSE
        CONTINUE
      END-IF
  END-IF.
  
  IF COUNT5 = 2 AND COUNT7 = 1
      DISPLAY "YES"
  ELSE
      DISPLAY "NO"
  END-IF.
        
 STOP RUN.