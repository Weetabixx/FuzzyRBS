#
#  Inference module:
#  -	Applies the fuzzy rules to the fuzzy values from the fuzzifier module
#  -	Will use max-min composition
#  -	Aggregates all the fuzzy values and passes them to the defuzzifier module


class Rule:
    # rulename
    # antecedence (list of pairs)
    # connective [and|or|none]
    # convariable
    # convalue
    def __init__(self, ruleasstring):  # sets up the rules
        #  rule should be in format
        #  Rule <rulename> if <antecedence> then <concequence>
        #  concequence should be in format
        #  the <variable> will be <value>
        #  antecedence should be in format
        #  the <variable1> is <value1> [and|or] [the <variablen> is <valuen>]
        try:
            ruleaslist = ruleasstring.split()
            length = len(ruleaslist)
            self.rulename = ruleaslist[1]
            self.antecedence = []
            antecedenceindex = ruleaslist.index("If")
            antecedentreading = True
            concequencereading = False
            if "and" in ruleaslist:
                self.connective = "and"
            elif "or" in ruleaslist:
                self.connective = "or"
            else:
                self.connective = "none"
            while antecedentreading:
                antecedenceindex += 1
                if ruleaslist[antecedenceindex] == "then":  # if we reached the end of the antecedence
                    antecedentreading = False
                    concequenceindex = antecedenceindex
                    concequencereading = True
                    break
                elif ruleaslist[antecedenceindex] == "the":  # means the start of a variable and value pairing
                    antecedenceindex += 1
                    antevariable = ruleaslist[antecedenceindex]
                    antecedenceindex += 1
                    if ruleaslist[antecedenceindex] == "is":
                        antecedenceindex += 1
                        antevalue = ruleaslist[antecedenceindex]
                        self.antecedence.append((antevariable, antevalue))
            if concequencereading:
                concequenceindex += 2
                self.convariable = ruleaslist[concequenceindex]
                concequenceindex += 3
                self.convalue = ruleaslist[concequenceindex]
        except IndexError:
            print("that rule did'nt make any sense")

    def andoror(self, values):  # max-min the values
        if self.connective == "and":
            return max(values)
        else:
            return min(values)

    def fire(self, variablevalues):             # takes a dictionary of the non zero fuzzy dimensions with their sets and membershipness,
        values = []                             # returns triple of consequence and fire value
        for antpair in self.antecedence:
            values.append(variablevalues[antpair[0]][antpair[1]])
        firevalue = self.andoror(values)
        r = (self.convariable, self.convalue, firevalue)
        return r

