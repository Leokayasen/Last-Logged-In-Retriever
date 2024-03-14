username = input("Enter your username: ")
text_file = open("UserData", "r")
end_of_file = False
while not end_of_file:
	user = text_file.readline().strip()
	login_date = text_file.readline().strip()
	if user == username:
		end_of_file = True
		print("Last logged in on:", login_date)
	if user == "":
		end_of_file = True
		print("User not found")
text_file.close()
