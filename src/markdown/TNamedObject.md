# TNamedObject

| ***TNamedObject*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Property- private** | Get\_QualifiedName | Returns the name of the caller including class. E.g. Load.myload. |
| **Property- private** | Get\_DisplayName | Returns the name to be displayed for the caller, if not assigned, returns the class, underscore character and element names. |
| **Property- private** | Set\_DisplayName | Sets the name to be displayed (different from the objects name) for the caller. |
| **Property- private** | Get\_UUID | Returns the unique identifier for the caller object. |
| **Property- private** | Get\_ID | Returns the unique identifier for the caller object as a string. |
| **Property- private** | Set\_UUID | Sets the unique identifier for the caller object. |
| **property- public** | DSSClassName | Returns the name of the class the caller belongs to. |
| **property- public** | LocalName | PA the objects name within the circuit. It is not the class nor display name. E.g. load.myload, LocalName = myload. |
| **property- public** | QualifiedName | PA Get\_QualifiedName. |
| **property- public** | DisplayName | PA Get\_DisplayName, Set\_DisplayName. |
| **property- public** | UUID | PA Get\_UUID, Get\_UUID. |
| **property- public** | ID | PA Get\_ID. |
| **property- public** | CIM\_ID | Returns the string defining the CIM\_ID for the caller object. |



***
_Created with the Standard Edition of HelpNDoc: [Converting Word Docs to eBooks Made Easy with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
