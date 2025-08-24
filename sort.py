def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Determine bulky condition
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    
    # Determine heavy condition
    heavy = mass >= 20
    
    # Sorting logic
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

print(sort(100, 100, 100, 10))   # SPECIAL (bulky only)
print(sort(200, 50, 40, 25))     # REJECTED (bulky and heavy)
print(sort(50, 50, 50, 25))      # SPECIAL (heavy only)
print(sort(50, 50, 50, 10))      # STANDARD (neither)
