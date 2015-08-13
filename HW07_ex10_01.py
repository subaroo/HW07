# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


list_a = [[1,2], 5, 7]


def nested_sum(list_a):
	'''
	Gets the sum of all the integers in a list (even nexted lists)
	'''
	list_sum = 0
	for entry in list_a:
		if type(entry) == list:
			list_sum = nested_sum(entry)
			print list_sum
		# else:
		# 	list_sum += entry	
	return list_sum







##############################################################################
def main():
	pass
    

if __name__ == '__main__':
    main()
