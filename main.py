import pandas as pd

df = pd.read_csv('timetable.csv')

all_rooms = sorted(df["Room"].unique())

day_start = "08:30"
day_end = "18:30"
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def to_time(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

# Open a file for writing
with open('room_availability.txt', 'w') as file:
    file.write("All rooms: " + str(all_rooms) + "\n")
    file.write("A Total of: " + str(len(all_rooms)) + " rooms\n")
    
    for room in all_rooms:
        file.write(f"\nRoom {room} availability:\n")
        for day in days:
            day_classes = df[(df["Room"] == room) & (df["Day"] == day)]
            if day_classes.empty:
                file.write(f"  {day}: Available all day\n")
                continue
            
            # Sort by start time
            day_classes = day_classes.sort_values(by="Start Time")
            
            current_time = to_minutes(day_start)
            end_of_day = to_minutes(day_end)
            
            for index in range(len(day_classes)):
                class_info = day_classes.iloc[index]
                class_start = to_minutes(class_info["Start Time"])
                class_end = to_minutes(class_info["End Time"])
                
                # If there's a gap before the class starts
                if current_time < class_start:
                    file.write(f"  {day}: Available from {to_time(current_time)} to {class_info['Start Time']}\n")
                
                # Updates the current time to the end of the class if it's later
                current_time = max(current_time, class_end)
            
            # If there's time left after the last class
            if current_time < end_of_day:
                file.write(f"  {day}: Available from {to_time(current_time)} to {day_end}\n")

print("Output saved to room_availability.txt")