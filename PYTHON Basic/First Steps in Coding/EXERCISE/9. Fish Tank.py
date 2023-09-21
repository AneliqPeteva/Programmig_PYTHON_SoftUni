length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage = float(input())

volume_aquarium = length_cm * width_cm * height_cm
volume_litres = volume_aquarium / 1000
litres_water = volume_litres * (1-percentage/100)
print(litres_water)