"""
Name: Caleb Quattlebaum
traffic.py

Purpose: Recieve data from the DOT and calculate average number of vehicles that travel each road
         per day and the overall number and average number of vehicles that have traveled over all
         roads

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    cars_acc = 0
    total_acc = 0
    roads_surveyed = eval(input("How many roads were surveyed? "))
    for roads in range(roads_surveyed):
        num_days = eval(input("How many days was road " + str(roads + 1) + " surveyed? "))
        for days in range(num_days):
            cars = eval(input("How many cars traveled on day " + str(days + 1) + " ? "))
            cars_acc = cars_acc + cars
        road_avg = cars_acc / num_days
        print("Road", (roads + 1), "average vehicles per day: ", str(round(road_avg, 2)))
        total_acc = total_acc + cars_acc
        cars_acc = 0
    total_avg = total_acc / roads_surveyed
    print("Total number of vehicles traveled on all roads: ", total_acc)
    print("Average number of vehicles per road: ", str(round(total_avg, 2)))


if __name__ == "__main__":
    main()
