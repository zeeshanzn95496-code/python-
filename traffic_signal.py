import time 
roads = ["North","East","south","west"]

Normal_Time = 5
Emergency_Time =3

while True:
    print("\n traffic signal system")
    print("1. normal traffic")
    print("2. ambulance emergency")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice=="1":
        for road in roads:
            print("\n    GREEN:    ",road)
            for other_road in roads:
                if other_road != road:
                    print("RED:",other_road)
                    time.sleep(Normal_Time)