from profanity_filter import ProfanityFilter

class Profanity_Filter():

	def check_profanity_filter_text():

		pf = ProfanityFilter()

		#Opens the text file from the given location.
		file_location = open('/yourfilelocation/filename.txt')

		# Opens the file. This line should be added when if your text file is in same location a program.
		#file_location = open('profanity.txt')
		
		#Read is a built in function of python to read files.
		content_of_file = file_location.read()
		
		#Censor is a built in function of ProfanityFilter package to check profanity of a sentence.
		text = pf.censor(content_of_file)
		
		#Prints the contents of the file where offensive words are marked by "*".
		print(text)

# Main function.
if __name__ == '__main__':
	Profanity_Filter.check_profanity_filter_text()
