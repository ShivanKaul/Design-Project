import sys
import filterPhys

data = filter(sys.argv[1])
newFile = open('./filtered', 'w+')
newFile.write(data)
