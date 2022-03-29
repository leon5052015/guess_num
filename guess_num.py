import random

r = random.randint(1,100)
count = 0

while True:
	count = count + 1
	num = int(input('guess:'))
	if num == r:
		print('congrat')
		break
	elif num > r:
		print('so big')
	elif num < r:
		print('so small')
	print(count,'次')