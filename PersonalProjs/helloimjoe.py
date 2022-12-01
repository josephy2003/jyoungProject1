courses_file =open("helloimjoe.txt", 'r')
lines_from_file = courses_file.readlines()
for line in lines_from_file:
    loud_line = line.upper
    loud_line = loud_line.strip()