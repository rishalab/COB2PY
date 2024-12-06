       IDENTIFICATION DIVISION.
       PROGRAM-ID. AddSubtractDemo.

       DATA DIVISION.
       WORKING-STORAGE SECTION.


       01  A            PIC 9(3) VALUE 10.
       01  B            PIC 9(3) VALUE 20.
       01  C            PIC 9(3) VALUE 5.
       01  RESULT       PIC 9(4).
       01  OVERFLOW-FLAG PIC Xx VALUE 'NY'.

       PROCEDURE DIVISION.

           MOVE 0 TO RESULT.
           DISPLAY "Simple ADD: "
           ADD A TO B.
           DISPLAY "A + B = " B.


           DISPLAY "ADD with GIVING: "
           ADD A TO B GIVING RESULT.
           DISPLAY "A + B giving RESULT = " RESULT.


           DISPLAY "ADD multiple variables: "
           ADD A B C GIVING RESULT.
           DISPLAY "A + B + C giving RESULT = " RESULT.


           DISPLAY "ADD with literal values: "
           ADD 15 TO A GIVING RESULT.
           DISPLAY "A + 15 giving RESULT = " RESULT.


           DISPLAY "ADD multiple literals: "
           ADD 5 10 15 GIVING RESULT.
           DISPLAY "5 + 10 + 15 giving RESULT = " RESULT.




           DISPLAY "Simple SUBTRACT: "
           SUBTRACT C FROM B.
           DISPLAY "B - C = " B.


           DISPLAY "SUBTRACT with GIVING: "
           SUBTRACT A FROM B GIVING RESULT.
           DISPLAY "B - A giving RESULT = " RESULT.


           DISPLAY "SUBTRACT multiple variables: "
           SUBTRACT A C FROM B GIVING RESULT.
           DISPLAY "B - A - C giving RESULT = " RESULT.


           DISPLAY "SUBTRACT with literal values: "
           SUBTRACT 5 FROM A GIVING RESULT.
           DISPLAY "A - 5 giving RESULT = " RESULT.


           DISPLAY "SUBTRACT multiple literals: "
           SUBTRACT 5 10 3 FROM B GIVING RESULT.
           DISPLAY "B - 5 - 10 - 3 giving RESULT = " RESULT.





           STOP RUN.
