      IDENTIFICATION DIVISION.
      PROGRAM-ID.  090A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP PIC X(10).
      01 C1.
      	03 C11 PIC X(1).
      	03 C12 PIC X(1).
      	03 C13 PIC X(1).
      01 C2.
      	03 C21 PIC X(1).
      	03 C22 PIC X(1).
      	03 C23 PIC X(1).
      01 C3.
      	03 C31 PIC X(1).
      	03 C32 PIC X(1).
      	03 C33 PIC X(1).
      
      01 OUT PIC X(3).
      
      PROCEDURE DIVISION.
      ACCEPT INP.
	  MOVE INP TO C1.
            
      ACCEPT INP.
	  MOVE INP TO C2.
            
      ACCEPT INP.
	  MOVE INP TO C3.
      
	  STRING C11 C22 C33 DELIMITED BY SIZE
      INTO OUT.
      
      DISPLAY OUT.
      
      STOP RUN.