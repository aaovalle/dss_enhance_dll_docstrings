# Support routines and global context

There are libraries created for supporting specific OpenDSS functions that are required at different parts of the program. These libraries are implemented as subroutines (not objects) and depending on their purpose, are implement in specific files. The list of files and a brief description to them is given as follows:

| ***File name*** | ***Description*** |
| --- | --- |
| **Diakoptics.pas** | Implements the routines needed for solving the circuit model using spatial parallelization (A-Diakoptics). |
| **DSSCallBackRoutines.pas** | Implements the routines for connecting different routines across OpenDSS-X. |
| **DSSForms.pas** | Depending on the implementation (EXE, DLL, COM, Cmd), implements all the forms and graphical objects for providing feedback to the user. |
| **DSSGlobals.pas** | Includes all the global variables and routines to be used in the global context. It also includes the initialization for the global variables.&nbsp; |
| **ExportResults.pas** | Includes all the routines for exporting results and information about the simulation. |
| **KLUsolve.pas** | Implements the calls and connections to the solver DLL (KLUSolve). |
| **Notes.pas** | Contains notes from the developers, not actively updated. |
| **ShowResults.pas** | Includes all the routines for exporting results and information about the simulation. It is like ExportResult.pas, however, in this case, once the reports are exported, they will show up using the default editor (normally Notepad). |
| **SolutionAlgs.pas** | Implements the solution algorithms required for implementing the different solution modes available in OpenDSS-X. |
| **TOPExport.pas** | Implements the routines for exporting simulation results compatible with TOP. |
| **Utilities.pas** | Implements multiple routines for extracting circuit data in specific formats, fixing strings, navigate the circuit model, perform specific calculations based on the simulation results, among others. |
| **YMatrix.pas** | Implements the routines for creating, initializing, storing, and freeing sparse matrices. |
| **Arraydef.pas** | Implements the structures and pointers used across the program for storing arrays of elements. |
| **Mathutil.pas** | Implements special mathematical routines that can be used for translating electrical quantities into other formats. |
| **UCmatrix.pas** | Implements the structure and operation that can be applied to complex matrices in OpenDSS-X. |
| **Ucomplex.pas** | Implements linear algebra, domain conversion, and mathematical operations with complex numbers.&nbsp; |



***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Creation with a Help Authoring Tool](<https://www.helpndoc.com>)_
