import csv

# Used to convert the csv files to give heart rate, skin and time


class Convertom:
    heart = []
    breath = []
    time = []

    def __init__(self, infile):
        self.infile = infile
        self.clear()

    def generate(self):
        baseline_index = 1

        file = csv.reader(self.infile, delimiter='\n')
        for row in file:
            # A row as converted by csv.reader is actually a single item
            # list of string
            # We need to get the item and split it on the comma
            row = row[0].split(',')
            if(row[1] != 'nan'):
                row = map(float, row)
                self.heart.append(row[1])
                self.breath.append(row[2])
                self.time.append(row[0])
            elif (not row[0]):
                print 'Found baseline!'
                baseline_index = len(self.time)
                print baseline_index 
            else:
                self.heart.append(0.0)
                self.breath.append(float(row[2])) 
                self.time.append(float(row[0]))                  

        # Get average values of heart and skin up to baseline
        avgHeart = sum(self.heart[:baseline_index]) / baseline_index
        avgSkin = sum(self.breath[:baseline_index]) / baseline_index

        # Get diff of heart and skin values
        diffedHeart = map(lambda x: x - avgHeart,
                          self.heart[baseline_index:])
        diffedBre = map(lambda x: x - avgSkin,
                         self.breath[baseline_index:])
        diffedTime = self.time[baseline_index:]

        # Zip all lists. We have the tag for the file, and we replicate that
        # into a list of the same size as the other 3 lists
        return zip(diffedTime, diffedBre, diffedHeart)

    def clear(self):
        self.heart[:] = []
        self.breath[:] = []
        self.time[:] = []
