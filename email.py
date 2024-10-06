email = input (" entrt the mail")
index = email .index('@')
username = email[:index]
domain = email [index+1:]

print(f"your user name is {username} and domain is {domain}")