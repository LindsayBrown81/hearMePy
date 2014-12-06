# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
breadSlice = 7
jellyBlob = 8
pbBlob = 3

weHaveASandwich = breadSlice >= 2 and jellyBlob >=1 and pbBlob >=1

if weHaveASandwich == True:
	print "Goal 1: Can I make a classic sandwich? Answer: {0}".format(weHaveASandwich)
else:
	print "Not enough ingredients for a classic sandwich."


# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make
if weHaveASandwich == True:
	noOfSandwich = min(breadSlice/2,jellyBlob,pbBlob)
	print "Goal 2: How many classic sandwiches can I make? Answer: {0}".format(noOfSandwich)
else:
	print "I can make a partial sandwich then."

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
if breadSlice%2>0:
	if jellyBlob>=1 or pbBlob>=1:
		print "Goal 3: Can I make an open-faced sandwich? Answer: Yes, I can make an open-faced sandwich."
else:
	print "I can't make an open-faced sandwich"
#~I gave myself extra challenge for goal 3:
print "Goal 3 bonus: How many open-faced sandwiches and what types?"
if breadSlice%2>0:
	opnfSandwich = max((jellyBlob-noOfSandwich),(pbBlob-noOfSandwich))-(breadSlice-noOfSandwich)
	if opnfSandwich != 1:
		plural = "es"
	else:
		plural = ""
print "I can make {0} open-faced sandwich{1}.".format(opnfSandwich, plural)

pbOpnfSandwich = min((breadSlice-(noOfSandwich*2)),(pbBlob-noOfSandwich)) 
if pbOpnfSandwich > 1:
	plural = "es"
else:
	plural = ""

if pbOpnfSandwich < 1:
	str(pbOpnfSandwich)
	pbOpnfSandwich = "not a single"
print "Goal 3 Embellished Answer: I can make {0} peanut butter open-faced sandwich{1}.".format(pbOpnfSandwich, plural)

jellyOpnfSandwich = min((breadSlice-(noOfSandwich*2)),(jellyBlob-noOfSandwich)) 
if jellyOpnfSandwich < 1:
	str(jellyOpnfSandwich)
	jellyOpnfSandwich = "not a single"

	if jellyOpnfSandwich > 1:
		plural = "es"
	else:
		plural = ""	
print "Goal 3 Embellished Answer: I can make {0} jelly open-faced sandwich{1}.".format(jellyOpnfSandwich, plural)

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your ~open-faced~sandwiches
print "Goal 4: What missing ingredients do I need to buy to make more open-faced sandwiches?"
goBuyLowest=max(breadSlice, pbBlob, jellyBlob)-min(breadSlice, pbBlob, jellyBlob)
#~I wish Python could tell me what the variable name is, but Python doesn't do that well, or so I've read on stackoverflow.
#inMiddle=median(breadSlice, pbBlob, jellyBlob) #~I would need to define median somewhere above or below. I don't know how to do that mathematically. So I'll try a workaround.
#print nextLowest
#inMiddle=plentiful%lowest I have no idea how to define this "inMiddle" variable
#print nextLowest
lowest=min(breadSlice, pbBlob, jellyBlob)
plentiful=max(breadSlice, pbBlob, jellyBlob)


if breadSlice == min(breadSlice, pbBlob, jellyBlob) and pbBlob == max(breadSlice, pbBlob, jellyBlob):
	print "breadSlice is lowest at {0}".format(lowest)
	print "jellyBlob is next lowest\npbBlob is most plentiful at {0}".format(plentiful)
	print "Goal 4 Answer: I should buy {0} more breadSlices and a little more jelly so I can make more open-faced sandwiches.".format(goBuyLowest)
elif breadSlice == min(breadSlice, pbBlob, jellyBlob) and jellyBlob == max(breadSlice, pbBlob,jellyBlob):
	print "breadSlice is the lowest at {0}".format(lowest)
	print "pbBlob is the next lowest\njellyBlob is most plentiful at {0}".format(plentiful)
	print "Goal 4 Answer: I should buy {0} more breadSlices and a little more pb so I can make more open-faced sandwiches.".format(goBuyLowest)
elif pbBlob == min(breadSlice, pbBlob, jellyBlob) and jellyBlob == max(breadSlice, pbBlob, jellyBlob):
	print "pbBlob is lowest at {0}".format(lowest)
	print"breadSlice is next lowest\njellyBlob is most plentiful at {0}".format(plentiful)
	print "Goal 4 Answer: I should buy {0} more pbBlobs and a small loaf of bread so I can make more open-faced sandwiches.".format(goBuyLowest)
elif pbBlob == min(breadSlice, pbBlob, jellyBlob) and breadSlice == max(breadSlice, pbBlob, jellyBlob):
	print "pbBlob is the lowest at {0}".format(lowest)
	print "jellyBlob is the next lowest\nbreadSlice is most plentiful at {0}".format(plentiful)
	print "Goal 4 Answer: I should buy {0} more pbBlobs and a little more jelly so I can make more open-faced sandwiches.".format(goBuyLowest)
elif jellyBlob == min(breadSlice, pbBlob, jellyBlob) and pbBlob == max(breadSlice,pbBlob, jellyBlob):
	print "jellyBlob is the lowest at {0}.".format(lowest)
	print "breadSlice is the next lowest\npbBlob is most plentiful at {0}".format(plentiful)
	print "Goal 4 Answer: I should buy {0} more jellyBlobs and a small loaf of bread so I can make more open-faced sandwiches.".format(goBuyLowest)
else: #jellyBlob == min(breadSlice, pbBlob, jellyBlob) and breadSlice == max(breadSlice, pbBlob, jellyBlob):
	print "jellyBlob is the lowest at {0}".format(lowest)
	print "pbBlob is the next lowest\nbreadSlice is the most plentiful at {0}".format(plentiful)
	print "Goal 4 Answer: I should buy {0} more jellyBlobs and a little more pb so I can make more open-faced sandwiches.".format(goBuyLowest)

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, or vice versa, that you can make a peanut butter sandwich or a jelly sandwich but then make a judgemental statement.
print "Goal 5: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, or vice versa, that you can make a peanut butter sandwich or a jelly sandwich but then make a judgemental statement."





