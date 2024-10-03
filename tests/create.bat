@echo off
:: Step 1: Create a folder named accept
mkdir accept

:: Step 2: Create COBOL files with properly formatted content

:: COBOL Code 1 - Accept from DATE
echo IDENTIFICATION DIVISION. > accept\accept1.cbl
echo PROGRAM-ID. AcceptDateExample. >> accept\accept1.cbl
echo DATA DIVISION. >> accept\accept1.cbl
echo WORKING-STORAGE SECTION. >> accept\accept1.cbl
echo 01  WS-Date    PIC 9(8). >> accept\accept1.cbl
echo PROCEDURE DIVISION. >> accept\accept1.cbl
echo ACCEPT WS-Date FROM DATE. >> accept\accept1.cbl
echo DISPLAY "Accepted Date: " WS-Date. >> accept\accept1.cbl
echo STOP RUN. >> accept\accept1.cbl

:: COBOL Code 2 - Accept from DATE YYYYMMDD
echo IDENTIFICATION DIVISION. > accept\accept2.cbl
echo PROGRAM-ID. AcceptDateYYYYMMDD. >> accept\accept2.cbl
echo DATA DIVISION. >> accept\accept2.cbl
echo WORKING-STORAGE SECTION. >> accept\accept2.cbl
echo 01  WS-Date    PIC 9(8). >> accept\accept2.cbl
echo PROCEDURE DIVISION. >> accept\accept2.cbl
echo ACCEPT WS-Date FROM DATE YYYYMMDD. >> accept\accept2.cbl
echo DISPLAY "Accepted Date (YYYYMMDD): " WS-Date. >> accept\accept2.cbl
echo STOP RUN. >> accept\accept2.cbl

:: COBOL Code 3 - Accept from DAY
echo IDENTIFICATION DIVISION. > accept\accept3.cbl
echo PROGRAM-ID. AcceptDayExample. >> accept\accept3.cbl
echo DATA DIVISION. >> accept\accept3.cbl
echo WORKING-STORAGE SECTION. >> accept\accept3.cbl
echo 01  WS-Day    PIC 9(7). >> accept\accept3.cbl
echo PROCEDURE DIVISION. >> accept\accept3.cbl
echo ACCEPT WS-Day FROM DAY. >> accept\accept3.cbl
echo DISPLAY "Accepted Day: " WS-Day. >> accept\accept3.cbl
echo STOP RUN. >> accept\accept3.cbl

:: COBOL Code 4 - Accept from DAY YYYYDDD
echo IDENTIFICATION DIVISION. > accept\accept4.cbl
echo PROGRAM-ID. AcceptDayYYYYDDD. >> accept\accept4.cbl
echo DATA DIVISION. >> accept\accept4.cbl
echo WORKING-STORAGE SECTION. >> accept\accept4.cbl
echo 01  WS-Day    PIC 9(7). >> accept\accept4.cbl
echo PROCEDURE DIVISION. >> accept\accept4.cbl
echo ACCEPT WS-Day FROM DAY YYYYDDD. >> accept\accept4.cbl
echo DISPLAY "Accepted Day (YYYYDDD): " WS-Day. >> accept\accept4.cbl
echo STOP RUN. >> accept\accept4.cbl

:: COBOL Code 5 - Accept from DAY_OF_WEEK
echo IDENTIFICATION DIVISION. > accept\accept5.cbl
echo PROGRAM-ID. AcceptDayOfWeekExample. >> accept\accept5.cbl
echo DATA DIVISION. >> accept\accept5.cbl
echo WORKING-STORAGE SECTION. >> accept\accept5.cbl
echo 01  WS-DayOfWeek    PIC 9(1). >> accept\accept5.cbl
echo PROCEDURE DIVISION. >> accept\accept5.cbl
echo ACCEPT WS-DayOfWeek FROM DAY_OF_WEEK. >> accept\accept5.cbl
echo DISPLAY "Accepted Day of Week: " WS-DayOfWeek. >> accept\accept5.cbl
echo STOP RUN. >> accept\accept5.cbl

:: COBOL Code 6 - Accept from TIME
echo IDENTIFICATION DIVISION. > accept\accept6.cbl
echo PROGRAM-ID. AcceptTimeExample. >> accept\accept6.cbl
echo DATA DIVISION. >> accept\accept6.cbl
echo WORKING-STORAGE SECTION. >> accept\accept6.cbl
echo 01  WS-Time    PIC 9(6). >> accept\accept6.cbl
echo PROCEDURE DIVISION. >> accept\accept6.cbl
echo ACCEPT WS-Time FROM TIME. >> accept\accept6.cbl
echo DISPLAY "Accepted Time: " WS-Time. >> accept\accept6.cbl
echo STOP RUN. >> accept\accept6.cbl

:: COBOL Code 7 - Accept from TODAYS_DATE MMDDYYYY
echo IDENTIFICATION DIVISION. > accept\accept7.cbl
echo PROGRAM-ID. AcceptTodaysDateMMDD. >> accept\accept7.cbl
echo DATA DIVISION. >> accept\accept7.cbl
echo WORKING-STORAGE SECTION. >> accept\accept7.cbl
echo 01  WS-TodaysDate    PIC 9(8). >> accept\accept7.cbl
echo PROCEDURE DIVISION. >> accept\accept7.cbl
echo ACCEPT WS-TodaysDate FROM TODAYS_DATE MMDDYYYY. >> accept\accept7.cbl
echo DISPLAY "Accepted Today's Date (MMDDYYYY): " WS-TodaysDate. >> accept\accept7.cbl
echo STOP RUN. >> accept\accept7.cbl

:: COBOL Code 8 - Accept from mnemonicName
echo IDENTIFICATION DIVISION. > accept\accept8.cbl
echo PROGRAM-ID. AcceptMnemonicExample. >> accept\accept8.cbl
echo DATA DIVISION. >> accept\accept8.cbl
echo WORKING-STORAGE SECTION. >> accept\accept8.cbl
echo 01  WS-Mnemonic    PIC X(10). >> accept\accept8.cbl
echo PROCEDURE DIVISION. >> accept\accept8.cbl
echo ACCEPT WS-Mnemonic FROM SYSIN. >> accept\accept8.cbl
echo DISPLAY "Accepted Mnemonic: " WS-Mnemonic. >> accept\accept8.cbl
echo STOP RUN. >> accept\accept8.cbl
