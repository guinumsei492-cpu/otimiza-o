import socket
import os
import subprocess

def executar_otimizacao(cmd):
    if cmd == "clean_temp":
        os.system('del /s /f /q %temp%\*.*')
        os.system('ipconfig /flushdns')
    elif cmd == "high_perf":
        os.system('powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
    elif cmd == "game_mode":
        # Comando para dar prioridade ao processo do jogo
        os.system('cmd /c start /high "" "C:\Caminho\Do\Seu\Jogo.exe"')

# Lógica de conexão Wi-Fi entre Celular e PC vai aqui
