def activate_row(screen, row_index):
    for col in range(len(screen[row_index])):
        screen[row_index][col] = 1


monitor = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

activate_row(monitor, 1)

print(monitor)
