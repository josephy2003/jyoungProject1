courses_file =open("requiredCS.txt", 'r')
lines_from_file = courses_file.readlines()
for line in lines_from_file:
    loud_line = line.upper()
    loud_line = loud_line.strip()
    print(loud_line)
print("Those are the classes you HAVE to take for the CS major")
