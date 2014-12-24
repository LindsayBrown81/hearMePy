# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
breadSlice = 6
jellyBlob = 0
pbBlob = 3

weHaveASandwich = breadSlice >= 2 and jellyBlob >=1 and pbBlob >=1

if weHaveASandwich == True:
	print "Goal 1: Can I make a classic sandwich? Answer: {0}".format(weHaveASandwich)
else:
	print "Goal 1: Can I make a classic sandwich? Answer: Not enough ingredients for a classic sandwich."

if breadSlice == 0:
	print "Goal 1: Can I make a classic sandwich? Answer: I can't make any type of sandwich without bread, but if I find a spoon, I can eat out of the jar."
else:
	print "Goal 1: Can I make a classic sandwich? Answer: I could make a partial sandwich."


# Second Goal: Modify that program to tell you: if you can make a classic sandwich, how many you can make
noOfSandwich = min(breadSlice/2,jellyBlob,pbBlob)
if weHaveASandwich == True:
	#noOfSandwich = min(breadSlice/2,jellyBlob,pbBlob)
	print "Goal 2: How many classic sandwiches can I make? Answer: {0}".format(noOfSandwich)
else:
	print "Goal 2: N/A How many classic sandwiches can I make? Answer: Zero, because I don't have the ingredients to make a classic sandwich."



# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
if breadSlice%2!=0:
	if jellyBlob>=1 or pbBlob>=1:
		print "Goal 3: Can I make an open-faced sandwich? Answer: Yes, I can make an open-faced sandwich."
else:
	print "Goal 3: N/A Can I make an open-faced sandwich? Answer: No, I can't make an open-faced sandwich."

#~I gave myself extra challenge for goal 3:
#noOfSandwich = min(breadSlice/2,jellyBlob,pbBlob)#Why did I need to redefine this variable again in order for the program to keep running? B/c I indented it above originally
if breadSlice%2==1:
	if jellyBlob>=1 or pbBlob>=1:
		opnfSandwich = min( (noOfSandwich&breadSlice),max(jellyBlob-noOfSandwich,pbBlob-noOfSandwich) )#this line doesn't work if breadSlice > 7, or jellyBlob = 0
		if opnfSandwich != 1:
			plural = "es"
		else:
			plural = ""
		print "Goal 3 Bonus: How many open-faced sandwiches? Answer: I can make {0} open-faced sandwich{1}.".format(opnfSandwich, plural)

pbOpnfSandwich = min((breadSlice-(noOfSandwich*2)),(pbBlob-noOfSandwich)) 
if pbOpnfSandwich > 1:
	plural = "es"
else:
	plural = ""

if pbOpnfSandwich < 1:
	str(pbOpnfSandwich)
	pbOpnfSandwich = "not a single"
print "Goal 3 Bonus: What types of open-faced sandwich? Answer: Type PB: I can make {0} peanut butter open-faced sandwich{1}.".format(pbOpnfSandwich, plural)

jellyOpnfSandwich = min((breadSlice-(noOfSandwich*2)),(jellyBlob-noOfSandwich)) 
if jellyOpnfSandwich > 1:
	plural = "es"
else:
	plural = ""	

if jellyOpnfSandwich < 1:
	str(jellyOpnfSandwich)
	jellyOpnfSandwich = "not a single"
print "Goal 3 Bonus: What types of open-faced sandwich? Answer: Type Jelly: I can make {0} jelly open-faced sandwich{1}.".format(jellyOpnfSandwich, plural)


# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your ~open-faced sandwiches
print "Goal 4: What missing ingredients do I need to buy to make more open-faced sandwiches?"
#~I wish Python could return the variable name as a string, but Python doesn't do that well, or so I've read on stackoverflow. "A cat can't tell you its own name - someone else would need to tell you the cat's name.""

if breadSlice%2 == 0 and noOfSandwich%jellyBlob == 0 and noOfSandwich%pbBlob == 0:
	print "Buy more of everything."
else:
	lowest=min(breadSlice-(noOfSandwich*2), pbBlob-noOfSandwich, jellyBlob-noOfSandwich)
	plentiful=max(breadSlice-(noOfSandwich*2), pbBlob-noOfSandwich, jellyBlob-noOfSandwich)
	#nextLowest=median(breadSlice, pbBlob, jellyBlob) #~I would need to define median somewhere above or below. I don't know how to do that mathematically. So I'll try a workaround.
	#print nextLowest
	#nextLowest=plentiful%lowest I have no idea how to define this "nextLowest" variable
	#print nextLowest

	if lowest == breadSlice-(noOfSandwich*2) and plentiful == pbBlob-noOfSandwich:
		print "breadSlice is lowest at {0}".format(breadSlice-(noOfSandwich*2))
		print "jellyBlob is next lowest at {0}".format(jellyBlob-noOfSandwich)
		print "pbBlob is most plentiful at {0}".format(pbBlob-noOfSandwich)
		print "Goal 4 Answer: I should buy {0} more breadSlices and a little more jelly so I can make more open-faced sandwiches.".format(plentiful-lowest)

	elif lowest == breadSlice-(noOfSandwich*2) and plentiful == jellyBlob-noOfSandwich:
		print "breadSlice is the lowest at {0}".format(breadSlice-(noOfSandwich*2))
		print "pbBlob is the next lowest at {0}".format(pbBlob-noOfSandwich)
		print "jellyBlob is most plentiful at {0}".format(jellyBlob-noOfSandwich)
		print "Goal 4 Answer: I should buy {0} more breadSlices and a little more pb so I can make more open-faced sandwiches.".format(plentiful-lowest)

	elif lowest == pbBlob-noOfSandwich and plentiful == jellyBlob-noOfSandwich:
		print "pbBlob is lowest at {0}".format(pbBlob-noOfSandwich)
		print"breadSlice is next lowest at {0}".format(breadSlice-(noOfSandwich*2))
		print "jellyBlob is most plentiful at {0}".format(jellyBlob-noOfSandwich)
		print "Goal 4 Answer: I should buy {0} more pbBlobs and a small loaf of bread so I can make more open-faced sandwiches.".format(plentiful-lowest)

	elif lowest == pbBlob-noOfSandwich and plentiful == breadSlice-(noOfSandwich*2):
		print "pbBlob is the lowest at {0}".format(pbBlob-noOfSandwich)
		print "jellyBlob is the next lowest at {0}".format(jellyBlob-noOfSandwich)
		print "breadSlice is most plentiful at {0}".format(breadSlice-(noOfSandwich*2))
		print "Goal 4 Answer: I should buy {0} more pbBlobs and a little more jelly so I can make more open-faced sandwiches.".format(plentiful-lowest)


	elif lowest == jellyBlob-noOfSandwich and plentiful == pbBlob-noOfSandwich:
		print "jellyBlob is the lowest at {0}".format(jellyBlob-noOfSandwich)
		print "breadSlice is the next lowest at {0}".format(breadSlice-(noOfSandwich*2))
		print "pbBlob is most plentiful at {0}".format(pbBlob-noOfSandwich)
		print "Goal 4 Answer: I should buy {0} more jellyBlobs and a small loaf of bread so I can make more open-faced sandwiches.".format(plentiful-lowest)


	elif lowest == jellyBlob-noOfSandwich and plentiful == breadSlice-(noOfSandwich*2):
		print "jellyBlob is the lowest at {0}".format(jellyBlob-noOfSandwich)
		print "pbBlob is the next lowest at {0}".format(pbBlob-noOfSandwich)
		print "breadSlice is the most plentiful at {0}".format(breadSlice-(noOfSandwich*2))
		print "Goal 4 Answer: I should buy {0} more jellyBlobs and a little more pb so I can make more open-faced sandwiches.".format(plentiful-lowest)


# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, or vice versa, that you can make a peanut butter sandwich or a jelly sandwich but then make a judgemental statement.
print "Goal 5: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, or vice versa, that you can make a peanut butter sandwich or a jelly sandwich but then make a judgemental statement."
if breadSlice>=2:
	if jellyBlob/(breadSlice/2)>=1:
		print "Goal 5: Can I make a jelly sandwich? Answer: Yes, I can make a jelly sandwich, but that's so weird."
		print "How many? Answer: {0}".format(min(jellyBlob,breadSlice/2))
	else:
		print "I can't even make one of those half-assed jelly sandwiches."
if breadSlice>=2:
	if pbBlob/(breadSlice/2)>=1:
		print "Goal 5: Can I make a peanut butter sandwich? Answer: Yes, I can make a peanut butter sandwich, but that's so weird."
		print "How many? Answer: {0}".format(min(pbBlob,breadSlice/2))
	else:
		print "I can't even make one of those half-assed peanut butter sandwiches."
else:
	print "I can make neither a peanut butter sandwich nor a jelly sandwich, but who wants to eat one of those anyway?"

#Run this pbj program through the shell to use raw_input. I navigated to cd hearMePy directory from within shell, typed python then a space then the name of this file and then I was able to run program and use raw-input through terminal
breadInquiry = raw_input("How many pieces of bread do I have left again?")
print breadInquiry







