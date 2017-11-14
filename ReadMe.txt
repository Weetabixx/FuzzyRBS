to run the fuzzy rule based system, create an input file with any name, it should have the same layout and format as
SampleInput.txt
the rules should be in the format of:
Rule <rulename> If the <variable> is <fuzzy-set> [[and|or] the <variable> is <fuzzy-set>] then the <variable> will be <fuzzy set>
each rule or definition should be contained to one line
the variable defenitions should be in the format of:
<variable>

<fuzzy set> <a value> <b value> <alpha value> <beta value>
...
...

<variable>

...

note that the whitespaces are also important, also none of the variable or fuzzy set names should contain any = signs or
whitespaces in the name and the values need to be a number.
the input variables should have the format:
<variable> = <value>

once the input text file is created you should run $ python Input.py
and when prompted specify the input file
the prerequisite for running this system is python 3.5 or later