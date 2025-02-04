phrase = str(input('Type a phrase here'))
letter_a = phrase.lower().count('a')
first_letter_a = phrase.lower().find('a')
last_letter_a  = phrase.lower().rfind('a')

print(phrase)
print(letter_a)
print(first_letter_a)
print(last_letter_a)