import colorsys

print("RED:",colorsys.rgb_to_hsv(1.0,0.0,0.0))
print("YELLOW:",colorsys.rgb_to_hsv(1.0,1.0,0.0))
print("GREEN:",colorsys.rgb_to_hsv(0.0,1.0,0.0))
print("AQUAM:",colorsys.rgb_to_hsv(0.0,1.0,1.0))
print("BLUE:",colorsys.rgb_to_hsv(0.0,0.0,1.0))
print("PURPLE:",colorsys.rgb_to_hsv(1.0,0.0,1.0))
r, g, b = colorsys.hsv_to_rgb(0.5,1,1)
print(r,",",g,",",b)

for i in range(100):
    r, g, b = colorsys.hsv_to_rgb((float(i)/100),1,1)
    print("I ",i,":",r,",",g,",",b)
