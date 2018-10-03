def fibonacci(lim):
	# start with 1,2
	result = [1,2]

	for n in range(1, lim):
		val = result[n] + result[n-1] # calculation for Fibonacci
		if(val > lim): # stop when the limit has been reached without appending it to the list
			break
		else:
			result.append(val)
	return result # returns a list of Fibonacci sequence up to the limit given.

def sum_even(arr):
	even = [ n for n in arr if n%2 == 0] # Filters out the even numbers from arr list
	result = 0
	for n in even:
		result += n # iterate through these even numbers and add them together
	return result # final answer

numCases = int(input().strip())
cases = []

for n in range(numCases):
	cases.append(int(input().strip()))

for case in cases:
	fibArray = fibonacci(case)
	result = sum_even(fibArray)
	print(result)
