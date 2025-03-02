# NumCores

&nbsp;

Returns the number of physical processors (Cores) available in the computer. If the computer has less than 64 CPUs the number of cores will be the half of the number of CPUs (2 threads per Core), otherwise, these numbers will be the same. This is a read-only value and must be executed using the “Get” command. The value is returned in the Result string in the EXE version and the @result variable for the text scripting interface. The string is also available in the Result property of the Text interface in the COM interface and the result of the DSSPut\_Command function of the DLL interface. The number of Cores will be equal to the number of number of physical cores of the active processor multiplied by the number of NUMA nodes.

***
_Created with the Standard Edition of HelpNDoc: [How to Protect Your PDFs with Encryption and Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
