# TDSSClass

| ***TDSSClass*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Method- private** | Set\_active | Sets the class/element given by index at the argument active. |
| **Property-private** | Get\_Element | Returns a pointer to the element’s index given in the argument. |
| **Property-private** | Get\_First | Returns the index of the first element in the list for the active class. If none, returns 0. Lists start in 1. |
| **Property-private** | Get\_Next | Returns the index of the next element in the list of for the active class. If none, returns 0. Lists start in 1. |
| **Property-protected** | AddObjectToList | Adds a new object to the list of the active class. |
| **Property-protected** | Get\_FirstPropertyName | Returns the name of the first property of the active element. Sets the element’s property cursor in 1. If none, returns 0. |
| **Property-protected** | Get\_NextPropertyName | Returns the name of the next property of the active element. increments the element’s property cursor in 1. If none, returns 0. |
| **Property-protected** | MakeLike | Created as reference for copying the properties of another element into the caller. It needs to be detailed at a more specific class. |
| **Method-protected** | CountProperties | Counts the number of properties defined for the caller. |
| **Method-protected** | AllocatePropertyArrays | Allocates memory for storing the property arrays of the caller. |
| **Method-protected** | DefineProperties | Created for adding a property to the caller. |
| **Property-protected** | ClassEdit | Routine to continue parsing with contents of Parser. |
| **Method-public** | AddProperty | Helper routine for building Property strings |
| **Method-public** | ReallocateElementNameList | Reallocate the device name list to improve the performance of searches. |
| **Property- public** | Edit | Implements the base for editing the caller’s properties. The content of this routine needs to be defined at local level for the caller. Reaching this instance produces an error. |
| **Property- public** | Init | Implements the base for initializing the caller’s properties and variables. The content of this routine needs to be defined at local level for the caller. Reaching this instance produces an error. |
| **Property- public** | NewObject | Implements the routine for adding a new element to the list of the active class. |
| **Property- public** | SetActive | Activates an element within the active class by name. |
| **Property- public** | GetActiveObj | Returns a pointer to the active element within the active class. |
| **Property- public** | Find | Returns a pointer to the element’s name given in the argument. If not found, the pointer will be NULL (nil). |
| **Property- public** | PropertyIndex | Returns the index of the property name given in the argument. If not found, returns 0. |
| **Property-public** | FirstPropertyName | Returns the index to the first property in the property list for the active element. PA the same routine in the private/protected context. |
| **Property-public** | NextPropertyName | Returns the index to the next property in the property list for the active element. PA the same routine in the private/protected context. |
| **Property-public** | Active | Set/get by index the active element in the active class. |
| **Property-public** | ElementCount | Returns the number of elements within the active class. |
| **Property-public** | First | Activates the first element of the list for the active class. Returns 1 if success, otherwise, returns 0. |
| **Property-public** | Next | Activates the next element of the list for the active class. Returns the elements index if success, otherwise, returns 0. |
| **Property-public** | Name | Returns the name of the active class. |



***
_Created with the Standard Edition of HelpNDoc: [Say Goodbye to Documentation Headaches with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
