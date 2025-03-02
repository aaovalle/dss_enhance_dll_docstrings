# Other objects

Other objects around OpenDSS are not descendants of the main classes in the program’s architecture (TNamedObject, TDSSClass), however, they play an important role during the simulation execution given the information they carryout. These types of objects are normally subclasses of containers or circuit elements that user them for storing data that is important during the simulation.

The elements are enumerated in the following list with a brief description of what they are used to:

| ***Object name*** | ***Description*** |
| --- | --- |
| **TControlQueue** | Stores the pending control actions uploaded by controls after sampling. Controls can push and pull actions from the control queue. |
| **TConductor** | It’s the basic structure for a conductor in OpenDSS-X. |
| **TExecutive** | Implements all the routines needed for executing a command string written in OpenDSS-X syntax. It is also responsible for creating the default items for OpenDSS-X. Executive is the first element to be created when trying to implement an OpenDSS-X global instance. |
| **TParser** | Implements the DSS parser that interprets strings in OpenDSS-X syntax and returns their equivalents as integer, floating-point numbers, arrays, and other structures. It also helps to identify classes and elements by name while processing a script. |
| **TRPNCalc** | Implements the Reverse Polish Notation solver used for solving mathematical expressions in OpenDSS-X. |
| **TCktTreeNode** | Implements the structure for storing and managing the circuit tree for topological operations and navigation. |
| **TCommandList** | Implements the structure for storing the command list for an element when gets created. |
| **THashList** | Implements the structure for creating hash lists. |
| **TPointerList** | Implements the structure for storing pointers. The pointer list gets populated while creating the circuit and allows to gain access to an element within the circuit through its pointer. |
| **TcMatrix** | Implements the structure for defining matrices within OpenDSS-X. It also implements linear algebra operations that can be applied to the active matrix or between matrices. |
| **TAutoAdd** | Unit for processing the AutoAdd Solution FUNCTIONs. |
| **TdJSON** | Implements a JSON serializer for Delphi provided by Thomas Erlang. |



***
_Created with the Standard Edition of HelpNDoc: [Easily create iPhone documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
