# Weather Prediction

weather = (1,0,0,1,0,1,1,0,1)
sunny = 0
rainy = 0
for i in weather:
    if i in weather:
        if i == 1:
            sunny += 1
        else:
            rainy += 1 

if sunny > rainy:
    print("good weather")
else:
    print("bad weather")