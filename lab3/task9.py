def sphere_volume(radius):
    volume = (4 / 3) * 3.14 * radius**3
    return volume

radius = float(input())
result = sphere_volume(radius)
print( result)
