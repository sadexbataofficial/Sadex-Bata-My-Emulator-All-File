import json
import time

print("Sadex Free Fire Keymapping Driver v1.0 Initialized...")

default_mapping = {
    "WASD": "Joystick Movement",
    "LCLICK": "Fire / Shoot",
    "RCLICK": "Aim Lock / Scope",
    "SHIFT": "Sprint",
    "SPACE": "Jump",
    "C": "Crouch",
    "R": "Reload"
}

with open("keymap_config.json", "w") as kf:
    json.dump(default_mapping, kf, indent=4)

print("Keymapping Configured Successfully for Free Fire!")
