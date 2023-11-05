import time

# Programmer: Peter Cook
# Peter Cook:
# Purpose: To ask user about the weather

# Timed print statement 
print('CEIS 110 mod 2 deliverable')
time.sleep(0.5)
print('App: Weather Advisor')
time.sleep(0.5)
print('Created by: Peter Cook')
time.sleep(0.5)

name = input('What do they call you: ')
city = input('Where are you from.... just the city... not at all for stalking purposes:  ')
age = int(input('How old are you? '))
temperature = int(input('What is the temperature? check your phone or turn on the news its not that hard. '))

if temperature <= 65 and age >= 30:
    print(f"Hello {name}, it's way to cold outside.... That's why your knees hurt, call in sick and go back to bed. ")
elif temperature < 65 and age < 30:
    print(f"Hello {name}, it's cold outside, but you're young...Put a jacket on amd take you're behind to work!!!")
elif 65 <= temperature <= 80:
    print(
        f"Hello {name} Thats the sweet spot, its perfect outside!!!.... ooops I didnt check for rain, look out the window, is it raining.")
elif temperature > 80 and temperature <= 90:
    print(f"Hello {name}, it's hot outside, drink plenty of water.")
else:
    print(
        f"Hello {name}, it's way to hot outside... I mean the kind of heat that makes people upset for no reason...Remember all the talk about global warming, well you were warned.")
