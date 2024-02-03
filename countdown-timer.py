import time

def countdown_timer(duration):
    for remaining in range(duration, 0, -1):
        print(f"Time remaining: {remaining} seconds", end='\r')
        time.sleep(1)
    print("\nThanks for Watching ! ")

def get_user_input():
    while True:
        try:
            duration = int(input("Enter the countdown duration in seconds: "))
            if duration > 0:
                return duration
            else:
                print("Please Enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    countdown_duration = get_user_input()
    countdown_timer(countdown_duration)