import unittest

from src.automata.dfa import dfa
from src.validator.validator import Validator


class ValidatorTestCases(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.validator = Validator(dfa)

	def assertAccepted(self, code):
		result = self.validator.validate_code(code)
		self.assertTrue(result["accepted"], msg=result)
		self.assertEqual(result["final_state"], "{q24}")

	def assertRejected(self, code):
		result = self.validator.validate_code(code)
		self.assertFalse(result["accepted"], msg=result)

	# Mga tanggap
	def test_accepts_cs_code(self):
		self.assertAccepted("GG-CS-25-ABC-R01-A")

	def test_accepts_is_code(self):
		self.assertAccepted("GG-IS-29-0123C-R20-B")

	def test_accepts_it_code(self):
		self.assertAccepted("GG-IT-26-9999-R10-C")

	# Rejects	
	def test_rejects_year_below_25(self):
		self.assertRejected("GG-CS-24-ABC-R01-A")

	def test_rejects_year_above_29(self):
		self.assertRejected("GG-CS-30-ABC-R01-A")

	def test_rejects_payload_that_is_too_short(self):
		self.assertRejected("GG-CS-25-AB-R01-A")
		
	def test_rejects_payload_that_is_too_long(self):
		self.assertRejected("GG-CS-25-ABC123-R01-A")

	def test_rejects_invalid_r_number(self):
		self.assertRejected("GG-CS-25-ABC-R00-A")

	def test_rejects_invalid_final_letter(self):
		self.assertRejected("GG-CS-25-ABC-R01-D")
		
	def test_rejects_missing_hyphen(self):
		self.assertRejected("GGCS-25-ABC-R01-A")

	def test_rejects_double_hyphen(self):
		self.assertRejected("GG--CS-25-ABC-R01-A")
		
	def test_rejects_spaces_in_code(self):
		self.assertRejected("GG- CS-25-ABC-R01-A")

	# Invalid Alphabet
	def test_rejects_lowercase_symbol(self):
		result = self.validator.validate_code("gg-CS-25-ABC-R01-A")
		self.assertFalse(result["accepted"])
		self.assertEqual(result["final_state"], "INVALID SYMBOL")

	def test_rejects_punctuation_symbol(self):
		result = self.validator.validate_code("GG-CS-25-ABC-R01-!")
		self.assertFalse(result["accepted"])
		self.assertEqual(result["final_state"], "INVALID SYMBOL")

	# Input test
	def test_evaluates_multiple_inputs_independently(self):
		scenarios = {
			"GG-CS-25-ABC-R01-A": True,
			"GG-IS-29-0123C-R20-B": True,
			"GG-CS-24-ABC-R01-A": False,
			"GG-CS-25-AB-R01-A": False,
		}

		for code, expected in scenarios.items():
			with self.subTest(code=code):
				self.assertEqual(
					self.validator.validate_code(code)["accepted"], expected
				)

	# Results
	def test_empty_input_starts_at_q0(self):
		result = self.validator.validate_code("")
		self.assertFalse(result["accepted"])
		self.assertEqual(result["final_state"], "{q0}")
		self.assertEqual(result["transitions"], [])


if __name__ == "__main__":
	unittest.main()
