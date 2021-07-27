def chkNum(num):
	if(int(num) > 0):
		print("Positive Number");
	elif(int(num) < 0):
		print("Negative Number");
	else:
		print("Zero");

def main():
	if(__name__ == "__main__"):
		print("Enter number:");
		num = input();
		chkNum(num);
			
main();