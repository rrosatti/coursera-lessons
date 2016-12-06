import csv

with open('mpg.csv') as csvfile:
	mpg = list(csv.DictReader(csvfile)) # save the csv content as a list/dictionary

## print the first 3 dictionaries in this list
#print mpg[:3]	

## print keys
#print mpg[0].keys()

## find the average weight across all cars.
#print sum(float(d['weight']) for d in mpg) / len(mpg)

## use set to return the unique values for the number of cylinders
cylinders = set(d['cylinders'] for d in mpg)
#print cylinders

# try to convert a String to int
def get_int(content):
	try:
		num = int(content)
		return num
	except ValueError:
		return 0

## group the cars by the number of cylinder, and finding the average horsepower for each group
avgHorsePowerByCyl = []

for c in cylinders:
	sumHorsePower = 0
	count = 0
	for d in mpg: # iterate over all dicitionaries
		if d['cylinders'] == c: # if the cylinder level type matches
			sumHorsePower += get_int(d['horsepower']) # add the horse power
			count += 1 # increase the count variable

	avgHorsePowerByCyl.append((c, sumHorsePower / count)) # append the tuple ('cylinder', 'avg horsepower')

avgHorsePowerByCyl.sort(key=lambda x: x[0]) # I still don't really know what's going on here
print avgHorsePowerByCyl
