import string
import random

if __name__ == '__main__':
	id=input("Whose password you want to create?")

	s=[]
	s1=string.ascii_lowercase
	s2=string.ascii_uppercase
	s3=string.digits
	s4=string.punctuation

	s.extend(s1)
	s.extend(s2)
	s.extend(s3)
	s.extend(s4)
	random.shuffle(s)
	
	lenn=int(input("Please Enter the length of your password:"))
	pas=("".join(s[0:lenn]))
	with open("pass.txt","a") as op:
		op.write(f" it is the password of {id} and the password is {pas}  \n")