questions = (("How many planets are there in the solar system?"),
             (("What is 4+7?")),
             ("What is the name of US president?"))
options =   (("1. 7, 2. 8, 3. 9, 4. 10"),
             ("1. 10, 2. 9, 3. 12, 4. 11"),
             ("1. Putin, 2. Trump, 3. Epstien, 4. Kim jong un"))
answers = [2,4,2]
score = 0
for x in range(0,len(questions)):
    print(questions[x])
    print(options[x])
    guess = int(input("Your Choice(1-4): "))
    while not guess in (1,2,3,4):
       guess = int(input("Incorrect input! please choose(1-4): "))
       if guess in (1,2,3,4):
           break
    if int(guess) == answers[x]:
        score += 1
print(f"Your final score is: {score}")


