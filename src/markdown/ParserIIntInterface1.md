# ParserI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t ParserI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Parser.IntValue

This parameter return next parameter as a long integer.

&nbsp;

### Parameter 1: Parser.ResetDelimeters

This parameter reset delimiters to their default values.

&nbsp;

### Parameter 2: Parser.AutoIncrement read

In this parameter the default is false (0). If true (1) parser automatically advances to next token after DblValue, IntValue, or StrValue. Simpler when you don't need to check for parameter names.

&nbsp;

### Parameter 3: Parser.AutoIncrement write

With this parameter the user can set the Auto increment value. Default is false (0). If true (1) parser automatically advances to next token after DblValue, IntValue, or StrValue. Simpler when you don't need to check for parameter names.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
