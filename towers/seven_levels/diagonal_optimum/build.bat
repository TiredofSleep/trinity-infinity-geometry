@echo off
rem Build bb3.exe, bb5.exe and bb7.exe with MSVC: /fp:strict keeps every double operation IEEE round-to-nearest.
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" >nul
cd /d "%~dp0"
for %%p in (3 5 7) do cl /nologo /O2 /fp:strict /openmp /W3 /DP=%%p bb.c /Fe:bb%%p.exe /Fo:bb%%p.obj
