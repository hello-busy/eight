#!/usr/bin/env python3
"""
Eight - A simple program demonstrating various operations with the number 8
"""

def print_eight():
    """Print the number 8"""
    return 8

def eight_times_table():
    """Generate the multiplication table for 8"""
    return [(i, 8 * i) for i in range(1, 11)]

def powers_of_eight(limit=5):
    """Generate powers of 8 up to the specified limit"""
    return [(i, 8 ** i) for i in range(limit)]

def eight_ascii_art():
    """Return ASCII art representation of the number 8"""
    art = """
 ████████ 
██      ██
██      ██
 ████████ 
██      ██
██      ██
 ████████ 
"""
    return art.strip()

def is_multiple_of_eight(number):
    """Check if a number is a multiple of 8"""
    return number % 8 == 0

def main():
    """Main function demonstrating eight-related operations"""
    print("Welcome to Eight!")
    print("=" * 20)
    
    # Display the number 8
    print(f"The number: {print_eight()}")
    print()
    
    # Display ASCII art
    print("ASCII Art:")
    print(eight_ascii_art())
    print()
    
    # Show multiplication table
    print("Eight times table:")
    for multiplier, result in eight_times_table():
        print(f"8 × {multiplier} = {result}")
    print()
    
    # Show powers of 8
    print("Powers of eight:")
    for power, result in powers_of_eight():
        print(f"8^{power} = {result}")
    print()
    
    # Test multiples
    test_numbers = [8, 16, 24, 25, 32, 40, 45, 48]
    print("Testing multiples of 8:")
    for num in test_numbers:
        is_multiple = is_multiple_of_eight(num)
        print(f"{num} is {'a' if is_multiple else 'not a'} multiple of 8")

if __name__ == "__main__":
    main()