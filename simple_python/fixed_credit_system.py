# OPEN CREDIT SYSTEM

dept = input("Enter Department Name (CSE/EEE/BBA/LAW/ENG): ")

total_weighted = 0
total_credit = 0

# ---------- CSE ----------
if dept == "CSE":
    # Subject 1: Programming (3 credit)
    ct = float(input("Programming CT: "))
    mid = float(input("Programming Mid: "))
    final = float(input("Programming Final: "))
    total = ct + mid + final

    if total >= 80:
        gp = 4.0
    elif total >= 75:
        gp = 3.75
    elif total >= 70:
        gp = 3.5
    elif total >= 65:
        gp = 3.25
    elif total >= 60:
        gp = 3.0
    elif total >= 50:
        gp = 2.5
    else:
        gp = 0.0

    total_weighted += gp * 3
    total_credit += 3

    # Subject 2: Data Structure (3 credit)
    ct = float(input("DS CT: "))
    mid = float(input("DS Mid: "))
    final = float(input("DS Final: "))
    total = ct + mid + final

    if total >= 80:
        gp = 4.0
    elif total >= 75:
        gp = 3.75
    elif total >= 70:
        gp = 3.5
    elif total >= 65:
        gp = 3.25
    elif total >= 60:
        gp = 3.0
    elif total >= 50:
        gp = 2.5
    else:
        gp = 0.0

    total_weighted += gp * 3
    total_credit += 3

    # Subject 3: Database (3 credit)
    ct = float(input("Database CT: "))
    mid = float(input("Database Mid: "))
    final = float(input("Database Final: "))
    total = ct + mid + final

    if total >= 80:
        gp = 4.0
    elif total >= 75:
        gp = 3.75
    elif total >= 70:
        gp = 3.5
    elif total >= 65:
        gp = 3.25
    elif total >= 60:
        gp = 3.0
    elif total >= 50:
        gp = 2.5
    else:
        gp = 0.0

    total_weighted += gp * 3
    total_credit += 3

    # Subject 4: Math (4 credit)
    ct = float(input("Math CT: "))
    mid = float(input("Math Mid: "))
    final = float(input("Math Final: "))
    total = ct + mid + final

    if total >= 80:
        gp = 4.0
    elif total >= 75:
        gp = 3.75
    elif total >= 70:
        gp = 3.5
    elif total >= 65:
        gp = 3.25
    elif total >= 60:
        gp = 3.0
    elif total >= 50:
        gp = 2.5
    else:
        gp = 0.0

    total_weighted += gp * 4
    total_credit += 4

    # Subject 5: Electronics (3 credit)
    ct = float(input("Electronics CT: "))
    mid = float(input("Electronics Mid: "))
    final = float(input("Electronics Final: "))
    total = ct + mid + final

    if total >= 80:
        gp = 4.0
    elif total >= 75:
        gp = 3.75
    elif total >= 70:
        gp = 3.5
    elif total >= 65:
        gp = 3.25
    elif total >= 60:
        gp = 3.0
    elif total >= 50:
        gp = 2.5
    else:
        gp = 0.0

    total_weighted += gp * 3
    total_credit += 3

    cgpa = total_weighted / total_credit
    print("CGPA:", round(cgpa, 2))

else:
    print("Department not found")
