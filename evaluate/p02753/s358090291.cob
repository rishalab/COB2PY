      IDENTIFICATION DIVISION.
      PROGRAM-ID. 158A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP PIC X(100).
      01 S.
      	03 S1 PIC X(1).
      	03 S2 PIC X(1).
      	03 S3 PIC X(1).
      
      PROCEDURE DIVISION.
      ACCEPT INP.
      MOVE INP TO S.
      
      EVALUATE TRUE
      WHEN ( S1 = S2 ) AND ( S2 = S3 )
      	DISPLAY "No"
      WHEN OTHER
      	DISPLAY "Yes"
      END-EVALUATE.
      
      STOP RUN.