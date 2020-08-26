from pygame import mixer
from datetime import datetime
from time import time

def music_loop(file_name,stopper):
	mixer.init()
	mixer.music.load(file_name)
	mixer.music.play()

	while True:
		a=input()
		if a=='exit':
			stopp()

		if a==stopper:
			mixer.music.stop()
			break


def log_now(msg):
	with open("programmer.txt","a") as op:
		op.write(f" {msg} {datetime.now()} \n")

if __name__ == '__main__':
				init_water=time()
				init_eye=time()
				init_exe=time()
			
				water_sec=40*60
				eye_sec=50*60
				exe_sec=60*60

				while(True):
					def stopp():
						break

					if time()-init_water > water_sec:
						print("Its time to drink water and enter 'drank' to stop alaram\n")
						music_loop('Water-draining-through-plumbing-pipe.mp3','drank')
						init_water=time()
						log_now("Drank water at :")

					if time()-init_eye > eye_sec:
						print("Its time to relax your eyes from computer screen and please enter'relaxed' to stop alaram\n")
						music_loop('Water-draining-through-plumbing-pipe.mp3','relaxed')
						init_eye=time()
						log_now("Eyes relaxed at :")

					if time()-init_exe > exe_sec:
						print("Its time to do some physical streching and please enter 'streched' to stop alaram\n")
						music_loop('Water-draining-through-plumbing-pipe.mp3','streched')
						init_exe=time()
						log_now("Body streched at :")		

						