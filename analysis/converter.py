import csv

# Used to convert the csv files to give heart rate, skin and time


class Converter:
    heart = []
    skin = []
    time = []
    filtered_skin = []
    filtered_heart = []

    def __init__(self, infile, tag):
        self.infile = infile
        self.tag = tag
        self.clear()

    def generate(self):
        baseline_index = 1

        file = csv.reader(self.infile, delimiter='\n')
        for row in file:
            # A row as converted by csv.reader is actually a single item
            # list of string
            # We need to get the item and split it on the comma
            row = row[0].split(',')
            if (row[2]):
                row = map(float, row)
                self.heart.append(row[2])
                self.skin.append(row[1])
                self.time.append(row[0])
            elif (not row[0]):
                print 'Found baseline!'
                baseline_index = len(self.time)
                print baseline_index

        # Filter
        self.filtered_skin = self.filter(self.skin,
                                         q=590.0, r=50000.0, p=399900.0, k=0.0)
        self.filtered_heart = self.filter(self.heart,
                                          q=0.99, r=260.0, p=1000.0, k=0.0)

        # Get average values of heart and skin up to baseline
        avgHeart = sum(self.filtered_heart[:baseline_index]) / baseline_index
        avgSkin = sum(self.filtered_skin[:baseline_index]) / baseline_index

        # Get diff of heart and skin values
        diffedHeart = map(lambda x: x - avgHeart,
                          self.filtered_heart[baseline_index:])
        diffedSkin = map(lambda x: x - avgSkin,
                         self.filtered_skin[baseline_index:])
        diffedTime = self.time[baseline_index:]

        # Zip all lists. We have the tag for the file, and we replicate that
        # into a list of the same size as the other 3 lists
        return zip(diffedTime, diffedSkin, diffedHeart,
                   [self.tag] * len(diffedTime))

    def filter(self, mylist, q, r, p, k):
        x = mylist[0]
        filtered = []
        for i in xrange(len(mylist)):
            p = p + q
            k = p/(p + r)
            x = x + k*(mylist[i] - x)
            p = (1-k)*p
            filtered.append(x)
        return filtered

    def clear(self):
        self.heart[:] = []
        self.skin[:] = []
        self.time[:] = []
        self.filtered_heart[:] = []
        self.filtered_skin[:] = []
