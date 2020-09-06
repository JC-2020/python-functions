# Write an is_odd function that uses you is_even function to determine if a number is odd.  (That is, do not do the calculation - call a function that does the calculation.)

num = int(input("Enter a number:"))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

