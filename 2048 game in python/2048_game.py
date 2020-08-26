import logic_2048


print("       .........******* Welcome to 2048 Game *******........\n \n")

if __name__ == '__main__':
	mat=logic_2048.start_game()

while (True):
	x=input("Enter your choice....\n")

	if x=='w' or x=='W':
		mat,flag=logic_2048.move_up(mat)
		status=logic_2048.get_current_stats(mat)
		print(status)
		if status=='Continue...':
			logic_2048.get_new_2(mat)

		else:
			break

	elif x=='s' or x=='S':
		mat,flag=logic_2048.move_down(mat)
		status=logic_2048.get_current_stats(mat)
		print(status)

		if status=='Continue...':
			logic_2048.get_new_2(mat)

		else:
			break

	elif x=='a' or x=='A':
		mat,flag=logic_2048.move_left(mat)
		status=logic_2048.get_current_stats(mat)
		print(status)

		if status=='Continue...':
			logic_2048.get_new_2(mat)

		else:
			break

	elif x=='d' or x=='D':
		mat,flag=logic_2048.move_right(mat)
		status=logic_2048.get_current_stats(mat)
		print(status)

		if status=='Continue...':
			logic_2048.get_new_2(mat)

		else:
			break

	else:
		print("Enter valid input.....")


	# print(logic_2048.score)	
	print("score = ",logic_2048.get_score(),"\n")
	for i in range(4):
		for j in range(4):
			print(mat[i][j],end=" ")
		print()			

			

						


			


