import csv
with open('Ind_Loc.csv') as Inputcsv:
    csvreader = csv.reader(Inputcsv,delimiter=',')
    read = list(csvreader)

with open('Mumbai_Data.csv','a') as Outputcsv:
    csvwriter = csv.writer(Outputcsv, delimiter=',')
    try:
        for row in read:
            latlong = list([row[4],row[5]])
            if 19.5 >= float(latlong[0]) >= 18.9:
                if 73.37 >= float(latlong[1]) >= 72.7:
                    csvwriter.writerow([row[1],latlong[0],latlong[1]])

    except:
        print "No LatLong"








