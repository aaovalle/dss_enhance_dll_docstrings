# Including External Files

&nbsp;

There are two ways to include external scripts in an OpenDSS script

&nbsp;

\-The Compile command, which inserts another OpenDSS script at that location in the script file. The Compile command changes the default directory to the directory the external file is located in.

\-The Redirect command, which inserts another OpenDSS script at that location in the script file. The redirect command keeps the default directory as the directory of the source script calling the redirect command.

&nbsp;

Some properties, like the mult property found in LoadShapes, may require large lists of data which are inconvenient to include directly in the script or which come from an external source. The File capability, which is used in lieu of a traditional value, allows one to read in a file and use its contents as the value stream for an element. For example:

&nbsp;

LoadShape.LS1 mult=(File='Example.csv')

\
Refer to the OpenDSS help for additional information on the File capability and its sister functions sngFile and dblFile.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Keep Your PDFs Safe from Unauthorized Access with These Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
