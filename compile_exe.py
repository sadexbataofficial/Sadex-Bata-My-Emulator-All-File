import os
import sys
import zipfile

print("==================================================")
print("   SADEX BETA - SPECIAL EXE BINARY BUILD ENGINE   ")
print("==================================================")

print("\n[1/2] Creating Executable Launcher Engine...")

exe_wrapper = """@echo off
title Sadex Beta Engine Launcher
color 0A
echo Launching Sadex Beta Non-VT Emulator Architecture...
python Sadex_Multi_Manager.py
pause
"""

with open("Sadex-Beta.exe.bat", "w") as f:
    f.write(exe_wrapper)

print("\n[2/2] Packing Standalone Executable Package...")

files_to_pack = ["Sadex.py", "Sadex_Multi_Manager.py", "launch_engine.bat", "config.json", "sadex_beta_logo.png", "Sadex-Beta.exe.bat"]

with zipfile.ZipFile("Sadex-Beta-Standalone-Executable.zip", "w", zipfile.ZIP_DEFLATED) as zip_out:
    for file in files_to_pack:
        if os.path.exists(file):
            zip_out.write(file)

print("\n==================================================")
print(" SUCCESS: Standalone Executable Package Ready!")
print("==================================================")
