# error sa .lower()

print("WELCOME TO MY COMPUTER QUIZ!")

playing = input("Do you want to play?  ")
score = 0

if playing != "yes": #convert text to lower case
    quit()
print("Okay! Let's play :)")

# question 1 ====================
answer = input("What does CPU stand for?  ")
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# question 2 ====================
answer = input("What does GPU stand for?  ")
if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# question 3 ====================
answer = input("What does RAM stand for?  ")
if answer == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# question 4 ====================
answer = input("What does PSU stand for?  ")
if answer == "Power Supply Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")