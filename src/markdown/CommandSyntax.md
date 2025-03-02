# Command Syntax

&nbsp;

The command language is of the form:&nbsp;

&nbsp;

Command parm1, parm2 parm3 parm 4 ….&nbsp;

&nbsp;

Parameters (parm1, etc) may be separated by commas (,) or white space (blank, tab). If a parameter includes a delimiter, enclose it in either&nbsp;

&nbsp;

• Double quotes (“),&nbsp;

• Single quotes(‘), or&nbsp;

• Parentheses (… ), or..&nbsp;

• Brackets \[..\], or&nbsp;

• Braces {..}.&nbsp;

&nbsp;

While any of these will work, double or single quotes are preferred for strings. Brackets are preferred for arrays, and curly braces are preferred for in-line math.&nbsp;

&nbsp;

Note: Be careful of using parentheses on Windows for file names containing full path names because Windows uses the string (x86) for 32-bit programs in the default Program Files folders. Use some other delimiter. Double quotes work fine and are what Windows returns for a full path name when there are blanks in the name. Hint: Right-click on a file name in Windows explorer and select Copy as Path. You will get the full pathname in double quotes that you can use in OpenDSS anywhere a file name is expected.
***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
