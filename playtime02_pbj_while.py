# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.


breadSlice = 6
pbBlob = 3
jellyBlob = 3

#weHaveASandwich = breadSlice >= 2 and pbBlob >=1 and jellyBlob >=1 #in playtime01_pbj.py, I assigned value to this var like this

weHaveASandwich = 0

while breadSlice >= 2 and pbBlob >= 1 and jellyBlob >= 1: #in this exercise, I'm assigning value to sandwich var like this instead
	print "Making sandwich number {0}".format(weHaveASandwich+1)
	breadSlice = breadSlice-2
	pbBlob = pbBlob-1
	jellyBlob =jellyBlob-1
	weHaveASandwich=weHaveASandwich+1

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

print "Making sandwich {0}, enough jelly for {1} more, enough pb for {2} more, enough bread for {3} more".format(weHaveASandwich,jellyBlob,pbBlob,breadSlice/2)
breadSlice = breadSlice-2
pbBlob = pbBlob-1
jellyBlob =jellyBlob-1
weHaveASandwich=weHaveASandwich+1

if breadSlice<2:
    print "not enough bread left"
if pbBlob<1:
    print "outta peanut butter"
if jellyBlob<1:
    print "outta jelly"


