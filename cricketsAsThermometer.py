# print instructions

print("Hey Dipper, I'll calculate the temperature for you.")
print("Using your stopwatch, count how many times the cricket chirps in 13 seconds.")

# get input

Chirps=input("Enter the number of chirps here: ")

# figure out calculations

Chirps=float(Chirps)
Temperature=(Chirps+40)

# print the results

if Temperature < 55:
    print("Too cold!")
else:
    print("The temperature is",Temperature,"degrees")