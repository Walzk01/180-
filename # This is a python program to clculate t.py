# This is a python program to clculate the Fibonacci sequence. Create the Fibonacci sequence for the 5th number in the sequence.
def fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]  # Calculate the next number in the sequence
        sequence.append(next_number)  # Add the next number to the sequence
    return sequence

n = 10  # Specify the number of Fibonacci numbers to generate
fib_sequence = fibonacci(n)
print(fib_sequence)

