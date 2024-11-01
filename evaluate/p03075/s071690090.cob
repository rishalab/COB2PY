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
        01 F PIC 9(15).
      	01 t PIC 9(15).
	    01 temp1 PIC 9(15).
        01 temp2 PIC 9(15).
        01 N PIC 9(15).
      
        PROCEDURE DIVISION.
      	MAIN.
			ACCEPT A.
      		ACCEPT B.
      		ACCEPT C.
      		ACCEPT D.
      		ACCEPT E.
      		ACCEPT F.
      		IF E - A > F THEN
      			DISPLAY ":("
      		ELSE
      			DISPLAY "Yay!"
      		END-IF.
		STOP RUN.