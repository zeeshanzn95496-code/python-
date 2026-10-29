import time 
roads = ["North", "East", "South", "West"]

Normal_Time = 5
Emergency_Time = 3

while True:
    print("\n++++++ TRAFFIC SIGNAL SYSTEM ++++++")
    print("1. NORMAL TRAFFIC")
    print("2. AMBULANCE EMERGENCY")
    print("3. EXIT ")

    choice = input("ENTER YOUR CHOICE: ")

    if choice == "1":
        for road in roads:
            print("\n    GREEN:    ", road)
            for other_road in roads:
                if other_road != road:
                    print("RED:", other_road)
            time.sleep(Normal_Time)

    elif choice == "2":
        ambulance_road = input("ENTER AMBULANCE ROAD FIRST WORD IN CAPITAL (North/East/South/West): ").strip().title()

        if ambulance_road not in roads:
            print("INVALID CHOICE!! TRY AGAIN")
            continue

        print("AMBULANCE DETECTED ON:", ambulance_road)
        for road in roads:
            if road == ambulance_road:
                print("Green:", road)
            else:
                print("RED:", road)

        time.sleep(Emergency_Time)
        print("emergency phase completed<3")

    elif choice == "3":
        print("++++++ TRAFFIC SYSTEM STOPPED  ++++++.")
        break
        
    else:
        print("INVALID CHOICE!!\n CHPICE MUST BE IN  1,2 or 3 !!")