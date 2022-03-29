import random
r = random.randint(1,100)


while True:
	num = int(input('guess:'))
	if num == r:
		print('congrat')
		break
	elif num > r:
		print('so big')
	elif num < r:
		print('so small')