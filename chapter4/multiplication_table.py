def print_multiplication_table(n):
    """Prints the multiplication table up to n."""
    for i in range(1, n + 1):
        print("    ", end="")
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()


if __name__ == "__main__":
    print_multiplication_table(20)
