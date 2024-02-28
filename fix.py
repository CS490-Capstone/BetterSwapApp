import re

# The constants for the different types of sensors
# These values are for the working analyzer. 
FORCEPLATE = "01"
RAFT = "02"
TRACKER = "03"

# Get the values for the different sensors from the file
def getValues(file):
    with open(file, 'r') as f:
        for line in f:
            # The regex for the Raft sensor.
            if re.search(r'00\s\sRaft\s=\s\d+', line):
                print(line)
                raft = line[-3:].rstrip()
            
            # The regex for the Tracker sensor.
            if re.search(r'00\s\sTracker\s=\s\d+', line):
                print(line)
                tracker = line[-3:].rstrip()

            # The regex for the ForcePlate sensor.
            if re.search(r'00\s\sBertecForcePlate_Recorder\s=\s\d+', line):
                print(line)
                forceplate = line[-3:].rstrip()
                
    return {
        "raft": raft,
        "tracker": tracker,
        "forceplate": forceplate
    }

def main():
    inputFile = "Tyler123456none120male2006.txt" # the input file with incorrect format
    outputFile = "text.txt" # the output file with the correct format
    
    file = open(inputFile, 'r') 
    newFile = open(outputFile, 'w') 

    oldVals = getValues(inputFile)
    print(oldVals)
    
    # Read each line in the file to make changes.
    for line in file: 
        if line[0:2] == oldVals['tracker']:
            line = line.replace(oldVals['tracker'], TRACKER) 
        elif line[0:2] == oldVals["raft"]:
            line = line.replace(oldVals["raft"], RAFT)
        elif line[0:2] == oldVals["forceplate"]:
            line = line.replace(oldVals["forceplate"], FORCEPLATE)
        newFile.write(line)
        
    file.close()
    newFile.close()
main()