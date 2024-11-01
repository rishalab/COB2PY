IDENTIFICATION DIVISION.
      PROGRAM-ID. 046A.
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 INP PIC X(100).
      01 A PIC 9(3).
      01 B PIC 9(3).
      01 C PIC 9(3).
      
      PROCEDURE DIVISION.
      ACCEPT INP.
      UNSTRING INP DELIMITED BY " "
      INTO A B C.
      
      EVALUATE TRUE
      WHEN ( A = B ) AND ( B = C )
      	DISPLAY "1"
      WHEN ( A = B ) AND ( A NOT = C )
      WHEN ( A = B ) AND ( B NOT = C )
      WHEN ( B = C ) AND ( B NOT = A )
      WHEN ( B = C ) AND ( C NOT = A )
      WHEN ( A = C ) AND ( A NOT = B )
      WHEN ( A = C ) AND ( C NOT = B )
      	DISPLAY "2"
      WHEN ( A NOT = B ) AND ( B NOT = C )
      	DISPLAY "3"
      WHEN OTHER
      	CONTINUE
      END-EVALUATE.
      
      STOP RUN.