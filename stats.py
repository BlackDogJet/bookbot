def get_number_of_words(file_contents):
	words = file_contents.split()
	return len(words)

def number_of_each_character(words):
	each_character = {}
	new_words = words.lower()

	for i in new_words:		
		if i not in each_character:
			each_character.update({i:1})		
		else:
			num_char = each_character[i] + 1
			each_character.update({i:num_char})
	
	return each_character

def sort_on(items):
	return items["num"]
