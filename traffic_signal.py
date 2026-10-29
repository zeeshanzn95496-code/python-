import time 
roads = ["North", "East", "South", "West"]

Normal_Time = 7
Emergency_Time = 4

while True:
    print("\n traffic signal system")
    print("1. normal traffic")
    print("2. ambulance emergency")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        for road in roads:
            print("\n    GREEN:    ", road)
            for other_road in roads:
                if other_road != road:
                    print("RED:", other_road)
            time.sleep(Normal_Time)

    # These must line up with 'if choice == "1":'
    elif choice == "2":
        ambulance_road = input("enter ambulance road first letter in capital (North/East/South/West): ").strip().title()

        if ambulance_road not in roads:
            print("invalid road !! try again")
            continue

        print("ambulance detected on :", ambulance_road)
        for road in roads:
            if road == ambulance_road:
                print("Green:", road)
            else:
                print("RED:", road)

        time.sleep(Emergency_Time)
        print("emergency phase completed<3")

    elif choice == "3":
        print("traffic system stopped.")
        break
        
    else:
        print("invalid choice !!\n choice must be in 1,2 or 3 !!")