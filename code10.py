#Checking Love count of couple
men_name = input("enter name of the men in the couple: ")
women_name = input("enter name of the women in the couple: ")
couple = men_name.lower() + women_name.lower()
score_1 = couple.count('t') + couple.count('r') + couple.count('u') + couple.count('e')
score_2 = couple.count('l') + couple.count('o') + couple.count('v') + couple.count('e')
score = str(score_1)+ str(score_2)
if int(score) < 10 or int(score) > 90:
    print(f"Your score{score} is like coke and Mentos")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your {score} are alright together")
else:
    print(f"your score is {score}")