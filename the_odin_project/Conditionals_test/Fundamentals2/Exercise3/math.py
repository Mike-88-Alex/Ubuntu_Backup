import logging


logging.basicConfig(level=logging.INFO)

a = 1 + 8
b = 22 * 3
c = 5 % 4
d = a - 17
e = a + b + c + d

if(a == 9): 
	logging.info("'a' is correct!")
else: 
	print(f"'a' is incorrect, got {a}, expected 9")

print("\n")

if(b == 66):
	print("'b' is correct!")
else:
	print(f"'b' is incorrect, got {b}, expected 66")

print("\n")

if(c == 1):
	print("'c' is correct!")
else:
	print(f"'c' is incorrect, got {c}, expected 1")

print("\n")

if(d == -8):
	print("'d' is correct!")
else:
	print(f"'d' is incorrect, got {d}, expected -8")

print("\n")

if(e == 68):
	print("'e' is correct!")
	print("\n Congrats! You've solved them all, you may move onto the next lesson")
else:
	print(f"'e' is incorrect, got {e}, expected 68")