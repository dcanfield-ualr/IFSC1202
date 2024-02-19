def draw_grid(rows, cols):
    for i in range(rows):
        print("+", end="")
        for j in range(cols):
            print("----+", end="")
        print()
        for j in range(cols + 1):
            print("|    ", end="")
        print()
    print("+", end="")
    for j in range(cols):
        print("----+", end="")
    print()

# Example usage:
draw_grid(3, 2)
