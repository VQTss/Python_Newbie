n = int(input())
if n % 2 == 1:
    print("Weird")
else:
    if n <= 5:
        print("Not Weird")
    elif n <= 6:
        print("Weird")
    else:
        print("Not Weird")