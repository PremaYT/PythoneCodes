

#import random
#print("Please enter a number of ur guess... ")
#randnum = random.randint(1,10)
#for i in range(1,7):
#    guess = int(input())
#    if(guess > randnum):
#        print("Number is too big...")
#    elif(guess < randnum):
#        print("Number is too small
#    else:
#        break
#if(guess == randnum):
#   print("Congo you guessed number right in " + str(i) + " attempts")
#else:
   #print("the right number is " + str(randnum))



#eggs = {'name': 'Sophie', 'species':'cat', 'age': 8}
#print(list(eggs.items()))
#print(eggs.get('age',0))
#eggs.setdefault('color','black')
#print(eggs)

import pprint
message = "That was a quiet bright day and the clock was Set to thirteen.. "
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character]+=1

#pprint.pprint(count)
rjtext = pprint.pformat(count)
print(rjtext)