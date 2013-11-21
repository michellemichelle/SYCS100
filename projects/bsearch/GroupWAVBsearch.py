#Hezekiah
#Michelle
def bsearch():
	find_name = raw_input ("input")
	first_element = 0
	last_element = len(List) - 1 
	found = False
	while first_element < last_element and found == False:
		middle_element = (int) ((first_element + last_element) / 2)
		if List[middle_element] < find_name:
			first_element = middle_element + 1
		elif List[middle_element] > find_name:
			last_element = middle_element
		else:
			found = True
	
	if found:
		print "the name is ", middle_element 
	else:
		print "-1"

bsearch()
#Sacha
#Eboni
#Ashanti
#Tyler
