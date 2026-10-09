import os
import sys
import json
import subprocess

print("=========================================")
print("     SADEX BETA EMULATOR CORE RUNNER     ")
print("=========================================")

print("1. Initializing Keymapping Driver...")
os.system("python keymapper.py")

print("2. Launching Android OS Engine via QEMU...")
if os.name == 'nt':
    os.system("launch_qemu_android.bat")
else:
    print("[Linux/Termux Test Mode] Android Engine Command Script Ready!")

