def process(list):
    n = len(list)
    cuples = 0

    j = 1
    for i in range(1 ,n - 2):
        if i % 2 != 0:
            j += 2
        for k in range(j, n):
            if (list[i] % 2 == 0 and list[k] % 2 != 0):
                cuples += 1
                print(list[i], list[k])
            if (list[i] % 2 != 0 and list[k] % 2 == 0):
                cuples += 1
                print(list[i], list[k])

    print("Кількість комбінацій паp:", cuples)
