import enchant
dict = enchant.Dict("en_UK")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #Define Alphabet
remove_letters = ["s","t","a","i"]
included_letters = ["r","e","d","v"]
position_definite = ["d","r","","v","e"]

for letter in alphabet:
	for remove_letter in remove_letters:
		if remove_letter == letter:
			alphabet.remove(remove_letter)

for a in alphabet: #First Letter
	for b in alphabet: #Second Letter
		for c in alphabet: #Third Letter
			for d in alphabet: #Fourth Letter
				for e in alphabet: #Fifth Letter
					word = (a+b+c+d+e) #Create Word
					if dict.check(word): #Check Word
						correct = 1
						for check_included in included_letters:
							if not check_included in word:
								correct = 0
						for definite in range(0,len(position_definite)):
							if position_definite[definite] != "":
								if position_definite[definite] == word[definite-1:definite]:
									pass
								else:
									correct = 0

						if correct:
							print(word)

								
