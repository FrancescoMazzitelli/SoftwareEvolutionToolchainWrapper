@echo off
rem TXL Windows 95/98/ME/NT/2000/XP/Vista Install Script
rem J.R. Cordy, Queen's University, October 2002 (Rev June 2018)

rem Announce our plans
echo Installing TXL 10.8b on your system
echo/
pause
cls

rem What kind of place are we
echo Determining system environment ...
if "%OS%"=="Windows_NT" echo Windows 7, 8 or 10.
if "%OS%"=="Windows_NT" set CommandDir="%windir%\System32"
if "%OS%"==""  echo Windows 95, 98 or ME.
if "%OS%"==""  set CommandDir="%windir%\Command"
echo/
pause
cls

rem Check we have the TXL distribution files
set HERE=%~dp0
chdir %HERE%
if exist bin\txl.exe goto gotem
echo/
echo Can't find the unzipped TXL distribution folder Txl106a764\ -
echo please run this install script directly from the distribution folder.
echo/
pause
exit
:gotem

rem OK copy the txl commands to the command dir
echo Copying TXL commands to the system command directory ...
copy/y bin\*.* %CommandDir%
if errorlevel 2 goto failed
echo Done.
echo/
pause
cls

rem And copy the txl library to the library dir
echo Copying TXL commands to the txl library directory ...
mkdir %CommandDir%\..\txl
copy/y lib\*.* %CommandDir%\..\txl
if errorlevel 2 goto failed
echo Done.
echo/
pause
cls

rem Time to test
echo Testing that TXL is installed ...
echo/
echo txl -V
txl -V
echo/
if errorlevel 2 goto failed
echo Ok.
echo/
pause
cls

cd test
echo Running test program ...
echo/
echo txl ultimate.que
txl ultimate.que
if errorlevel 2 goto failed
echo/
echo The answer to the Ultimate Question looks right to me.
echo/
pause
cls
goto tryout

:failed
echo/
echo Installation failed!
echo/
echo Possibly you are not logged in as adminstrator -
echo if so, please log in as adminstrator and try again.
echo/
pause
exit

rem Your turn
:tryout
echo TXL is now installed and working.
echo/
pause
exit

rem Rev 12.6.18
