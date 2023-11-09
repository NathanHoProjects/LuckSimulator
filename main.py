import random #Imports random module
#Counters used to break out of loops
count = 0
def rolling(rolls, Banner): #Rolling variable
  roll = 0 #Value set to break out of loop
  #Four variables below are used to count how many times each item is rolled
  L = 0
  SR = 0
  R = 0
  C = 0
  CRoll = 0
  #Lists separated by rarity, containing items that will be randomly chosen within those rarities
  LCharacters = ['Lcharacter1', 'Lcharacter2', 'LCharacter3', 'LCharacter4', 'LCharacter5', 'LCharacter6']
  SRCharacters = ['SRCharacter1', 'SRCharacter2', 'SRCharacter3', 'SRCharacter4', 'SRCharacter5', 'SRCharacter6']
  RCharacters = ['RCharacter1', 'RCharacter2', 'RCharacter3', 'RCharacter4', 'RCharacter5', 'RCharacter6']
  CCharacters = ['CCharacter1', 'CCharacter2', 'CCharacter3', 'CCharacter4', 'CCharacter5', 'CCharacter6']
  
  LItems = ['LItem1', 'LItem2', 'LItem3', 'LItem4']
  SRItems = ['SRItem1', 'SRItem2', 'SRItem3', 'SRItem4']
  RItems = ['RItem1', 'RItem2', 'RItem3', 'RItem4']
  CItems = ['CItem1', 'CItem2', 'CItem3', 'CItem4']

  
  while roll < int(rolls): #While the amount of rolls is less than the amount specified by user, the program repeats
    #Value that was rolled
    rarity = random.randrange(0, 100)
    if rarity == 1: #If the number that was rolled is equal to 1, add 1 value to legendary. Also add one to total rolls
      L = L + 1
      roll = roll + 1
    if rarity in range(2, 5): #If the number that was rolled is between 2-5, add 1 value to Super rare. Also add 1 to total rolls
      SR = SR + 1
      roll = roll + 1
    if rarity in range(6, 30): #If the number that was rolled is between 6-30, add 1 value to Rares. Also add 1 to total rolls
      R = R + 1
      roll = roll + 1
    if rarity in range(31, 100): #If the number that is rolled is 31-100, add 1 value to Commons. Also add 1 to total rolls
      C = C + 1
      roll = roll + 1
 #Prints out the value for each of them along with rarity
  print()
  print('Legendaries:', str(L))
  print('Super Rares:', str(SR))
  print('Rares:', str(R))
  print('Commons:', str(C))
  print()
  #Picks random element from the list chosen, and lists it
  if Banner == 'character':
    print('Legendary Characters Obtained')
    while CRoll < L:
      print(random.choice(LCharacters))
      CRoll = CRoll + 1
    print()
    CRoll = 0
    #Picks random character from specified list, then prints until all characters for that rarity are decided for
    print('Super Rare Characters Obtained')
    while CRoll < SR:
      print(random.choice(SRCharacters))
      CRoll = CRoll + 1
    CRoll = 0
    print()
    #Picks random character from specified list, then prints until all characters for that rarity are decided for
    print('Rare Characters Obtained')
    while CRoll < R:
      print(random.choice(RCharacters))
      CRoll = CRoll + 1
    CRoll = 0
    print()
    #Picks random character from specified list, then prints until all characters for that rarity are decided for
    print('Common Characters Obtained')
    while CRoll < C:
      print(random.choice(CCharacters))
      CRoll = CRoll + 1
    CRoll = 0
    print()
  elif Banner == 'item':
    print('Legendary Items Obtained')
    while CRoll < L:
      print(random.choice(LItems))
      CRoll = CRoll + 1
    print()
    CRoll = 0
    #Picks random item from specified list, then prints until all item for that rarity are decided for
    print('Super Rare Items Obtained')
    while CRoll < SR:
      print(random.choice(SRItems))
      CRoll = CRoll + 1
    CRoll = 0
    print()
    #Picks random item from specified list, then prints until all item for that rarity are decided for
    print('Rare Items Obtained')
    while CRoll < R:
      print(random.choice(RItems))
      CRoll = CRoll + 1
    CRoll = 0
    print()
    #Picks random item from specified list, then prints until all item for that rarity are decided for
    print('Common Items Obtained')
    while CRoll < C:
      print(random.choice(CItems))
      CRoll = CRoll + 1
    CRoll = 0
    print()

print('Feeling down on your luck?')
print('Luck Tester:')
print()
print('Rates:')
print('Legendary: 1%')
print('Super rare: 4%')
print('Rare: 25%')
print('Common: 70%')
print() 



#Other group member coded everything above

while count == 0:
  print('Enter the amount of times you would like to roll, as a positive digit. (MAX ROLLS IS 15)')
  rolls = input() #Stores user's roll amount into variable
  #Checks if the user entered a number. If they did, it exits the program, forcing them to rerun.
  if rolls.isdigit() == False or int(rolls) > 15: #Keeps rerunning program until user provided digit which is less than 15
    print()
    print('That is not a valid answer, please try again.')
    print('You must enter a DIGIT that is 15 OR LESS.')
    print()
  else:
    count = count + 1
count = 0
#Stores the users banner amount into a variable
while count == 0:
  print()
  print('Which banner would you like to summon on?')
  print('Enter "Item" or "Character".')
  banner = input().casefold()
  #Checks if the response they give is valid
  if banner == 'item' or banner == 'character':
    count = count + 1
  else:
    print('Sorry, that is not a valid response. Please try again.')
    print()

rolling(rolls, banner) #Uses procedure, previously mentioned

#variables used for while loop
count = 0
countt = 0
#If user were to provide an invalid response, it would reloop. You ask the user if they would like to summon on the other banner or not. 
while count == 0:
  print('Would you like to roll on the other banner? Answer with "Yes", or "No".')
  answer = input().casefold()
  if answer == 'yes':
    count = count + 1
    print()
  elif answer == 'no':
    count = count + 1
    countt = countt + 1
    print()
    print('Thank you for using luck tester.')
  elif answer != 'yes' or answer != 'no':
    print('That is not a valid response. Please try again.')
    print()

#Same as before
while countt == 0:
  print('Enter the amount of times you would like to roll, as a positive digit. (MAX ROLLS IS 15)')
  rolls = input() #Stores user's roll amount into variable
  #Checks if the user entered a number. If they did, it exits the program, forcing them to rerun.
  if rolls.isdigit() == False or int(rolls) > 15: #Keeps rerunning program until user provided digit which is less than 15
    print()
    print('That is not a valid answer, please try again.')
    print('You must enter a DIGIT that is 15 OR LESS.')
    print()
  else:
    countt = countt + 1

#If statement which checks which banner they summoned on previously.
if answer == 'yes':
  if banner == 'character':
    rolling(rolls, 'item')
  elif banner == 'item':
    rolling(rolls, 'character')
  print('Thank you for using luck tester.')
