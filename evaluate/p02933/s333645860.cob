		IDENTIFICATION DIVISION.
        PROGRAM-ID. AtCoder.
      
        ENVIRONMENT DIVISION.
      
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        01 INP PIC X(100).
        01 A PIC 9(11).
        01 B PIC 9(11).
        01 C PIC 9(11).
	    01 temp1 PIC 9(11).
        01 temp2 PIC 9(11).
        01 N PIC 9(11).
      
        PROCEDURE DIVISION.
      	MAIN.
            ACCEPT A.
			ACCEPT INP.
			IF A >= 3200 THEN
				DISPLAY INP
			ELSE 
				DISPLAY "red"
			END-IF.
		STOP RUN.