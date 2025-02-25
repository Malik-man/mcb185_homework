import random 

trial = 5
die = 0
stable = 0 
revive = 0

for i in range(1, trial + 1):
	print('trial', i)
	faliure = 0
	success = 0
	
	for j in range(5):
		r = random.randint(1,20)
		
		if r == 1: faliure += 2
		elif r <= 9: faliure += 1
		elif r <= 19: success += 1
		else: 
			revive += 1
			break
			
		if success == 3:
			stable += 1
			break
			
		if faliure >= 3:
			die += 1
			break 
			
total = die + stable + revive
prob_die = (die / total) * 100
prob_stable = (stable / total) * 100
prob_revive = (revive / total) * 100

print(prob_die)
print(prob_stable)
print(prob_revive)

		
		
		


	
