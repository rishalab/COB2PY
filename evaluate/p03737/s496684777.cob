      IDENTIFICATION DIVISION.
      PROGRAM-ID. 059A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP PIC X(100).
      01 S1.
        03 S1A PIC X(1).
      	03 S1B PIC X(9).
      01 S2.
        03 S2A PIC X(1).
      	03 S2B PIC X(9).
      01 S3.
        03 S3A PIC X(1).
      	03 S3B PIC X(9).
      
      01 ANS.
      	03 ANSX PIC X(1) OCCURS 3 TIMES.
      
      01 IDX PIC 9(1).
      
      PROCEDURE DIVISION.
      ACCEPT INP.
      UNSTRING INP DELIMITED BY " "
      INTO 	S1 S2 S3.

      MOVE  S1A TO ANSX(1).
      MOVE  S2A TO ANSX(2).
      MOVE  S3A TO ANSX(3).
            
      PERFORM VARYING IDX FROM 1 BY 1 UNTIL IDX > 3      
      	EVALUATE ANSX(IDX)
   	   		WHEN "a"
				MOVE "A" TO ANSX(IDX)
   	   		WHEN "b"
				MOVE "B" TO ANSX(IDX)
   	   		WHEN "c"
				MOVE "C" TO ANSX(IDX)
   	   		WHEN "d"
				MOVE "D" TO ANSX(IDX)
   	   		WHEN "e"
				MOVE "E" TO ANSX(IDX)
   	   		WHEN "f"
				MOVE "F" TO ANSX(IDX)
   	   		WHEN "g"
				MOVE "G" TO ANSX(IDX)
   	   		WHEN "h"
				MOVE "H" TO ANSX(IDX)
   	   		WHEN "i"
				MOVE "I" TO ANSX(IDX)
   	   		WHEN "j"
				MOVE "J" TO ANSX(IDX)
   	   		WHEN "k"
				MOVE "K" TO ANSX(IDX)
   	   		WHEN "l"
				MOVE "L" TO ANSX(IDX)
   	   		WHEN "m"
				MOVE "M" TO ANSX(IDX)
   	   		WHEN "n"
				MOVE "N" TO ANSX(IDX)
   	   		WHEN "o"
				MOVE "O" TO ANSX(IDX)
   	   		WHEN "p"
				MOVE "P" TO ANSX(IDX)
   	   		WHEN "q"
				MOVE "Q" TO ANSX(IDX)
   	   		WHEN "r"
				MOVE "R" TO ANSX(IDX)
   	   		WHEN "s"
				MOVE "S" TO ANSX(IDX)
      		WHEN "t"
				MOVE "T" TO ANSX(IDX)
      		WHEN "u"
				MOVE "U" TO ANSX(IDX)
      		WHEN "v"
				MOVE "V" TO ANSX(IDX)
      		WHEN "w"
				MOVE "W" TO ANSX(IDX)
      		WHEN "x"
				MOVE "X" TO ANSX(IDX)
      		WHEN "y"
				MOVE "Y" TO ANSX(IDX)
      		WHEN "z"
				MOVE "Z" TO ANSX(IDX)
			WHEN OTHER
      			CONTINUE
     	END-EVALUATE
      END-PERFORM.
      
      DISPLAY ANS.
      STOP RUN.