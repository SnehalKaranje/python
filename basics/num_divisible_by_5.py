def isNumDivisibleBy5(num):
	if(int(num) % 5 == 0):
		return True;
	else:
		return False;

def main():
	if(__name__ == "__main__"):
		print("Enter number:");
		num = input();
		print(isNumDivisibleBy5(num));
			
main();