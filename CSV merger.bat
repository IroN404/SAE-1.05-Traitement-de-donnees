@echo off
chcp 28591 > nul
set /p VAR1=Entrez Le dossier source ?
set /p VAR2=Entrez Le dossier destination ?
cd %VAR1%
echo Les fichiers CSV pr�sents dans ce r�pertoire vont �tre fusionn�s
pause
copy *.csv netflix.csv
echo Et d�plac�s vers le dossier de destination
pause
move %VAR1%\netflix.csv %VAR2%