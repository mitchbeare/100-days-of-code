#Excercise 1:
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))

#Excercise 2:
#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# BMI = w / h ^ 2

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(int(float(weight) / (float(height) ** 2)))

#Excercise 3
#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#https://waitbutwhy.com/2014/05/life-weeks.html
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#    You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.
#Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remainingYears = 90 - int(age)

#365 days in a year
days = remainingYears * 365
#52 weeks in a year
weeks = remainingYears * 52
#12 months in a year
months = remainingYears * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left")
