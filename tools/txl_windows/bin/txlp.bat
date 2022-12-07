@echo off
rem FreeTXL 10.8 Profiler

rem Where's FreeTXL?
if "%OS%"=="Windows_NT" set CommandDir=%windir%\System32
if "%OS%"==""  set CommandDir=%windir%\Command
set TXLLIB=%CommandDir%\..\txl

rem Find profile command arguments
set parg1=
set parg2=
set parg3=
: getprofargs
if "%1" == "-help" goto usage
if "%1" == "-parse" goto profarg
if "%1" == "-time" goto profarg
if "%1" == "-space" goto profarg
if "%1" == "-calls" goto profarg
if "%1" == "-cycles" goto profarg
if "%1" == "-eff" goto profarg
if "%1" == "-percall" goto profarg
goto doneargs
: profarg
if "%parg1%" == "" set parg1=%1
if "%parg2%" == "" set parg2=%1
if "%parg3%" == "" set parg3=%1
shift
goto getprofargs

rem Run the TXL command, using txlpf
: doneargs
if "%1" == "" goto profiled
if exist txl.pprofout del txl.pprofout
if exist txl.rprofout del txl.rprofout
%TXLLIB%\txlpf.exe -q %1 %2 %3 %4 %5 %6 %7 %8 %9 > nul
: profiled
if exist txl.rprofout goto analyze

: usage
echo Usage:  txlp [-parse] [-time] [-space] [-calls] [-cycles] [-eff] [-percall] [txloptions] inputfile [txlfile]
goto exit

rem Analyze the results
: analyze
%TXLLIB%\txlapr.exe %parg1% %parg2% %parg3% > profile.txt
echo Output profile in 'profile.txt'

rem Clean up
: exit
set parg1=
set parg2=
set parg3=

rem Rev 16.1.05
