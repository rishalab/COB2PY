      IDENTIFICATION DIVISION.
      PROGRAM-ID. 122A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 B PIC X(1).
      
      PROCEDURE DIVISION.
      
      ACCEPT B.
      
      EVALUATE B
      	WHEN "A"
      		DISPLAY  "T"
      	WHEN "C"
      		DISPLAY  "G"
      	WHEN "G"
      		DISPLAY  "C"
      	WHEN "T"
      		DISPLAY  "A"
      WHEN OTHER
      	CONTINUE
      END-EVALUATE.
      
      STOP RUN.