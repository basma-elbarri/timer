import time

timer = input('please enter your timer in seconds: ')

while timer.isalpha() == True or timer == "":
    print('please enter a valid number')
    timer = input('please enter your timer in seconds: ')

for x in range (int(timer), 0, -1):
    seconds = x % 60
    minutes = int((x /60) % 60)
    hours = int(x / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")