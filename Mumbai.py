import re
import csv

#Empty list for storing all the places and their lat longs, in Mumbai.
placelist = []

#Mumbai_Data a csv which consists of all the places and their lat longs, in Mumbai.
with open('Mumbai_Data.csv','r') as csvfile:
    DATABASE = list(csv.reader(csvfile,delimiter=','))

#storing all the data from Mumbai_Data.csv into a list
for DATA in DATABASE:
    place = {}
    place['name'] = DATA[0]
    place['lat'] = DATA[1]
    place['lon'] = DATA[2]
    placelist.append(place)

#simple.txt a text file which has the content to be searched for locations.
with open("simple.txt") as txtfile:
    contents = txtfile.readlines()

i = 0
for content in contents:
    try:
        i = i + 1

        #regex to find words in the content which comes after the words 'at,in,to,from' or after a comma. In any article
        #In any article these are the common words before a place's name#
        Allwords = re.findall('(?<=at )\w+|(?<=from )\w+|(?<=in )\w+|(?<=, )\w+|(?<=to )\w+',content)

        #checks whether any of the above found words matches a place's name from the database.
        #if match found print its name, latutide and longitude.
        for p in placelist:
            if p['name'] in Allwords:
                print(p['name'],p['lat'],p['lon'])
        print str(i)+" Article Over"
    except:
        print "Fail"
