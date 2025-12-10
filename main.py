import sys
from stats import get_number_of_words, number_of_each_character, sort_on

def get_book_text(path_to_file):	
	with open(path_to_file) as f:
		file_contents = f.read()
	
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")

	file_contents = get_book_text(book_path)

	print("----------- Word Count ----------")

	number_of_words = get_number_of_words(file_contents)

	print(f"Found {number_of_words} total words")

	number_of_chars = number_of_each_character(file_contents)

	sort_this_list = []

	for char in number_of_chars:
		sort_this_list.append({"char":char, "num":number_of_chars[char]})

	sort_this_list.sort(reverse=True, key=sort_on)

	print("--------- Character Count -------")

	for sort in sort_this_list:
		if sort["char"].isalpha():
			print(f"{sort["char"]}: {sort["num"]}")

	print("============= END ===============")

main()