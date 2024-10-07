def new_activity(data, activity, time):
    if activity not in data:
        data[activity] = [0]
    data[activity].append(int(time))
    data[activity][0] += int(time)
    
def total_time(data, activity):
    if (activity not in data):
        return 0
    return data[activity][0]

def top_activities(data):
    activities = list(data.keys())
    activities.sort(key=lambda x: data[x][0], reverse=True)
    return [(x, data[x][0]) for x in activities[:3]]

if __name__ == '__main__':
    data = {}

    while (True):
        comm = input("Enter a command: ")

        if comm == "exit":
            break

        elif comm == "new":
            activity = input("Enter the activity: ")
            time = input("Enter the time: ")
            if not time.isdigit():
                print("Time must be an integer.")
                continue
            new_activity(data, activity, time)

        elif comm == "total":
            activity = input("Enter the activity: ")
            print(total_time(data, activity))

        elif comm == "top":
            print(top_activities(data))

        else:
            print("Invalid command")
            print("Valid commands are: new, total, top, exit")