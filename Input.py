from FuzzySet import FuzzyDimension
from Inference import Rule
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
numberoflines = len(inputlines)
ruleBaseName = ""  # name of the rulebase, always first line of text file
ruletexts = []  # the rules as strings
fuzzysetmembertexts = {}  # the fuzzy set memberships as strings in a dictionary
variables = {}  # the variables in a dictionary

ruleBaseName = inputlines[0].rstrip()  # read the name of the rule base
print("Rules Base:")
print(ruleBaseName)

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
print("rules:")
print(ruletexts)

currentdimension = ""
while readfuzzysets:  # read the fuzzy sets and their definitions
    if '=' in inputlines[currentline]:  # if we have reached the variables, stop
        readfuzzysets = False
        break
    elif inputlines[currentline] == '\n':  # skip the empty lines
        pass
    elif len(inputlines[currentline].split()) > 1:  # if there is more than one item on line it must be a fuzzy set
        fuzzysetmembertexts[currentdimension].append(inputlines[currentline].rstrip())
    else:  # if there is only one item it must be a new fuzzy dimension/ new set of fuzzy sets
        currentdimension = inputlines[currentline].rstrip()
        fuzzysetmembertexts[currentdimension] = []
    currentline += 1
    if currentline == numberoflines:
        readrules = False
        readfuzzysets = False
        readvariables = False
print("fuzzy sets:")
print(fuzzysetmembertexts)

while readvariables:
    if '=' in inputlines[currentline]:  # if the line contains a variable
        variableline = inputlines[currentline].split(" = ")
        variables[variableline[0]] = float(variableline[1])
    currentline += 1
    if currentline >= numberoflines:  # if we reached the end of the file stop
        readrules = False
        readfuzzysets = False
        readvariables = False
print("variables:")
print(variables)

# create fuzzy sets and their membership functions and fuzzify variables
membershipofsets = {}  # this will contain the state of the membership-ness of every set
dimensions = {}  # this will contain the dimension objects
for dimension, fuzzysets in fuzzysetmembertexts.items():  # for each dimension and its fuzzy sets
    x = FuzzyDimension(dimension)
    membershipofsets[dimension] = {}
    for setastext in fuzzysets:  # for each fuzzy set in the dimension
        setaslist = setastext.split()
        setname = setaslist[0]
        memberships = (float(setaslist[1]), float(setaslist[2]), float(setaslist[3]), float(setaslist[4]))
        x.add_membership(setname, memberships)
        membershipofsets[dimension][setname] = 0   # initialise the membership of all sets to 0
        if dimension in variables.keys():
            # send variables to fuzzy sets
            membershipofsets[dimension][setname] = x.membership(setname,variables[dimension])
    dimensions[dimension] = x

# send fuzzy rules to inference engine
rules = []  # create a list of all rules
for ruleastext in ruletexts:
    r = Rule(ruleastext)
    rules.append(r)

# tell inference engine to use fuzzy values to infere and aggregate
results = []
for rule in rules:  # fire all the rules
    result = rule.fire(membershipofsets)
    results.append(result)
for concequence in results:  # aggregate all the values
    resultdimension = concequence[0]
    resultset = concequence[1]
    resultvalue = concequence[2]
    membershipofsets[resultdimension][resultset] = max(membershipofsets[resultdimension][resultset], resultvalue)

# deffuzzify the output of the inference engine
crispdimensionvalues = {}
for dimensionname, fuzzysetlist in membershipofsets.items():
    dimensionvalue = 0
    dimensionset = ""
    for fset, fvalue in fuzzysetlist.items():  # selects the fuzzy set with the highest membership
        if fvalue > dimensionvalue:
            dimensionvalue = fvalue
            dimensionset = fset
    if dimensionset == "":  # check there is a fuzzy set
        print("couldn't find an answer to" + dimensionname)
    else:
        crisp = dimensions[dimensionname].meanofmax(dimensionset)
        crispdimensionvalues[dimensionname] = crisp
print("fuzzy sets used:")
print(membershipofsets)
print("crisp output:")
print(crispdimensionvalues)
