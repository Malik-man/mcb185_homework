import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def duplicate_birthdays(people, days):
	birthdays = []
	for i in range(people):
		bday = random.randint(1, days)
		if bday in birthdays:
			return True
		birthdays.append(bday)
	return False 
	
matches = 0 
for _ in range(trials):
	if duplicate_birthdays(people, days):
		matches += 1

prob = matches / trials

print("probability of a shared birthdays:", prob)

