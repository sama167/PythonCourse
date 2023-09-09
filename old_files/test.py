forbidden_words = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
word=""
bad_words_couter = 0

while word != "End":
  if word in forbidden_words:
    bad_words_couter = bad_words_couter + 1
    print(f"You are not allowed to enter this word. You cannot do this more than {2 - bad_words_couter} times")
    print(" ",bad_words_couter)
    if bad_words_couter < 2:
      word = input("Enter a correct word ")
      continue
    else: 
      break

  print(word)#echo
  word = input("Enter a word ")


print("Ending the program...")

