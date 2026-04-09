"""
TODO: Build a function that generates the Fibonacci sequence till 'n'number.
"""

def main(num_1: int, num_2: int):
    """Fibonacci sequence:

    This is a mathematical sequence that says:
    Each number is composed for the sum of the two preceding numbers.
    F(0) = 0  
    F(1) = 1  
    F(2) = 0 + 1 = 1  
    F(3) = 1 + 1 = 2 ..."""
    if num_1.is_integer and num_2.is_integer:

        fib_sequence = [num_1, num_2]
        count_end = 0

        while count_end <= 6: #The sequence its infinit so we will take end point number with this
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            count_end += 1
    return fib_sequence
    """"
    The curious thing is that the ratios of consecutive Fibonacci numbers 
    do not match the initial values; instead, they tend to the golden ratio :O
    """
if __name__ == "__main__":
    print(main(0, 1)) #[0,1,1,2,3,5,13,21]
