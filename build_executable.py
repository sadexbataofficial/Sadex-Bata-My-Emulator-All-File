import os
import subprocess

print("Creating standalone executable package for Sadex Beta...")

# PyInstaller command to compile Sadex.py into a single package
command = [
    "pyinstaller",
    "--onefile",
    "--windowed",
    "--name=Sadex-Beta-Engine",
    "Sadex.py"
]

try:
    subprocess.run(command, check=True)
    print("✅ Build Successful! Check the 'dist' folder for Sadex-Beta-Engine.")
except Exception as e:
    print(f"❌ Error during compilation: {e}")
