       IDENTIFICATION DIVISION.
       PROGRAM-ID. test1.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 N PICTURE 9999.
       01 A PIC 9999.
       01 B PIC 9999.
       01 C PIC 9999.
       01 D PIC 9999.
       PROCEDURE DIVISION.
       MAIN.
        ACCEPT N.
        COMPUTE A=N / 1000.
        COMPUTE B= N - A * 1000.
     	COMPUTE B=B / 100.
      	COMPUTE C=N- A * 1000 - B * 100.
      	COMPUTE C=C / 10.
      	COMPUTE D=N - A * 1000 - B *100 - C*10.
      	IF A=B AND B=C THEN
      		DISPLAY "Yes"
      	ELSE IF B=C AND C=D THEN
      		DISPLAY "Yes"
      	ELSE
      		DISPLAY "No"
      	END-IF.
        STOP RUN.
