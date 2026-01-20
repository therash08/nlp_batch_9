name = "rash"
print(f"my name is {name}")


def xyz():
    global name

    name = "rasidul hoque"
    print(f"my name is {name}")
    return 100


xyz()

print(name)

# xyz()
