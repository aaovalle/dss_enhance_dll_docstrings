# LinesI (Int) Interface

&nbsp;

This interface can be used to read/modify the properties of the Lines Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t LinesI(int32\_t Parameter, int32\_t argument)

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Lines.First

This parameter sets the first element active. Returns 0 if no lines. Otherwise, index of the line element.

&nbsp;

### Parameter 1: Lines.Next

This parameter sets the next element active. Returns 0 if no lines. Otherwise, index of the line element.

&nbsp;

### Parameter 2: Lines.Phases read

This parameter gets the number of phases of the active line object.

&nbsp;

### Parameter 3: Lines.Phases write

This parameter sets the number of phases of the active line object.

&nbsp;

### Parameter 4: Lines.NumCust

This parameter gets the number of customers on this line section.

&nbsp;

### Parameter 5: Lines.Parent

This parameter gets the parents of the active Line to be the active Line. Return 0 if no parent or action fails.

&nbsp;

### Parameter 6: Lines.Count

This parameter gets the number of Line Objects in Active Circuit.

&nbsp;

### Parameter 7: Lines.Units read

This parameter gets the units of the line (distance, check manual for details).

&nbsp;

### Parameter 8: Lines.Units write

This parameter sets the units of the line (distance, check manual for details).


***
_Created with the Standard Edition of HelpNDoc: [Eliminate the Struggles of Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
