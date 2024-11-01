       IDENTIFICATION DIVISION.
       PROGRAM-ID. test1.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 INP PIC 99.
       01 A PIC 9.
       PROCEDURE DIVISION.
       MAIN.
       	ACCEPT INP.
      	COMPUTE A=INP/10.
      	COMPUTE INP=INP - A*10.
      	IF A=9 OR INP=9 THEN
      		DISPLAY "Yes"
      	ELSE
      		DISPLAY "No"
      	END-IF.
        STOP RUN.
