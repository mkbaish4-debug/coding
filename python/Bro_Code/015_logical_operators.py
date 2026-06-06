temp = -12
is_sunny = False
if temp >= 32 and is_sunny:
    print("It is HOT outside! ")
    print("It is SUNNY!")
elif temp < 32 and temp > 0 and is_sunny:
    # 32>temp>0 would also work
    print("It is WARM outside! ")
    print("It is SUNNY!")
elif temp < 0 and is_sunny:
    print("It is COLD outside! ")
    print("It is SUNNY!")
elif temp < 0 and not is_sunny:
    print("It is COLD outside! ")
    print("It is CLOUDY!")
elif 32>temp>0 and not is_sunny:
    print("It is WARM outside! ")
    print("It is CLOUDY!")
elif temp > 32 and not is_sunny:
    print("It is HOT outside! ")
    print("It is CLOUDY!")
