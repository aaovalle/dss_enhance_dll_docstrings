# Default Values 

&nbsp;

When a New command results in the instantiation of a DSS element, the element is instantiated with reasonable values. Only those properties that need to be changed to correctly define the object need be included in the command string. Commonly, only the bus connections and a few key properties need be defined. Also, a new element need not be defined in one command line. It may be edited as many times as desired with subsequent commands (see Edit, More and ~ commands).

&nbsp;

When an element is created or selected by a command, it becomes the Active element. Thereafter, property edit commands are passed directly to the active element until another element is defined by the New command or selected by some other command. In that respect, the command language mirrors the basic [COM interface](<COMInterface.md>).

&nbsp;

All changes are persistent. That is, a parameter changed with one command remains as it was defined until changed by a subsequent command. This might be a source of misunderstanding with novices using the program who might expect values to reset to a base case as they do in some other programs. When this is a concern, issue a “clear” command and redefine the circuit from scratch.

***
_Created with the Standard Edition of HelpNDoc: [Add an Extra Layer of Security to Your PDFs with Encryption](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
