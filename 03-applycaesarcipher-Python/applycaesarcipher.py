# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")

def fun_applycaesarcipher(msg, shift):
	cipher_text = ''
	letters = 'abcdefghijklmnopqrstuvwxyz'

	for m in msg:
		if not m.isalpha():
			letters += m
		else:
			pos = letters.index(m.lower())
			new_pos = pos + shift

			if new_pos < 0:
				new_pos += 26
			elif new_pos > 25:
				new_pos -= 26

			if m.islower():
				letters += letters[new_pos]
			elif m.isupper():
				letters += letters[new_pos].upper()
	return m