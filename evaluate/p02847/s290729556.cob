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
			ACCEPT INP.
      		IF INP(1:3) = "SUN"
      			DISPLAY "7"
      		END-IF.
      		IF INP(1:3) = "MON"
      			DISPLAY "6"
      		END-IF.
      		IF INP(1:3) = "TUE"
      			DISPLAY "5"
      		END-IF.
      		IF INP(1:3) = "WED"
      			DISPLAY "4"
      		END-IF.
      		IF INP(1:3) = "THU"
      			DISPLAY "3"
      		END-IF.
      		IF INP(1:3) = "FRI"
      			DISPLAY "2"
      		END-IF.
      		IF INP(1:3) = "SAT"
      			DISPLAY "1"
      		END-IF.
		STOP RUN.