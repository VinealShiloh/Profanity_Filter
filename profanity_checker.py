from profanity_check import predict, predict_prob

file_location = open (Random.txt)

#Reads the file 
content_of_file = file_location.read()

#Finds the profanity of the text file
print(predict([content_of_file]))

#Finds the profanity of a file
print(predict_prob([content_of_file]))

#Test line to find the profanity of a sentence
#print(predict_prob(['hi guys im a bad boy','shutup you kid','welcome to python programming','checking profanity of the text file']))

file_location.close()
