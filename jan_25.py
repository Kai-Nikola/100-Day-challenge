import csv

with open("data.csv") as file:
    # writer = csv.writer(file)
    # writer.writerow(["Employee_Name","Employee_ID"])
    # writer.writerow(["Neha",50625])
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
