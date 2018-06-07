from PIL import Image
for city in cities:
    for x in ("HIGH","LOW","PRECIPITATION","CLOUD COVER"):
        file_in = "C:/Python34/Scripts/WeatherData/ALL_IMG/"+x+"/"+str(city[2])+"_"+str(city[0])+".bmp"
        im = Image.open(file_in)
        print(im.size)
        file_out = "C:/Python34/Scripts/WeatherData/ALL_IMG/PNG/"+x+"/"+str(city[2])+"_"+str(city[0])+".png"
        im.save(file_out,"png")
