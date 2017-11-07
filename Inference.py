#
#  Inference module:
#  -	Applies the fuzzy rules to the fuzzy values from the fuzzifier module
#  -	Will use max-min composition
#  -	Aggregates all the fuzzy values and passes them to the defuzzifier module


class Rule:
    def __init__(self, ruleasstring):
        #  rule should be in format
        #  Rule <rulename> if <antecedence> then <concequence>
        #  concequence should be in format
        #  <variable> is <value>
        #  antecedence should be in format
        #  <variable1> is <value1> [and|or] [<variablen> is <valuen>]
        ruleaslist = ruleasstring.split()
        self.rulename = ruleaslist[1]
        self.antecedence = []
        antecedenceindex = ruleaslist.index("if")
        antecedentreading = True
        concequencereading = False
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
