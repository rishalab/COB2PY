      IDENTIFICATION DIVISION.
      PROGRAM-ID. 132A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP.
      	03 A PIC X(1).
       	03 B PIC X(1).
       	03 C PIC X(1).
       	03 D PIC X(1).
       
      PROCEDURE DIVISION.
      
      ACCEPT INP.
      
      EVALUATE TRUE
      WHEN ( A = B ) AND ( C = D )
       	IF A = C
        DISPLAY "No"
        ELSE
        DISPLAY "Yes"
      	END-IF
      WHEN ( A = C ) AND ( B = D )
      WHEN ( A = D ) AND ( B = C )
       	IF A = B
        DISPLAY "No"
        ELSE
        DISPLAY "Yes"
      	END-IF
      WHEN OTHER
        DISPLAY "No"
      END-EVALUATE.
      
      STOP RUN.
  
