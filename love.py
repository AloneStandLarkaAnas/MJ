import time
import sys
import os

# Function to clear the terminal screen
def clear_screen():
    os.system('clear')  # For Unix-like systems, use 'cls' for Windows

# Function to print heart emojis in rain
def heart_rain(duration=600):
    start_time = time.time()
    while time.time() - start_time < duration:
        clear_screen()
        # Print hearts at random positions
        for _ in range(20):  # Number of hearts
            x = os.get_terminal_size().columns
            y = os.get_terminal_size().lines
            print('\033[{};{}H❤️'.format(int(y * random.random()), int(x * random.random())))
        time.sleep(0.1)

# Function to print zooming text
def zoom_text(duration=600):
    end_time = time.time() + duration
    message = "Alone Stand Larka love with you"
    while time.time() < end_time:
        for i in range(1, 6):
            clear_screen()
            # Print the message with varying sizes
            print("\033[1;37;40m" + "\n".join([" " * i + message for _ in range(10)]))
            time.sleep(1)

if __name__ == "__main__":
    import random
    # Run heart rain and zoom text concurrently
    from threading import Thread
    
    heart_thread = Thread(target=heart_rain)
    zoom_thread = Thread(target=zoom_text)
    
    heart_thread.start()
    zoom_thread.start()
    
    heart_thread.join()
    zoom_thread.join()
