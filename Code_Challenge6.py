# Compute the final grade
prelim = eval(input('Please Input Your Prelim Grade --> '))
midterm = eval(input('Midterm Grade --> '))
sfinals = eval(input('Semi-Finals Grade --> '))
finals = eval(input('Finals Grade --> '))
quiz = eval(input('Your Quiz Grade --> '))
project = eval(input('Input Your Project Grade --> '))
# Check if all grades are valid
if (65 <= prelim <= 100) and (65 <= midterm <= 100) and (65 <= sfinals <= 100) and \
   (65 <= finals <= 100) and (65 <= quiz <= 100) and (65 <= project <= 100):
    FG = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + \
         (finals * 0.15) + (quiz * 0.15) + (project * 0.15)
    
    if FG >= 65:
        print('Congrats, you pass the course/subject')
    else:
        print('Sorry, you failed')
else:
    print('Invalid Grade')