		IDENTIFICATION DIVISION.
        PROGRAM-ID. AtCoder.
      
        ENVIRONMENT DIVISION.
      
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01 INP PIC X(100).
        01 A PIC 9(15).
        01 B PIC X(6).
        01 C PIC 9(15).
      	01 t PIC 9(15).
	    01 temp1 PIC 9(15).
        01 temp2 PIC 9(15).
        01 N PIC 9(15).
      
        PROCEDURE DIVISION.
      	MAIN.
			ACCEPT A.
      		COMPUTE A = 3 * A * A.
      		MOVE A to B.
      		DISPLAY B.
		STOP RUN.