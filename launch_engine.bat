@echo off
title Sadex Beta Engine Runner
echo Launching Sadex Engine without Hardware VT...
qemu-system-x86_64.exe -hda system.img -m 2048 -smp 2 -accel tcg
pause
