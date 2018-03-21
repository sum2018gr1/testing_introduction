import unittest
from log_writer import LogWriter
import math

class MyTest(unittest.TestCase):

	def setUp(self):
		self.head_text = """
		The following list represents the total number of invisible unicorns in classroom.
		"""
		self.list_data = [1,2,3,4]
		self.test_instance = LogWriter(self.list_data, self.head_text)

	def test_init(self):
		self.assertEqual(self.test_instance.list_data, self.list_data)
		self.assertEqual(self.test_instance.head_text, self.head_text)

	def test_avg_every_second_element(self):
		self.assertEqual(LogWriter.avg_every_second_element([1,2,3,4]),3)

	def test_get_every_second_element(self):
		self.assertEqual(LogWriter.get_every_second_element([1,2,34,3]), [2,3])

	def test_insert_data_in_text(self):
		examplary_text = "silt kilst sliks klast list tilst liist"
		list_data = [1111, 11, 1111, 11, 111, 1]
		instance = LogWriter(list_data, examplary_text)
		new_text = instance.insert_data_in_text(examplary_text,list_data)
		self.assertEqual(new_text, "silt kilst sliks klast list ([1111, 11, 1111, 11, 111, 1]) tilst liist")

	def test_count_o(self):
		self.assertEqual(LogWriter.count_o("000ooo00ooo0o0"),7)
		self.assertEqual(LogWriter.count_o("oOooO"),5)

	def test_get_first_part(self):
		first_text_part, count = self.test_instance.get_first_part()
		self.assertEqual(count, 14)
		result_text= "\n\t\tThe following list represents the total number of invisible unicorns in classroom.\n\t\t_________\n After change: \n\n\t\tThe following list ([1, 2, 3, 4]) represents the total number of invisible unicorns in classroom.\n\t\t"
		self.assertEqual(result_text, first_text_part)

	def test_what_is_added_the_meaning_of_life(self):
		self.assertEqual(LogWriter.what_is_added_the_meaning_of_life(),math.sqrt(42))
		self.assertEqual(LogWriter.what_is_added_the_meaning_of_life(-6),6.0)
		
	def test_what_is_your_quest(self):
		self.assertEqual(LogWriter.what_is_your_quest(),"To seek the holy grail")
		self.assertEqual(LogWriter.what_is_your_quest("answers"),"To seek the answers")

	def test_get_second_word(self):
		self.assertEqual(LogWriter.get_second_word("To seek the holy grail"),"seek")
		self.assertEqual(LogWriter.get_second_word("answers to questions"),"to")

	def test_o_count_is_even(self):
		tmp = self.test_instance.o_count
		self.assertEqual(False, self.test_instance.o_count_is_even())
		self.test_instance.o_count += 1
		self.assertEqual(True, self.test_instance.o_count_is_even())
		self.test_instance.o_count -= 1

	def test_get_movie_reference(self):
		reference1 = self.test_instance.get_movie_reference()
		actual_reference1 = "To seek the following"
		self.assertEqual(reference1, actual_reference1)
		self.test_instance.o_count = 6
		reference2 = self.test_instance.get_movie_reference()
		actual_reference2 = str(math.sqrt(42+6))
		self.assertEqual(reference2, actual_reference2)
		self.test_instance.o_count = 8
		reference3 = self.test_instance.get_movie_reference()
		actual_reference3 = str(math.sqrt(42+8))+"\n"+"To seek the holy grail"
		self.assertEqual(reference3, actual_reference3)
		self.test_instance.o_count = 7

	def test_computation(self):
		comp_res = LogWriter.computation(3)
		self.assertEqual(math.sqrt(3)+9+math.sqrt(math.sqrt(3)), comp_res)

	def test_get_second_part(self):
		reference = self.test_instance.get_movie_reference()
		self.assertEqual(self.test_instance.get_second_part(), reference)
		self.assertEqual(
			self.test_instance.get_second_part(computation= lambda x: x+3), 
			reference+"\n"+str(50)
			)

	def test_combining_method(self):
		combined_text = self.test_instance.combining_method()
		total_text = "\n\t\tThe following list represents the total number of invisible unicorns in classroom.\n\t\t_________\n After change: \n\n\t\tThe following list ([1, 2, 3, 4]) represents the total number of invisible unicorns in classroom.\n\t\t0 O 0 O 0 O 0 O 0 O 0 O7.48331477355\nTo seek the holy grail\n2218.4739851"
		self.assertEqual(total_text, combined_text)