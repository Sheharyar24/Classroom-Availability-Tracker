import pandas as pd

# Read the text file
with open("timetable.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip() and line.strip() not in ["OR", "AND", "code misma"]]

# Each record has 6 lines: Type, Day, Start, End, Location, Lecturer
records = [lines[i:i+6] for i in range(0, len(lines), 6)]

# Convert into DataFrame
df = pd.DataFrame(records, columns=["Type", "Day", "Start Time", "End Time", "Room", "Lecturer"])

# Save and display
print("Done!")
print(len(df))
df.to_csv("timetable.csv", index=False)
