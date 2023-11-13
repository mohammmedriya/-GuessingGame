import random

secret = random.randint(1,20)

guess = 0
attempts = 0

print ("Guess the secret number (1 to 20)")
print ("=================================")
print ("")

while guess != secret:
    attempts += 1

    guess = input("Guess number: ")
    guess = int(guess)

    if (guess > secret):
        print ("Number is too high.")
    elif (guess < secret):
        print ("Number is too low.")


print ("Congratulations, you guessed right !!")
print ("Attempts used: ", attempts)
