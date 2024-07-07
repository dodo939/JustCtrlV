from pynput.keyboard import Controller
import keyboard
import pyperclip

controller = Controller()

print("Usage: Do not care about anything. Just Ctrl-V like you always do!")

while True:
    keyboard.wait("ctrl+v")
    content = pyperclip.paste()
    keyboard.release("ctrl")
    controller.type(content)
