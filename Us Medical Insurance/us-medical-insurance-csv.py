import csv

# list of insurance costs, regions, and ages
ins_costs = list()
regions = list()
ages = list()

# opening insurance.csv
with open("insurance.csv") as insurance_csv:
	# turning the file into a dict
	ins_dict = csv.DictReader(insurance_csv)
	
	# appending the data
	for row in ins_dict:
		ins_costs.append(row["charges"])
		regions.append(row["region"])
		ages.append(row["age"])

#print(ins_costs)
#print(regions)
#print(ages)


# the main function
def main():
	# total number of records
	no_of_records = len(ins_costs)
	
	# total insurance cost and age variables
	total_age = 0
	total_ins_cost = 0
	
	# calculating the total insurance cost
	for ins_cost in ins_costs:
		total_ins_cost += float(ins_cost)
	for age in ages:
		total_age += int(age)
	
	# finding where the majority of the individuals are from
	people_from_southwest = 0
	people_from_southeast = 0
	people_from_northwest = 0
	people_from_northeast = 0
	
	for region in regions:
		if region == "southwest":
			people_from_southwest += 1
		elif region == "southeast":
			people_from_southeast += 1
		elif region == "northwest":
			people_from_northwest += 1
		elif region == "northeast":
			people_from_northeast += 1
	
	# calculating the average insurance cost and age
	average_ins_cost_rounded = round(total_ins_cost / no_of_records, 1)
	exact_average_ins_cost = total_ins_cost / no_of_records
	average_age = round(total_age / no_of_records)
	
	# printing the results
	print(f"There are {no_of_records} records in insurance.csv.")
	print(f"The total insurance cost is {total_ins_cost}.")
	print(f"The average insurance cost is ${average_ins_cost_rounded}")
	print(f"The exact average insurance cost is ${exact_average_ins_cost}")
	print("People from southwest: ", people_from_southwest)
	print("People from southeast: ", people_from_southeast)
	print("People from northwest: ", people_from_northwest)
	print("People from northeast: ", people_from_northeast)
	print(f"Most of the people are from the southeast.")
	print(f"The average age is {average_age}")

main()
