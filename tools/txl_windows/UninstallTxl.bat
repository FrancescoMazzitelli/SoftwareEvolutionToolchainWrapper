@echo off
rem TXL Windows 95/98/ME/NT/2000/XP/Vista Uninstall Script
rem J.R. Cordy, Queen's University, October 2002 (Rev Oct 2009)

rem Announce our plans
echo Uninstalling the TXL commands from your system
echo/
pause
cls

rem What kind of place are we
echo Determining system environment ...
if "%OS%"=="Windows_NT" echo Windows NT, 2000, XP, Vista or 7.
if "%OS%"=="Windows_NT" set CommandDir="%windir%\System32"
if "%OS%"==""  echo Windows 95, 98 or ME.
if "%OS%"==""  set CommandDir="%windir%\Command"
echo/
pause
cls

rem OK delete the txl commands from the command dir
echo Deleting TXL commands from the system command directory ...
del %CommandDir%\txl.exe
del %CommandDir%\txldb.exe
del %CommandDir%\txlc.bat
del %CommandDir%\txlp.bat
echo Done.
echo/
pause
cls

rem And delete the txl library and library dir
echo Deleting the TXL library from the system directory ...
del /q %CommandDir%\..\txl\*.*
rmdir %CommandDir%\..\txl
echo Done.
echo/
pause
cls

rem All finished, bye ...
echo TXL has been deleted from your system.
echo/
pause
exit

rem Rev 8.1.05
