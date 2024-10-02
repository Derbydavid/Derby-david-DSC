def carton_breakup(bottles):
    carton_sizes = {
        "xl": 48,
        "large": 24,
        "medium": 12,
        "small": 6
    }

    cartons_used = {size: 0 for size in carton_sizes}

    for size, capacity in carton_sizes.items():
        if bottles >= capacity:
            cartons_used[size] = bottles // capacity  
            bottles %= capacity
            
    output = []
    for size in cartons_used:
        if cartons_used[size] > 0:
            output.append(f"{cartons_used[size]} {size}")

    result = ', '.join(output)
    print(result)

number_of_bottles = 140
carton_breakup(number_of_bottles)
