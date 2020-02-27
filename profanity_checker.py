from profanity_check import predict, predict_prob

file_location = open (Random.txt)

content_of_file = file_location.read()

print(predict([content_of_file]))


print(predict_prob(['hi guys im a bad boy','shutup you kid',
'welcome to python programming',
'checking profanity of the text file']))

