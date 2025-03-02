# ParserS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr ParserS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Parser.CmdString read

This parameter gets a string to be parsed. Loading this string resets the parser to the beginning of the line. Then parse off the tokens in sequence.

&nbsp;

### Parameter 1: Parser.CmdString write

This parameter sets a string to be parsed. Loading this string resets the parser to the beginning of the line. Then parse off the tokens in sequence.

&nbsp;

### Parameter 2: Parser.NextParam

This parameter gets next token and return tag name (before = sign) if any. See Autoincrement.

&nbsp;

### Parameter 3: Parser.StrValue

This parameter returns next parameter as a string.

&nbsp;

### Parameter 4: Parser.WhiteSpace read

This parameter gets the characters used for White space in the command string. Default in blank and Tab.

&nbsp;

### Parameter 5: Parser.WhiteSpace write

This parameter sets the characters used for White space in the command string. Default in blank and Tab.

&nbsp;

### Parameter 6: Parser.BeginQuote read

This parameter gets the string containing the characters for quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "(\[{.

&nbsp;

### Parameter 7: Parser.BeginQuote write

This parameter sets the string containing the characters for quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "(\[{.

&nbsp;

### Parameter 8: Parser.EndQuote read

This parameter gets the string containing the characters, in order, that match the beginning quote characters in BeginQuote. Default is ")\]}.

&nbsp;

### Parameter 9: Parser.EndQuote write

This parameter sets the string containing the characters, in order, that match the beginning quote characters in BeginQuote. Default is ")\]}.

&nbsp;

### Parameter 10: Parser.Delimiters read

This parameter gets the string defining hard delimiters used to separate token on the command string. Default is , and =. The =  separates token name from token value. These override whitespaces to separate tokens.

&nbsp;

### Parameter 11: Parser.Delimiters write

This parameter sets the string defining hard delimiters used to separate token on the command string. Default is , and =. The =  separates token name from token value. These override whitespace to separate tokens.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
