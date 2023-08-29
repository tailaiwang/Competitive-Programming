# Language question


# Helper function to check if we have a positive or negative integer
def int_check(n):
	try:
		int(n)
	except ValueError:
		return False
	else:
		return True

lang = []
while True:
	line = input()
	if line == "quit":
		break
	else:
		line  = line.split(" ")
		cmd = line[0]
		if cmd == "push":
			lang.append(line[1])
		elif cmd == "pop":
			if (len(lang) > 0):
				lang.pop()
			else:
				print("ERROR: Unable to Pop")
		elif cmd == "print":
			if (len(lang) > 0):
				print(lang[-1])
			else:
				print("ERROR: Unable to Print") 
		elif cmd == "add":
			if (len(lang) >= 2):
				arg1 = lang.pop()
				arg2 = lang.pop()
				if int_check(arg1) and int_check(arg2):
					lang.append(int(arg1) +int(arg2))
				else:
					lang.append(str(arg1) + str(arg2))
			else:
				print("ERROR: Unable to Add")


