import sys

def main(arguments):
	operation = '1'
	while operation != '0':
		list_operations()
		operation = read_operation()
	return 0

def list_operations():
	print ("1 - Suma: x + y")
	print ("2 - Resta: x - y")
	print ("3 - Multiplicación: x * y")
	print ("4 - División: x / y")
	print ("5 - Modulo: x % y")
	print ("0 - Salir")

def sum(nums):
	return nums[0] + nums[1]

def substraction(nums):
	return nums[0] - nums[1]

def multiplication(nums):
	return nums[0] * nums[1]

def division(nums):
	return nums[0] / nums[1]

def module(nums):
	return nums[0] % nums[1]

def read_operation():
	operation = input()
	resultString = "El resultado es {}\n"
	if operation == '1':
		print (resultString.format(sum(ask_values())))
	elif operation == '2':
		print (resultString.format(substraction(ask_values())))
	elif operation == '3':
		print (resultString.format(multiplication(ask_values())))
	elif operation == '4':
		print (resultString.format(division(ask_values())))
	elif operation == '5':
		print(resultString.format(module(ask_values())))
	elif operation == '0':
		sys.exit(0)

	return operation

def ask_values(count = 2):
	numbers = []
	for i in range(count):
		print ("Introduce el {} numero:".format(i+1))
		numbers.append(int(input()))
	
	return (numbers)

if __name__ == '__main__':
	main(sys.argv[1:])