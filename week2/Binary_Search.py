import random
#import time

#start = time.time()
number = random.randint(1,1000000)
lownumber = 1
highnumber = 10000000
guess = round((highnumber + lownumber) / 2)
count = 1
while guess != number:
  if guess > number:
    if highnumber > guess:
      highnumber = guess
    print("The number is smaller than : " + str(guess))
  if guess < number:
    if guess > lownumber:
      lownumber = guess
    print("The number is bigger than : " + str(guess))
  guess = guess = round((highnumber + lownumber) / 2)
  count = count + 1
print("The number is : " + str(number))
print("guesses : " + str(count))

#end = time.time()

#print('passed:',end - start)