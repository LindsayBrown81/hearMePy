# Challenge Level: Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.

# Sample output:
#       Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234

# Challenge 2: Add the extra information from survey.csv into all_employees.csv as extra columns.  
# IMPORTANT: It would probably be a good idea to save it as an extra file instead of accidentally overwriting your original!
# By the end, your all_employees.csv should contain the following columns: name, email, phone, department, position, twitter, github


# with open ("survey.csv", "r") as survey_file:
# 	respondents = survey_file.read()
# 	print "\n",respondents

# with open ("all_employees.csv", "r") as all_file:
# 	all = all_file.read()
# 	print "\n",all

#~emails is the only column header that appears in both csv files. first I'm going to print out the emails from each csv file.
# with open ("survey.csv", "r") as survey_file:
# 	respondents = survey_file.read().split("\n")
# 	for index, respondent in enumerate(respondents):
# 		respondents[index] = respondent.split(",")
# 		print respondents[index][0]

# with open ("all_employees.csv", "r") as all_file:
# 	all = all_file.read().split("\n")
# 	for index, employee in enumerate(all):
# 		all[index] = employee.split(", ")#I added space after comma. 

#~then, so that I can run methods on these two sets of strings, I'll turn them into two lists, although I could have somehow used the string method, .find()
	# allEmailList = []
	# for name, email, phone, department, position in all[1:]:
	# 	allEmailList.append(email)
	# print "\n",allEmailList

	# surveyEmailList = []
	# for email, twitter, git in respondents[1:]:
	# 	surveyEmailList.append(email)
	# print "\n",surveyEmailList

# Reminder of Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, 
# print out the rest of their information from all_employees.csv.

#~then, i'll use an if/else statement if email == email, wait, this sounds like mapping/matching keys (emails) and their values, meaning I need to create two dicts.
#Or do I? ~~~Can't I search for matching values between two lists using keyword, in? The in keyword allows you to check whether a value exists in the list
#From within allEmailList, I might ask, is "value" in surveyEmailList? If False, then surveyEmailList.append("value")
#list.append() adds an item to the end. If I work with index positions, say, is [index][0]==. Wait, I don't want to work with indices.
#You know what? I think dicts were made for this type of key-value matching. Let's move forward with reading the csv files and getting their content into two dicts.

# code below shows function on how to create dicts from reading csv files. source: https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/csv_to_dict.py
# I could have written one generic function
# def csvtodict(filename):
def csvtodict(survey):
#   with open(filename, 'r') as csv_file:
	with open("survey.csv", "r") as csv_file:#~I prefer double quotes. Also, quotes were needed around filename.
#   	text = csv_file.read().strip().split('\n')
		surveyText = csv_file.read().strip().split("\n")
#   header_row = text[0].split(',')
	header_row = surveyText[0].split(",")
#	dictionary = {}
	dictionarySurvey = {}
#   for row, line in enumerate(text[1:]):
	for row, line in enumerate(surveyText[1:]):
#		dictionary[row] = {}
		dictionarySurvey[row] = {}
#       for col, cell in enumerate(line.split(',')):
		for col, cell in enumerate(line.split(",")):
#           dictionary[row][header_row[col]] = cell
			dictionarySurvey[row][header_row[col]] = cell
#   return dictionary
	return dictionarySurvey
# print csvtodict('events.csv')
dictionarySurvey = csvtodict("survey.csv")
print "\ndictionarySurvey is", dictionarySurvey


def csvtodict(all):
	with open("all_employees.csv", "r") as csv_file2:
		text = csv_file2.read().strip().split("\n")
	header_row = text[0].split(",")

	dictionary = {}
	for row, line in enumerate(text[1:]):
		dictionary[row] = {}
		for col, cell in enumerate(line.split(",")):
			dictionary[row][header_row[col]] = cell
	return dictionary
dictionaryAll = csvtodict("all_employees.csv")
print "\ndictionaryAll is", dictionaryAll


#loop through dictionarySurvey, tell Python if email (key)'s value matches an email's value in dictionaryAll, then print dictionaryAll's whole value.

with open ("appended_survey.csv", "w") as appended_survey:
	append_survey_dict = {}
	
	for key, info in dictionaryAll.items():#items() now works like iteritems() in Python 2
		#print "info",info #I see white space in ' email' and other sub keys or "labels" so I'll use .strip()
		emailFromAll = {}
		strippedLabelsAndDetails = []
		for labelFromAll, details in info.items():
			strippedLabelsAndDetails.append(labelFromAll.strip())
		strippedLabelsAndDetails[4] = emailFromAll
		#print strippedLabelsAndDetails[4]
		print emailFromAll
	
	for key, info in dictionarySurvey.items():#items() now works like iteritems() in Python 2
		#print "info",info #I see white space in ' email' and other sub keys or "labels" so I'll use .strip()
		emailFromSurvey = {}
		strippedLabelsAndDetails = []
		for labelFromSurvey, details in info.items():
			strippedLabelsAndDetails.append(labelFromSurvey.strip())
		strippedLabelsAndDetails[1] = emailFromSurvey
		#print strippedLabelsAndDetails[1]
	

		# individual_info = {}
		# if dictionarySurvey.get(emailFromAll):#.get() returns a value for the given key. If key is not available, then returns default value None.
		# 	print "\n{0} took the survey! Here is her contact information:".format(dictionaryAll.get(labelFromAll).get("name"))#.get("name"))
		# 	print "Twitter: {0}".format(survey_dict.get(email).get("twitter"))
		# 	print "Github: {0}".format(survey_dict.get(email).get("github"))
		# 	print "Phone: {0}".format(emp_dict.get(email).get("phone"))
		# 	single_emp_info["name"]=info.get("name")
		# 	single_emp_info["email"]=email
		# 	single_emp_info["phone"]=info.get("phone")
		# 	single_emp_info["department"]=info.get("department")
		# 	single_emp_info["position"]=info.get("position")
		# 	single_emp_info["twitter"]=survey_dict.get(email).get("twitter")
		# 	single_emp_info["github"]=survey_dict.get(email).get("github")



# for key, value in dictionarySurvey.items():
# 	print key, value #printed the following:
# # # 0 {' github': '@shannonturner', 'email': 'shannon@ijustworkhe.re', ' twitter': '@svt827'}
# # # 1 {' github': '@bey', 'email': 'beyonce@beyonce.com', ' twitter': '@beyonce'}
# # # 2 {' github': '@bubblegum', 'email': 'pb@candykingd.om', ' twitter': '@pbg'}
# # # 3 {' github': '@maddowshow', 'email': 'rachel@maddow.com', ' twitter': '@maddow'}

# # for value in dictionarySurvey.values():
# #  	print value #printed the following:
# # {' github': '@shannonturner', 'email': 'shannon@ijustworkhe.re', ' twitter': '@svt827'}
# # {' github': '@bey', 'email': 'beyonce@beyonce.com', ' twitter': '@beyonce'}
# # {' github': '@bubblegum', 'email': 'pb@candykingd.om', ' twitter': '@pbg'}
# # {' github': '@maddowshow', 'email': 'rachel@maddow.com', ' twitter': '@maddow'}
# 	#value = {}
# 	for label, details in value.items():
# 		print label #printed the following four times down the console:
# #  github
# # email
# #  twitter
# #  github









