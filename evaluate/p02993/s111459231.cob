		IDENTIFICATION DIVISION.
        PROGRAM-ID. AtCoder.
      
        ENVIRONMENT DIVISION.
      
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01 INP PIC X(100).
        01 A PIC 9(15).
        01 B PIC 9(15).
        01 C PIC 9(15).
      	01 D PIC 9(15).
      	01 E PIC 9(15).
      	01 t PIC 9(15).
	    01 temp1 PIC 9(15).
        01 temp2 PIC 9(15).
        01 N PIC 9(15).
      
        PROCEDURE DIVISION.
      	MAIN.
			ACCEPT A.
      		COMPUTE B = A / 10.
      		COMPUTE B = A - B * 10.
      		COMPUTE A = (A - B) / 10.
      		COMPUTE C = A / 10.
      		COMPUTE C = A - C * 10.
      		COMPUTE A = (A - C) / 10.
      		COMPUTE D = A / 10.
      		COMPUTE D = A - D * 10.
      		COMPUTE A = (A - D) / 10.
      		MOVE A to E.
      		IF B = C OR C = D OR E = D THEN
      			DISPLAY "Bad"
      		ELSE
      			DISPLAY "Good"
      		END-IF.
		STOP RUN.