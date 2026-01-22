#Raghav Vij 590023842
sec = int(input("Enter seconds: "))

hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
