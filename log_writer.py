import math

class LogWriter(object):


	def __init__(self, list_data, head_text):
		#7
		#save list_data and head_text as members of this object
		# create member o_count with value None
		pass

	@staticmethod
	def get_every_second_element(data):
		#1
		# return every second element (counting from index 1) from passed list 
		# e.g. get_every_second_element([1,2,3,4]) == [2,4]
		pass

	@staticmethod
	def avg_every_second_element(data):
		#2
		#return the average of every second element 
		#(use function get_every_second_element )
		#e.g:
		# avg_every_second_element([1,2,3,4]) == 3.0
		pass

	@staticmethod
	def insert_data_in_text(text, data):
		#3
		#Find the occurance of word "list" in text (str).
		#Assume that word "list" does not repeat in text.
		#And put string form of data (str(data)) after that occurance.
		#String form of data should be surrounded with parentheses "()".
		#
		#e.g:
		# insert_data_in_text("AAAA list BBBB", [1,2,3]) = "AAAA list ([1, 2, 3]) BBBB"
		pass

	@staticmethod
	def count_o(text):
		#4
		#Count occurances of character 'o' in text
		#e.g.:
		# count_o("oOo0O00o") == 5
		pass

	def get_first_part(self):
		#5
		#append head_text (member of this object) with string
		#"_________" followed by "\n After change: \n"
		# append the output of insert_data_in_text applied 
		#on head_text and list_data (members of this object).
		#Set member o_count with number of o's in contained 
		# in text you created above - use count_o.
		# Return newly created text AND value of o_count
		pass

	@staticmethod
	def what_is_added_the_meaning_of_life(add):
		#6
		#return square root of 42 PLUS add
		# if add is not given return 42 
		#
		pass

	@staticmethod
	def what_is_your_quest(quest="holy grail"):
		#8
		# if the argument is not specified return "To seek the holy grail"
		# in other case append the texts "To seek the " with argument and return
		pass

	@staticmethod
	def get_second_word(text):
		#9
		# Return the second word of text
		pass

	def o_count_is_even(self):
		#10
		# return True if o_count is even
		# return False is o_count is odd
		pass

	def get_movie_reference(self):
		#11
		#this is the tough one
		#use o_count is even (use o_count_is_even())
		#If o_count is even set output of this function 
		#to value of what_is_added_the_meaning_of_life applied on o_count
		#If o_count is odd setoutput to be the value of what_is_your_quest applied on
		#the second word of head_text (member of this object).
		#Lastly if o_count is higher than seven append empty line and
		#empty call of what_is_your_quest to the output.
		#Return the output
		pass

	@staticmethod
	def computation(x):
		#12
		# return the the sum of:
		# x to the second power
		# square root of x
		# square root of the square root of x
		pass

	def get_second_part(self, computation=None):
		#13
		# append the:
		# - new line 
		# and 
		# - the value of function computation (in argument)
		# applied on number 47 
		# to the output of get_movie_reference
		pass

	def combining_method(self):
		#14
		#concatenate:
		# - text output from get_first_part
		# - string "0 O 0 O 0 O 0 O 0 O 0 O"
		# - output of get_second_part applied on computation method (class member)
		#return the concatenation
		pass

	def __str__(self):
		return self.combining_method()

if __name__=="__main__":
	head_text ="""
	Stil liist shilts list 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
	"""
	list_data = [1,2,34,4]
	test_instance = LogWriter(list_data, head_text)
	print(test_instance)

#
#examplary output is below
#
"""

Stil liist shilts list 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
_________
 After change: 

Stil liist shilts list ([1, 2, 34, 4]) 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
0 O 0 O 0 O 0 O 0 O 0 O7.34846922835
To seek the holy grail
2218.4739851
"""
