try:
    a = int(input("Enter a number\n"))
    print(a)

except ValueError as e:
    print(f"Invalid input: {e}")

except KeyboardInterrupt:
    print(f"Keyboard interrupt using ctrl+c")