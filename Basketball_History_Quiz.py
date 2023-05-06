print('Welcome to my history on basketball game')

playing = input('Type Yes or No to play: ') # This line asks the user to type yes or no if they want to play

if playing.lower() != 'yes':    # This if statement outputs: if the user does not want to play, then end the program
    print('Okay, thanks for coming.')
    quit()

print("Super! Let's play!")
score = 0

answer = input('What team did Michael Jordan play for? ') # Question 1
if answer.lower() == "chicago bulls":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect! He played for the Chicago Bulls!\n')

answer = input('How many points is a three-pointer? ') # Question 2
if answer.lower() == "3 points":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('How long is an NBA court? (in feet) ') # Question 3
if answer.lower() == "90 feet":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('How many points is a free throw? ') # Question 4
if answer.lower() == "1 point":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('Who scored 100 points in a game? ') # Question 5
if answer.lower() == "wilt chamberlain":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('How many free throw attempts come after a foul? ') # Question 6
if answer.lower() == "2 free throws":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('What team did Kobe Bryant play for? ') # Question 7
if answer.lower() == "los angeles lakers":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('Who is the current leading scorer in NBA history? ') # Question 8
if answer.lower() == "lebron james":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('How many teams are currently in the NBA? ') # Question 9
if answer.lower() == "30 teams":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

answer = input('How long is a NBA game with no stoppage? ') # Question 10
if answer.lower() == "48 minutes":
    print('Correct!\n')
    score += 1
else:
    print('That is incorrect!\n')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score/10) * 100) + '%.')