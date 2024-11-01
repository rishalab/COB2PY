       IDENTIFICATION DIVISION.
       PROGRAM-ID. AGC_025_A.
       DATA DIVISION.
       WORKING-STORAGE SECTION.   
           01 MAX_SM  PIC 9(2) VALUE 99.
       
           01 N       PIC 9(6).   
           01 half    PIC 9(5).
           01 i       PIC 9(5).
           01 a       PIC 9(6).
           01 b       PIC 9(6).
           01 asm     PIC 9(2).
           01 bsm     PIC 9(2).
           01 sm      PIC 9(2).
       
           01 r       PIC 9(1).
       
           01 ans     PIC X(2).
       
           01 ZS      PIC X(3).
           01 DUMMY   PIC X(1).
       
       
       PROCEDURE DIVISION.
           ACCEPT N.
       
           DIVIDE 2 INTO N GIVING half.
       
           MOVE MAX_SM TO sm.
       
           PERFORM VARYING i FROM 1 BY 1 UNTIL half < i
               MOVE i TO a
               SUBTRACT i FROM N GIVING b
               MOVE ZERO TO asm
               MOVE ZERO TO bsm
               PERFORM UNTIL a <= ZERO
                   DIVIDE 10 INTO a GIVING a REMAINDER r
                   ADD r TO asm
               END-PERFORM
               PERFORM UNTIL b <= ZERO
                   DIVIDE 10 INTO b GIVING b REMAINDER r
                   ADD r TO bsm
               END-PERFORM
               ADD asm TO bsm
               IF bsm < sm
                   MOVE bsm TO sm
               END-IF
           END-PERFORM.
           
           MOVE sm TO ZS.
           DISPLAY ZS.
           STOP RUN.
       UNANS.
           UNSTRING
               ZS DELIMITED BY ALL SPACE
               INTO DUMMY ans.
