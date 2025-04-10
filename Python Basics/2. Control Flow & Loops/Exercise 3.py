# Create a script that prints every 4-digit PIN code (0000-9999).

# my code
index = 0
while index <= 9999:
    if index < 10:
        print(f"000{index}")
    elif index < 100:
        print(f"00{index}")
    elif index < 1000:
        print(f"0{index}")
    else:
        print(index)
    index += 1

# Ai code
# for index in range(10000):
#     print(str(index).zfill(4))
