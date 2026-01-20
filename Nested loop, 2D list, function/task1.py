def check_failing(grades_grid):
    for i in range(len(grades_grid)):
        for score in grades_grid[i]:
            if score < 50:
                print(f"Student {i} failed a subject!")
                break


all_grades = [
    [88, 92, 70],
    [45, 80, 77],
    [99, 100, 95]
]

check_failing(all_grades)
