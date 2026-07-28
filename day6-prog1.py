places=[]
for i in range(1,6):
    place= input(f"enter the name of place{i}: ")
    places.append(place)
print(f"places stored in list: {places}")

place_str= ','.join(places)
result= place_str.upper()
print(f"All places separated by comma and space and in uppercase:{result}")