# CtrlQueueI (Int) Interface

&nbsp;

This interface can be used to read/modify the properties of the CtrlQueue Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t CtrlQueueI(int32\_t Parameter, int32\_t argument)

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: CtrlQueue.ClearQueue

This parameter clears the control queue.

&nbsp;

### Parameter 1: CtrlQueue.Delete

This parameter deletes a control action from the DSS control queue by referencing the handle of the action (Argument).

&nbsp;

### Parameter 2: CtrlQueue.NumActions

This parameter gets the number of actions on the current action list (that have been popped off the control queue by CheckControlActions).

&nbsp;

### Parameter 3: CtrlQueue.Action

This parameter sets the active action by index (argument).

&nbsp;

### Parameter 4: CtrlQueue.ActionCode

This parameter gets the code for the active action. Long integer code to tell the control device what to do.

&nbsp;

### Parameter 5: CtrlQueue.DeviceHandle

This parameter gets the handle (user defined) to device that must act on the pending action.

&nbsp;

### Parameter 6: CtrlQueue.Show

This parameter shows the entire control queue in CSV format.

&nbsp;

### Parameter 7: CtrlQueue.ClearActions

This parameter clears the action list.

&nbsp;

### Parameter 8: CtrlQueue.PopAction

This parameter pops next action off the action list and makes it the active action. Returns zero if none.

&nbsp;

### Parameter 9: CtrlQueue.QueueSize

This parameter delivers the size of the current control queue. Returns zero if none.

&nbsp;

### Parameter 10: CtrlQueue.DoAllQueue

This parameter forces the execution of all control actions stored at the control queue. Returns 0.


***
_Created with the Standard Edition of HelpNDoc: [Write eBooks for the Kindle](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
