print "\nWelcome to the list-memoriser thingy. Look at the 'before' and 'after' line and try to remember what the blanked-out line should be. Then, when you're ready, move on to another line from the text."

demo_list = ["He would declare and could himself believe", "that the birds there in all the garden round", "from having heard the daylong voice of Eve", "had added to their own an oversound", "her tone of meaning but without the words", "admittedly an eloquence so soft", "could only have had an influence on birds", "when call or laughter carried it aloft"]

from random import randint

def new_line():

	random_number = randint(0,len(demo_list) - 1)

	try:
		pre_line = demo_list[random_number - 1]
	except IndexError:
		pre_line ="START OF LIST"

	try:
		post_line = demo_list[random_number + 1]
	except IndexError:
		post_line ="END OF LIST"

	blank_filler = "-" * len((demo_list[random_number]))

	print "\n"
	print pre_line
	print blank_filler
	print post_line
	print "\n"

	get_another = raw_input("another? press 'y' for yes or 'q' to quit \n")

	if get_another == "y":
		new_line()
	elif get_another == "q":
		quit()

new_line()