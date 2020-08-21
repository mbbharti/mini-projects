import datetime

def getdatetime():
	return datetime.datetime.today()

def take(val):
	if val==1:
		c=int(input("Press 1 for exercise and 2 for food"))
		if(c==1):
			data=input("type here \n")
			with open("harry-ex.txt","a") as op:
				op.write(str([str(getdatetime())]) + ":" + data +"\n")
			print("Successfully Written")
		elif c==2:
			data=input("type here \n")
			with open("harry-meal.txt","a") as op:
				op.write(str([str(getdatetime())]) + ":" + data +"\n")
			print("Successfully Written")
		else :
			print("Please Enter Valid input\n")

	elif val==2:
		c=int(input("Press 1 for exercise and 2 for food"))
		if c==1:
			data=input("type here \n")
			with open("rohan-ex.txt","a") as op:
				op.write(str([str(getdatetime())]) + ":" + data)
			print("Successfully Written\n")
		elif c==2:
			data=input("type here\n")
			with open("rohan-meal.txt","a") as op:
				op.write(str([str(getdatetime())]) + ":" + data)
			print("Successfully Written\n")
		else:
			print("Please Enter Valid input\n")

	elif val==3:
		c=int(input("Press 1 for exercise and 2 for food"))
		
		if c==1:
			data=input("type here\n")
			with open("hammad-ex.txt","a") as op:
				op.write(str([str(getdatetime())]) + ":" + data)
			print("Successfully Written\n")
		elif c==2:
			data=input("type here\n")
			with open("hammad-meal.txt","a") as op:
				op.write(str([str(getdatetime())]) + ":" + data)
			print("Successfully Written\n")						
  		
		else :print("Please Enter Valid input\n")
	
	else :
		print("Please Enter Valid input\n")		

def retrieve(val):
	if val==1:
		c=int(input("Press 1 to retrieve exercise info or Press 2 to retrieve food info"))
		if c==1:
			with open("harry-ex.txt") as op1:
				for data in op1:
					print(data,end=" ")
		elif c==2:
			with open("harry-meal.txt") as op1:
				for data in op1:
					print(data,end=" ")
		else:
			print("Please Enter Valid input\n")						
	elif val==2:
		c=int(input("Press 1 to retrieve exercise info or Press 2 to retrieve food info"))
		if c==1:
			with open("rohan-ex.txt") as op1:
				for data in op1:
					print(data,end=" ")
		elif c==2:
			with open("rohan-meal.txt") as op1:
				for data in op1:
					print(data,end=" ")
		else:
			print("Please Enter Valid input\n")		
	elif val==3:
		c=int(input("Press 1 to retrieve exercise info or Press 2 to retrieve food info"))
		if c==1:
			with open("hammad-ex.txt") as op1:
				for data in op1:
					print(data,end=" ")
		elif c==2:
			with open("hammad-meal.txt") as op1:
				for data in op1:
					print(data,end=" ")
		else:
			print("Please Enter Valid input\n")		
	else:
			print("Please Enter Valid input\n")		

# if __name__ == '__main__':

print("Health Management System \n")
print("Press 1 to log\nPress 2 for retrieve")
key=int(input())
	
if key==1:
	print("press 1 for harry\nPress 2 for rohan\nPress 3 for hammad")
	val=int(input())
	take(val)	

elif key==2:
	print("Press 1 for harry\nPress 2 for rohan\nPress 3 for hammad")
	val=int(input())
	retrieve(val)
else:
	print("Please Enter Valid input\n")

		
