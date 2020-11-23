print("Hello This is Techvision7")
print("Welcome to my First Python Game!")

name = input("What is your Name? ")
age = int(input("what is your age? "))

print("Hello", name.upper(), "you are", age, "Years Old.")
if age >= 18:
	print("You can Participate in Game!")
	wants_to_play = input("Do you Want to play ").lower()
	if wants_to_play == "yes":
		print("Let's Play")

		health = 10
		print("you are starting with", health, "Health")
		left_or_right = input("First choose...Left or Right (left/right)? ").lower()
		if left_or_right == "left":
		
			ans =  input("Nice you followed a path and reached a lake ... do you swim across or go around (across/around)? ").lower()
			if ans == "around":
				print("you went around and reached the other side of the lake.")

			elif ans == "across":
				print("you manage to get across but bit by a Fishes and lost 5 health. ")
				health -= 5
		

			ans = input("you notice a house and a river which way do you go to (house/river)? ").lower()
			if ans == "house":
				print("you go to the house and greeted by the owner but he doesnt like you and you lost 5 health")
			else:
				print("you fell in the river and lost the Game")
				health -= 5


				if health <= 0 :
					print("you now have 0 health and You lost the Game...")
				else:
					print("Congratulations you have survived")


		else:
			print("you fell Down and lost.....")
	else:
		print("Good Bye See You Later")

else:
	print("sorry.. you cannot particiapte in following Game")