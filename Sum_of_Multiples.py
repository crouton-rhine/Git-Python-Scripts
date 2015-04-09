def sum_of_multiples(maximum):
	num_list = [x for x in range(1,maximum) if x%3 == 0 or x%5 == 0]
	num_sum = 0
	for i in num_list:
		num_sum += i
	print("The sum is... " + str(num_sum))
print("FIND THE SUM OF ALL THE MULTIPLES OF 3 AND 5 WITHIN A SPECIFIC RANGE")
sum_of_multiples(int(input("Enter a range, 1 - ")))
