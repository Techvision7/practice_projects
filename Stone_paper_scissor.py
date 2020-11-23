print("welcome to text based version of stone paper scissor.")
import random

def game():
	sps = ["stone", "paper", "scissor"]
	computer = sps[random.randint(0,2)]
	player = input("Enter your choice(stone/paper/scissor) :-").lower()

	if player == "stone":
		if computer == "scissor":
			print("player won.... computer choose", computer)
		else:
			print("computer won.... computer choose", computer)

	elif player == "scissor":
		if computer == "paper":
			print("player won.... computer choose", computer)
		else:
			print("computer won.... computer choose", computer)

	elif player == "paper":
		if computer == "stone":
			print("player won.... computer choose", computer)
		else:
			print("computer won.... computer choose", computer)

	else:
		print("You May Have Entered Wrong Values")



game()