import random


score=0


def start_game():
	mat=[]
	for i in range(4):
		mat.append([0]*4)


	print("Commands are as follows.......")	
	print("Press 'W' or 'w' to move UP ")
	print("Press 'S' or 's' to move DOWN ")
	print("Press 'A' or 'a' to move LEFT ")
	print("Press 'D' or 'd' to move RIGHT ")

	get_new_2(mat)
	for i in range(4):
		for j in range(4):
			print(mat[i][j],end=" ")
		print()
	return mat

def get_new_2(mat):
	p=random.randint(0,3)
	q=random.randint(0,3)

	while mat[p][q] != 0 :
		p=random.randint(0,3)
		q=random.randint(0,3)

	mat[p][q]=2

def get_current_stats(mat):
	
	for i in range(4):
		for j in range(4):
			if mat[i][j]==2048:
				return "****** YOU WON THE GAME *******"

	for i in range(4):
		for j in range(4):
			if mat[i][j]==0:
				return "Continue..."

	for i in range(3):
		for j in range(3):
			if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
				return "Continue..."

	# for j in range(3):
	# 	for i in range(4):
	# 		if mat[i][j]==mat[i][j+1]:
	# 			return "Continue..."

	for j in range(3):
		if mat[3][j]==mat[3][j+1]:
			return "Continue..."													

	for i in range(3):
		if mat[i][3]==mat[i+1][3]:
			return "Continue..."

	return "****** GAME OVER , You lost ******"

def reverse(mat):
	new_mat=[]
		

	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[i][3-j])

	return new_mat
	
def transpose(mat):
	new_mat=[]

	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[j][i])

	return new_mat
							
def compress(mat):
	changed=False

	new_mat=[]
	for i in range(4):
		new_mat.append( [0]*4)


	for i in range(4):
		pos=0

		for j in range(4):
			if (mat[i][j] != 0):
				new_mat[i][pos]=mat[i][j]

				if j != pos:
					changed=True
				pos+=1

	return new_mat,changed


def merge(mat):
	changed=False

	new_mat=[]

	for i in range(4):
		for j in range(3):
			if mat[i][j]==mat[i][j+1] and mat[i][j] !=0 :
				mat[i][j]= 2*mat[i][j]

				global score
				score+= 2*mat[i][j]
					
				mat[i][j+1]=0
				changed=True

	return mat,changed
	
def move_left(get_mat):
	get_new_mat,changed1 =compress(get_mat)

	get_new_mat,changed2=merge(get_new_mat)

	changed= changed1 or changed2

	get_new_mat,temp=compress(get_new_mat)

	return get_new_mat,changed

def move_up(get_mat):
	get_new_mat=transpose(get_mat)

	get_new_mat,changed=move_left(get_new_mat)

	get_new_mat=transpose(get_new_mat)

	return get_new_mat,changed

def move_right(get_mat):
	get_new_mat=reverse(get_mat)

	get_new_mat,changed=move_left(get_new_mat)

	get_new_mat=reverse(get_new_mat)

	return get_new_mat,changed

def move_down(get_mat):

	get_new_mat=transpose(get_mat)

	get_new_mat,changed=move_right(get_new_mat)

	get_new_mat=transpose(get_new_mat)

	return get_new_mat,changed

def get_score():
	return int(score/2)			



	


