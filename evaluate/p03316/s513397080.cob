      IDENTIFICATION DIVISION.
      PROGRAM-ID. 101B.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP PIC X(100).
      01 N   PIC 9(10).
      01 S.
      	03 WK-S PIC 9(1) OCCURS 10 TIMES.
      01 IDX PIC 9(2).
      01 ANS PIC 9(10).
      01 SHO PIC 9(10).
      01 AMA PIC 9(10).
      
      PROCEDURE DIVISION.
      ACCEPT INP.
      MOVE INP TO N.
      MOVE INP TO S.
      
      MOVE 1 TO IDX.
      PERFORM UNTIL ( IDX = 10 ) OR ( WK-S(IDX) = SPACE )
      ADD WK-S(IDX) TO ANS 
      ADD 1 TO IDX
      END-PERFORM.
      
      DIVIDE N BY ANS GIVING SHO REMAINDER AMA.
      
      IF AMA = 0
      	DISPLAY "Yes"
      ELSE
      	DISPLAY "No"
      END-IF.
      
      STOP RUN.
      
