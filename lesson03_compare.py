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

#~then, i'll use an if/else statement if email == email, wait, this sounds like mapping/matching keys (emails) and their values, meaning I need to create two dicts.
#Or do I? ~~~Can't I search for matching values between two lists using keyword, in? The in keyword allows you to check whether a value exists in the list
#From within allEmailList, I might ask, is "value" in surveyEmailList? If False, then surveyEmailList.append("value")
#list.append() adds an item to the end. If I work with index positions, say, is [index][0]==. Wait, I don't want to work with indices.
#You know what? I think dicts were made for this type of key-value matching. Let's move forward with reading the csv files and getting their content into two dicts.

# code below shows function on how to create dicts from reading csv files. source: https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/csv_to_dict.py
#~line by line, I pasted first Shannon's, then Anupama,s, then my own

# def csvtodict(filename):
def csvtodict(csv_file, k):
##	with open(filename, 'r') as csv_file:#shan's function incorporates with open statement
#										 #anu's function skips with open statement
#	~Like Anu's, I will write one generic function that will be reusable in all with open, read statements from which we create dicts. I like the descriptive key "email," rather than an index number.

##  	text = csv_file.read().strip().split('\n') 	#Shan's is indented here
#	lines = csv_file.read().split("\n") 			#Anu's is not indented here. Not much difference other than that, functionally.
	rows = csv_file.read().split("\n")

## 	header_row = text[0].split(',') 		#shan's saving header row to a var called header_row
#	for index, line in enumerate(lines):	#anu's enumerting all rows, including header
	for index, row in enumerate(rows): 

##	dict = {} 							#shan instantiates dict for entirety of csv's contents here
#		lines[index] = line.split(",")	#anu's is still formatting her csv's rows and columns
		rows[index] = row.split(",") 

##	for row, line in enumerate(text[1:]): 	#drilling down a level, shan's enumerating all rows below the header
	# 	stripped = [] 							#anu's stripping white space from all rows, lines 85-88
	# 	for item in lines[index]:					#~~~question: can't .strip() method be run on strings? why did she need to create a list?
	# 		stripped.append(item.strip())
	# 	lines[index] = stripped	
		stripped = []
		for item in rows[index]:
			stripped.append(item.strip())
		rows[index] = stripped
	
##	dict[row] = {} #shan initializes nested dict here
#	headers = lines.pop(0) #anu is making a list to store what will become the nested dict's keys
	headers = rows.pop(0)
	print "The headers are: ", headers

##	for col, cell in enumerate(line.split(',')): #shan's splitting the columns by ,'s
#	dict = {} #anu instantiates dict for entire csv contents here
	dict = {}

##	dict[row][header_row[col]] = cell 	#shan's divvying up the header row into columns
#	for line in lines: 					#anu's looping through all the rows in the csv
	for row in rows:

##	return dict 				#shan completes defining her function csvtodict		
#		single_line_dict = {}	#anu's loop will create nested dicts for each row
		single_row_dict = {}
#		for header, element in zip(headers, line):#anu's looping through headers and all lines and zips them into a list, returns what will become keys and values as strings
		for header, pair in zip(headers, row):
#			single_line_dict[header] = element #returns properties (key, value pairs, i.e., "labels" and "details") as dict
			single_row_dict[header] = pair
#			#print "single_line_dict",single_line_dict
		print "single_row_dict", single_row_dict #I chose to unindent print so wouldn't have to see every iteration of loop
#		dict[single_line_dict.get(k)] = single_line_dict
		dict[single_row_dict.get(k)] = single_row_dict
#	return dict #the dicts from both all_employees.csv and survey.csv use "email" as the main key rather than an index number. 
	return dict

# print csvtodict run on both file handlers:
with open("survey.csv", "r") as survey_file:#~I prefer double quotes. Also, quotes were needed around filename.
	dictSurvey = csvtodict(survey_file, "email")
	print "\ndictSurvey is", dictSurvey

with open("all_employees.csv", "r") as all_file:
	dictAll = csvtodict(all_file, "email")
	print "\ndictAll is", dictAll

# Reminder of Challenge 1: Open all_employees.csv and survey.csv and compare the two.  
# When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.
#~~Ok, I think I'll loop through dictSurvey, tell Python if email (key) matches an email in dictAll, then print/write dictAll's key and value to a new csv file.

with open ("write_survey.csv", "w") as write_survey:
	append_survey_dict = {}
	print "\nwrite_survey's info:"
	for email, info in dictAll.items(): #items() method works in Python 2 like iteritems() did in Python 1
#		print info
#		for label, details in info.items():
#			print label
		ind_info = {}
		if dictSurvey.get(email):#.get() returns a value for the given key. If key is not available, then returns default value None.
				print "\n{0} took the survey! Here is her contact information:".format(dictAll.get(email).get("name"))
		





		#emailFromAll = {}
		# for label, details in info.items():
		# 	print label
			# for dept, ph, pos, name, email in label.items():
			# 	print email
		# 	labelFromAll[4]= emailFromAll
		# print emailFromAll
		
		# for key, info in dictSurvey.items():#items() now works like iteritems() in Python 2
		# 	print "info",info #I see white space in ' email' and other sub keys or "labels" so I'll use .strip()
		# 	#emailFromSurvey = {}
		# 	for label, details in info.items():
		# 		print label
				# for twit, git, email in label.items():
				# 	print email
			# 	labelFromSurvey[1]=emailFromSurvey 
			# print emailFromAll
			
			
			# 	print "Twitter: {0}".format(survey_dict.get(email).get("twitter"))
			# 	print "Github: {0}".format(survey_dict.get(email).get("github"))
			# 	print "Phone: {0}".format(emp_dict.get(email).get("phone"))
			# 	ind_info["name"]=info.get("name")
			#	ind_info["email"]=email
			# 	ind_info["phone"]=info.get("phone")
			# 	ind_info["department"]=info.get("department")
			# 	ind_info["position"]=info.get("position")
			# 	ind_info["twitter"]=survey_dict.get(email).get("twitter")
			# 	ind_info["github"]=survey_dict.get(email).get("github")
			# else:
	 	# 		print "else nothing"
			# #	ind_info["email"]=email
			# # 	ind_info["phone"]=info.get("phone")
			# # 	ind_info["department"]=info.get("department")
			# # 	ind_info["position"]=info.get("position")
			# # 	ind_info["twitter"]=""
			# # 	ind_info["github"]=""
			# append_survey_dict[key]=ind_info



# for key, value in dictSurvey.items():
# 	print key, value #printed the following:
# # # 0 {' github': '@shannonturner', 'email': 'shannon@ijustworkhe.re', ' twitter': '@svt827'}
# # # 1 {' github': '@bey', 'email': 'beyonce@beyonce.com', ' twitter': '@beyonce'}
# # # 2 {' github': '@bubblegum', 'email': 'pb@candykingd.om', ' twitter': '@pbg'}
# # # 3 {' github': '@maddowshow', 'email': 'rachel@maddow.com', ' twitter': '@maddow'}

# # for value in dictSurvey.values():
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









