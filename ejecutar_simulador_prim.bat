@echo off
echo Ejecutando simulador Árbol Parcial Mínimo de Prim...
echo.

:: Verificar si pip está disponible
python -m ensurepip --default-pip

:: Instalar paquetes necesarios
echo Instalando dependencias necesarias...
python -m pip install --upgrade pip
pip install networkx matplotlib

:: Ejecutar el simulador
python simulador_prim.py

pause
