n = int(input("Enter a number: "))
count =0

while n >= 12:
    n /= 4
    count += 1
print("The given number can be divided by 4=",count, "times")