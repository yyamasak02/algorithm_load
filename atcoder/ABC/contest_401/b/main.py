n: int = int(input())
is_logged_in: bool = False
error_count: int = 0
for _ in range(n):
	s = input()
	if s == "login":
		is_logged_in = True
	elif s == "logout":
		is_logged_in = False
	elif s == "public":
		pass
	elif s == "private" and not is_logged_in:
		error_count += 1
	elif s == "private" and is_logged_in:
		pass

print(error_count)