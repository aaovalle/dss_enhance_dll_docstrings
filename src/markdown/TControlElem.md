# TControlElem

| ***TControlElem*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Method-protected** | Set\_ControlledElement | Stores a pointer to target circuit element. |
| **Method-protected** | RemoveSelfFrom ControlelementList | Remove this control from the control element list of the designated element. |
| **Method-protected** | Set\_MonitoredElement | Stores a pointer to the monitored element. |
| **Method-public** | Sample | Sample control quantities and set action times in Control Queue. |
| **Method-public** | DoPendingAction | Implements the routine for doing the action that is pending from last sampling. |
| **Method-public** | Reset | Implements the reference for resetting the control, it is expected to be overridden by more specific classes. |
| **Property-public** | ControlledElement | PA FControlledElement (variable) and Set\_ControlledElement. |
| **Property-public** | MonitoredElement | PA FMonitoredElement (variable) and Set\_MonitoredElement. |



***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
