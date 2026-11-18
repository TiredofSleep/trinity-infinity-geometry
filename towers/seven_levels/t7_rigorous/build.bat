@echo off
rem Build t7_rigorous.exe with MSVC: /fp:strict keeps every double operation IEEE round-to-nearest, one rounding each.
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" >nul
cd /d "%~dp0"
cl /nologo /O2 /fp:strict /openmp /W3 t7_rigorous.c /Fe:t7_rigorous.exe
