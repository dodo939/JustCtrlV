from pynput.keyboard import Controller
import keyboard
import pyperclip

controller = Controller()

print("Usage: Do not care about anything. Just Ctrl-V like you always do!")

while True:
    keyboard.wait("ctrl+v")
    content = pyperclip.paste()
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    keyboard.release("ctrl")
    controller.type(content)
