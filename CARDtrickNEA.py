import random
first_pile= []
second_pile = []
third_pile  = []


def the_deck():
  global deck
  
  classes = ["heart","clubs","diamond","spades"]
  deck = []
  numbers = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
  while(len(deck) < 21):
    randomclass = random.choice(classes)
    randomnumbers = random.choice(numbers)
    if randomnumbers + randomclass not in deck:
         
      deck.append(randomnumbers + randomclass)
  
def sorting(a):
  for x in range(0,21,3):
    first_pile.append(a[x])
    second_pile.append(a[x+1])
    third_pile.append(a[x+2])
  
  print("first pile:", first_pile)
  print("\n")
  print("second pile:", second_pile)
  print("\n")
  print("third pile:", third_pile)
  


the_deck()
sorting(deck)




choice = int(input("which pile was your card in? "))
print("\n")
if choice == 1:
  deck = second_pile  +first_pile + third_pile
  first_pile= []
  second_pile = []
  third_pile  = []
  sorting(deck)
  
  
  
  
  
elif choice == 2:
  deck = first_pile + second_pile + third_pile
  first_pile= []
  second_pile = []
  third_pile  = []
  sorting(deck)
  
  
else:
  deck = first_pile +third_pile + second_pile
  first_pile= []
  second_pile = []
  third_pile  = []
  sorting(deck)

choice = int(input("which pile was your card in? "))
if choice == 1:
  deck = second_pile  +first_pile + third_pile
  first_pile= []
  second_pile = []
  third_pile  = []
  sorting(deck)
  
  
  
  
elif choice == 2:
  deck = first_pile + second_pile + third_pile
  first_pile= []
  second_pile = []
  third_pile  = []
  sorting(deck)
  
  
else:
  deck = first_pile +third_pile + second_pile
  first_pile= []
  second_pile = []
  third_pile  = []
  sorting(deck)

choice = int(input("which pile was your card in? "))
if choice == 1:
  print(first_pile[3])
if choice == 2:
  print(second_pile[3])
if choice == 3:
  print(third_pile[3])




  
  
