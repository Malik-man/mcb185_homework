import random

def advantage():
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 > roll2: return roll1
	return roll2
	
def disadvantage():
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 < roll2: return roll1
	return roll2

def roll_saving_throws(trials, dc, modifier):
	success = 0
	

	for i in range(trials):
		if modifier == "normal":
			roll = random.randint(1,20)
		elif modifier == "advantage":
			roll = advantage()
		elif modifier == "disadvantage":
			roll = disadvantage()
		
		if roll >= dc: success += 1
	
		print(i, roll)
	
	return success / trials
	
trials = 1000 
dc = [5, 10, 15]

for dc in dc:
	success_rate = roll_saving_throws(trials, dc, "normal")
	print(success_rate * 100)
	
