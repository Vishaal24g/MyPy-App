#QUIZ PROGRAM
import time

ans1  = 'A'
ans2  = 'B'
ans3  = 'C'
ans4  = 'A'
ans5  = 'B'
ans6  = 'C'
ans7  = 'B'
ans8  = 'C'
ans9  = 'C'
ans10 = 'B'

print("Hi, Let's test your knowledge!")
print("Please enter your choice of option as A/B/C/D as per the question")

print("Q1) Which of the following is a Python package used for 2D graphics? \n A) matplotlib.pyplot \n B) matplotlib.pip \n C) matplotlib.numpy \n D) matplotlib.plt")

x= input ("Enter the option: ")
sum=0
if x== ans1:
    sum=sum+1
print('Next question is loading...')
time.sleep(1.5)

print('\n\t')

print("Q2) Identify the package manager for Python packages or modules \n A) Matplotlib \n B) PIP \n C) plt.show() \n D) python package")

x = input ("Enter the option: ")
if x== ans2:
    sum=sum+1
print('Next question is loading...')
time.sleep(1.5)

print('\n\t')

print("Q3) Read the given below statements & identify the right options from the following for Pie Chart \n Statement A: To make a Pie Chart with Matplotlib, we can use the plt.pie() function. \n Statement B: The autopct parameter allows us to display the % value using the Python string formatting. \n A) Statement A is correct \n B) Statement B is correct\n C) Both the statements are correct\n D) Both the statements are incorrect")

x= input ("Enter the option: ")
if x== ans3:
    sum=sum+1
print("Next question is loading...")
time.sleep(1.5)

print('\n\t')

print("Q4) Which of the following method will be used to display the plot? \n A) show() \n B) display() \n C) execute() \n D) plot()")

x= input ("Enter the option: ")
if x== ans4:
    sum=sum+1
print("Next question is loading...")
time.sleep(1.5)

print('\n\t')

print('Q5) Which type of chart shows the relationship between a numerical variable and categorical variable? \n A) Line Chart \n B) Bar Chart \n C) Pie Chart \n D) XY plot')

x= input ("Enter the option: ")
if x== ans5:
    sum=sum+1
print('Next question is loading...')
time.sleep(1.5)

print('\n\t')

print('Q6) Which plot displays the distribution of data based on the five number summary? \n A) Scatter Plot \n B) Line Plot \n C) Box Plot \n D)Chart Plot')

x= input ("Enter the option: ")
if x== ans6:
    sum=sum+1
print('Next question is loading...')
time.sleep(1.5)

print('\n\t')

print("Q7) To give a title to X-Axis, which of the following method is useful? \n A) pl.xtitle(“title”) \n B) pl.xlabel(“title”) \n C) pl.xheader(“title”) \n D) pl.xlabel.show(“title”)")

x= input ("Enter the option: ")
if x== ans6:
    sum=sum+1
print('Next question is loading...')
time.sleep(1.5)

print('\n\t')

print("Q8) To change the width of bars in Bar Chart, which of the following argument (float value) is used? \n A) thick \n B) thickness \n C) width \n D) barwidth")

x= input ("Enter the option: ")
if x== ans6:
    sum=sum+1
print('Next question is loading...')
time.sleep(1.5)


print('\n\t')

print("Q9) Which method is used to display or show the legends of a plot? \n A) pl.show() \n B) pl.display() \n C) pl.legend() \n D) pl.values()")

x= input ("Enter the option: ")
if x== ans6:
    sum=sum+1
print('Next question is loading...')
time.sleep(1.5)

print('\n\t')

print("Q10) What kind of plot(s) would you use to examine the distribution of a numeric variable? \n A) Scatter plot \n B) Boxplot \n C) Bar Plot \n D) Histogram")

x= input ("Enter the option: ")
if x== ans6:
    sum=sum+1

time.sleep(1.5)

print('\n\t')
print('The quiz is over')
print('Please wait while your scores are being calculated....')
time.sleep(2.5)

if sum == 10:
    print('Your score is: \n', sum,'/10')
    print("Keep up the good work!")
elif sum < 3:
    print('Your score is: \n', sum,'/10')
    print("Mistakes happen, Revise your concepts and attempt the questions carefully!")
elif sum < 6:
    print('Your score is: \n', sum,'/10')
    print("Don't feel bad, there is still room for improvement!")
elif sum < 9:
    print('Your score is: \n', sum,'/10')
    print("Almost there, you just need some more practise!")
else:
    print('Your score is: \n', sum,'/10')
