import random
#import time

#start = time.time()

number = random.randint(1,1000000)
count = 0
for i in range(1,10000000):
  count = count + 1
  if i == number:
    print("The number is : " + str(number))
    print("guesses : " + str(count))
    break

#end = time.time()
#print('passed:',end - start)