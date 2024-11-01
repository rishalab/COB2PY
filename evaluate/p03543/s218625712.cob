      IDENTIFICATION DIVISION.
      PROGRAM-ID. 079A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 N PIC X(4).
      01 INP.
      	03 INP1 PIC 9(1).
      	03 INP2 PIC 9(1).
      	03 INP3 PIC 9(1).
      	03 INP4 PIC 9(1).
      
      PROCEDURE DIVISION.
      ACCEPT N.
      MOVE N TO INP.
      
      EVALUATE TRUE
      WHEN ( INP1 = INP2 ) AND ( INP2 = INP3 )
      WHEN ( INP2 = INP3 ) AND ( INP3 = INP4 )
      	DISPLAY "Yes"
      WHEN OTHER
      	DISPLAY "No"   
      END-EVALUATE.
      
      STOP RUN.