# Difficulty Level: Intermediate
# Goal: Create a program that prints out an HTML drop down menu for all 50 states ~See step 3. use option tag, a form control

# Step 1: Define your list of states ~and abbreviations, it seems~
# These should all be strings, since they're names of places
# Instead of having to type them all out, I really like liststates.com -- you can even customize the format it gives you the states in to make it super easy to copy/paste into your code here

states = "Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District Of Columbia, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming"

states_as_list = states.split(", ")
print "states_as_list: {0}\n".format(states_as_list)

#~Where did my classmates get their abbreviations? liststates.com doesn't have abbreviations. I fumbled with 'with open("states.csv", "r") as states_file:        
    #states = states_file.read().split("\r")' but couldn't separate Abb from State as they were coupled elements in each list item. I'll learn how later. 

abbs = "AL,AK,AZ,AR,CA,CO,CT,DE,DC,FL,GA,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VT,VA,WA,WV,WI,WY"

abbs_as_list = abbs.split(",")
print "abbs_as_list: {0}\n".format(abbs_as_list)

statesAndAbbs_List = zip(states_as_list,abbs_as_list)
print "statesAndAbbs_List by using .zip( ): {0}\n".format(statesAndAbbs_List)

# Step 2: Create your loop
# Essentially, you're telling Python: for each state in my list: print this ~later, HTML code~
# A good place to start is by printing the name of the state in the loop; after that you can add the HTML around it

for state, abb in statesAndAbbs_List:
	print state, abb

# Step 3: Add the HTML
# A drop-down menu in HTML looks like this:

#<select>
# 			<option value="state_abbreviation">Full state name</option>
#</select>

# At line 14 ~or 44~, we create the drop-down menu
# At line 15 ~or 45~, we create one drop-down item.  Each additional <option> that we add will add another item to our drop-down menu
# At line 16 ~or 46~, we tell HTML that we're done with the drop-down menu

#~WHOOPS! the 4 lines below created 50 different drop-down menus. ~Save for later. I could use that.
for state, abb in statesAndAbbs_List: 
	print "<select>" #FYI-you can print an html tag from python
	print "<option value={0}> {1} </option>".format(abb, state)
	print "</select>"

#~HMM. the 4 lines below suceeded in creating one drop-down with 50 options, but my abbs are not in quotes. ~Will that cause a problem?
print "<select>"
for state, abb in statesAndAbbs_List:
	print "<option value={0}>{1} </option>".format(abb, state)
print "<select>"

#~So I'll add the quotes around the abb values...
print "<select>"
for state, abb in statesAndAbbs_List:
	print "<option value='{0}'>{1} </option>".format(abb, state)


# Step 4: Test it!
# Have Python print out the HTML code. Copy / paste it into a file, save that file as "states.html" and open that file in a web browser.
#~I tested mine at http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select 
# Later, when we learn file handling, we can skip the copy/paste step.
# File handling can also let us create a file with the state names and abbreviations in it so we don't have to add it to our code.

# Your finished project should look something like: https://github.com/shannonturner/python-lessons/blob/master/section_05_(loops)/states.html
