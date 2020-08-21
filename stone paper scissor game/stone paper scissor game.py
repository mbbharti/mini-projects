import random
data=["stone","paper","scissor"]

# val=random.choice(data)

print("-------******   Welcome to Stone Paper Scissor Game   ******--------\n")
i=0
a=0 #your score
b=0 #computer's score
while i<10:
	val=random.choice(data)
	print("Please Enter your choice among Stone, Paper and Scissor")
	inp=input()
	if(inp=="stone"):
		if val=="scissor":
			print("You Win\n")
			a+=1
		elif val=="paper":
			print("You Lose\n")
			b+=1
		elif val=="stone":
			print("Its a TIE\n")
		else:
			print("Please Enter valid input\n")

	elif(inp=="paper"):
		if(val=="stone"):
			print("You Win\n")
			a+=1				
		elif val=="scissor":
			print("You Lose\n")
			b+=1
		elif val=="paper":
			print("Its a TIE\n")
		else:
			print("Please Enter valid input\n")
	
	elif(inp=="scissor"):
		if(val=="paper"):
			print("You Win\n")
			a+=1				
		elif val=="stone":
			print("You Lose\n")
			b+=1
		elif val=="scissor":
			print("Its a TIE\n")
		else:
			print("Please Enter valid input\n")

	else:
		print("Please enter valid input\n")


	print(f"You choose {inp} and computer choose {val}")
	print(f"Current Score :-  you   {a} and  computer-  {b}\n")	

	i+=1		
	pass

print("    ----Final Result----\n")
if a>b:
	print("  YOU WON THE GAME")
elif b>a:
	print("  YOU LOSE THE GAME")
else:
	print("  I is a TIE")		