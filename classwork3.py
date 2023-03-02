number = 20

match number:
    case number if number in range (1,21):
        print("Case1")
    case _:
        print("Default")