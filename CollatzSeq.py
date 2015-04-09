def CollatzSeq(number):
	sequence = [number]
	while number != 1:
		if number % 2 == 0:
			number = int(number / 2)
			sequence.append(number)
		else:
			number = int(3*number + 1)
			sequence.append(number)
	return sequence
	#print(sequence)

def CountCollatz(sequence):
	return len(sequence)

def LargestList(n):
	Seq_Length_List = []
	for key in range(1, n):
		sequence = CollatzSeq(key)
		length = CountCollatz(sequence)
		Seq_Length_List.append(length)
	#return Seq_Length_List
	return Seq_Length_List.index(max(Seq_Length_List)) + 1

number = int(input("Enter number up to which the Collatz sequence should be computed:"))
#sequence = CollatzSeq(number)
#print(sequence)
#print("This list has %i elements" % CountCollatz(sequence))
print("The largest number that yields the largest Collatz Sequence is %i" % LargestList(number))
