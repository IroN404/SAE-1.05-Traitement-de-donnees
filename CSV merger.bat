@echo off
chcp 28591 > nul
set /p VAR=Entrez Le répertoire de travail : 
cd %VAR%\data\raw
echo Les fichiers CSV présents dans ce répertoire vont être fusionnés
pause
copy *.csv netflix.csv
echo Et déplacés vers le dossier de destination
pause
move %VAR%\data\raw\netflix.csv %VAR%\data\cleaned
