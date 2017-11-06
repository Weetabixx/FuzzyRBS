#
#  Input module:
#  -	Divides text into fuzzy rule base, membership functions and crisp input
#  -	Passes fuzzy rules to the inference module
#  -	Passes membership functions to fuzzifier (as a set of 4 tuples)
#  -	Passes crisp input to fuzzifier
#  -	Passes membership functions to defuzzifier

# read file
print("what file contains the input?")
filename = input()
inputfile = open(filename, 'r')
inputlines = []
with inputfile as f:
    inputlines = f.readlines()
inputfile.close()
print(inputlines)
numberoflines = len(inputlines)
ruleBaseName = ""  # name of the rulebase, always first line of text file
ruletexts = []  # the rules as strings
fuzzysetmembertexts = {}  # the fuzzy set memberships as strings in a dictionary
variables = {}  # the variables in a dictionary

ruleBaseName = inputlines[0].rstrip()  # read the name of the rule base

currentline = 2
readvariables = True
readfuzzysets = True
readrules = True
while readrules:  # read all the rules
    if inputlines[currentline] == '\n':
        readrules = False
    elif 'Rule' in inputlines[currentline]:
        ruletexts.append(inputlines[currentline].rstrip())
    else:
        print("dont understand line " + str(currentline))
    currentline += 1
    if currentline == numberoflines:
        readrules = False
        readfuzzysets = False
        readvariables = False
print(ruletexts)
print(len(ruletexts))

currentdimension = ""
while readfuzzysets:  # read the fuzzy sets and their definitions
    if '=' in inputlines[currentline]:
        readfuzzysets = False
        break
    elif inputlines[currentline] == '\n':
        pass
    elif len(inputlines[currentline].split()) > 1:
        fuzzysetmembertexts[currentdimension].append(inputlines[currentline].rstrip())
    else:
        currentdimension = inputlines[currentline].rstrip()
        fuzzysetmembertexts[currentdimension] = []
    currentline += 1
    if currentline == numberoflines:
        readrules = False
        readfuzzysets = False
        readvariables = False
print(fuzzysetmembertexts)

while readvariables:
    if '=' in inputlines[currentline]:
        variableline = inputlines[currentline].split(" = ")
        variables[variableline[0]] = float(variableline[1])
    currentline += 1
    if currentline == numberoflines:
        readrules = False
        readfuzzysets = False
        readvariables = False
print(variables)

# create fuzzy sets and their membership functions


# send variables to fuzzy sets


# send fuzzy rules to inference engine


# tell inference engine to use fuzzy values to infere and aggregate


# tell defuzzify module to deffuzzify the output of the inference engine
