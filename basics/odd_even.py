def chkNum(num):
	if(int(num) % 2 == 0):
		print("Even number");
	else:
		print("Odd number");
		
def main():
	if(__name__ == "__main__"):
		print("Enter number:")
		num = input();
		chkNum(num);
		
main();