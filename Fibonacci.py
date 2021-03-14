def Fibonacci(number):
    if (number == 0):
        return 0
    elif (abs(number) == 1):
        return 1
    elif (number > 1):
        return Fibonacci(number-1) + Fibonacci(number-2)
    else :
        return (Fibonacci(abs(number)-1) + Fibonacci(abs(number)-2)) * ((-1)**(abs(number)-1))

def main():
    number = int(input("Enter a number to get that Fibonacci's number\n"))
    print("The " + str(number) + " sequence of Fibonacci series is: " + str(Fibonacci(number)))


if __name__ == "__main__":
    main()
