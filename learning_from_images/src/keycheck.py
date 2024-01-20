# only for windows and Linux

import keyboard

print("Press the key you want to use for the hotkey.")
key = keyboard.read_key()
print(f"The key code for the pressed key is: {key}")
