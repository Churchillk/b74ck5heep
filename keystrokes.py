from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        key_str = str(key)
        print(f"Key_pressed: = {key_str}")
        
    except Exception as err:
        pass
    
with Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except Exception as err:
        print("error occured")
            
