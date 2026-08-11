def ft_water_reminder(): 
    days = input("Days since last watering: ")
    print("Water the plants!") if int(days) > 2 else print("Plants are fine")
