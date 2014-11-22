print "Watch out, world"
twitter = "@hearmecode"
print twitter
print "Welcome to Hear Me Code"#choose double or single quotes and stay consistent
print 'No boys allowed!'
print "Test print string"
print "But 'this' is okay"

print 'How about "this"'
print "what about 'this'?"
print "my governor's name is"#apostrophe okay
print 'she said "testing"'#read about triple quotes from the slides 
#special characters \n newline \t tab, just like JS, but in Python spaces matter. Literal quotes in front of single or double quotes to make sure they get printed as usual. Use \in front of quote marks.

#>>> in terminal means you've left the Python world by typing exit()
print "Lesson\t\tTopic\n1\t\t\tStrings and Conditionals\n2\t\t\tLists and Loops\n3\t\t\tDictionaries & Files"#& prints as usual
#Python is a scripting language. You could use it to build a web app along with Django, but its not often done. 

#Slicing lesson - how to navigate within strings
print twitter [1:5]#prints hear
print twitter [-11]#prints @
print twitter [1:]#Python assumes we want to go all the way to the last index and prints hearmecode without the @

#phone="202-559-7500"#declare and define the variable


#String formatting
first_name="Mariah"
age=23#or could use quotes and make this a string. .format works on strings and numbers.
phone="202-559-7500"
print "My name is {0} and my age is {1}".format(first_name,age)

print "Your number is: {0}".format(phone)
print "Local: {0}".format(phone[5:13])#yes, square brackets to slice this string go within the ()
print "Domestic: ({0}) {1}".format(phone[0:3],phone[5:10])#PROBLEM figure out answer from slides later

email="mariah@neworganizing.com"
print email.find("@")
email = email.replace("@","$")#we are redefining variable here to make this change permanent
print email
print email.upper()

#.strip() removes white space See slides for more formatting methods that are part of python library


#Conditionals asking question to see if a condition is true. 
#If else statement
#one = means youre equating one thing with another. two == means one thing IS the other thing

students = 212 #play with numbers to see different results
capacity = 50

if students < capacity:
	print "Keep Recruiting"
else:
	print "End tickets!"

#elif is like saying but if

teaching_assistants=5

if teaching_assistants==0:
	print "None? Uh oh!"
elif teaching_assistants<students/5:
	print "Keep recruiting TAs"
else:
	print "Aren't the TAs great though?"



#FYI More operators are listed in slides

#below is quick calculator program with 2 variables

goal=95
current_volunteers=94

if current_volunteers==goal:
	print "sweet,just barely!"

elif current_volunteers<goal:
	print "You have {0} volunteers but your goal is {1}. You still need {2} more".format(current_volunteers,goal,goal-current_volunteers)

else:
	print "sweet"


#Start a new Sublime file for completing the Playtime exercises.  every Thursday 6-9 at the rye center







