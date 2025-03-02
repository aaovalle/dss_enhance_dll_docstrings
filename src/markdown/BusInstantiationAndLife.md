# Bus Instantiation And Life 

&nbsp;

&nbsp;

One of the features of the OpenDSS that takes some getting used to for users familiar with other power system analysis platforms is that a Bus does not exist until it is needed for a solution or some other purpose. A list of buses is made from the presently enabled devices in the circuit. Then each bus is instantiated. Likewise, a bus may disappear during a simulation.&nbsp;

&nbsp;

The reason for this behavior of the OpenDSS is to avoid having to define all the buses in the problem ahead of time. This allows users a great deal of flexibility in simulating distribution circuits in which the topology is changing during the simulation. If you want to add a new bus, simply define a device that is connected to the bus or edit the bus connections of an existing device. Since the OpenDSS does not need to know the voltage bases to perform its solution, there is no need to define the base voltages ahead of time. However, the voltage bases are useful for reports and certain simulations. Just remember to set the voltage bases AFTER the buses exist and before the report is generated.&nbsp;

&nbsp;

Bus instantiation can be forced without performing a solution by issuing the “MakeBusList” command.&nbsp;

&nbsp;

The CalcVoltageBases command will automatically set the voltage bases where practical by performing a no-load power flow. The legal voltage bases for a problem are defined using the Set Voltagebases = \[array of voltagebases in kV L-L\].&nbsp;

&nbsp;

Otherwise, you can use the SetkVBase command to set the voltage base for a selected bus. Often, users will create separate script files with all the necessary SetkVBase commands. These execute quickly but are used only when it is difficult to automatically discern between two voltage bases in a problem.&nbsp;

&nbsp;

The bus list is reorganized whenever there is a change in the circuit.&nbsp;

&nbsp;

**Implications/Side Effects of Bus Instantiation Rules:**&nbsp;

&nbsp;

•&nbsp; You can’t define the voltage base for a bus until it exists. The CalcVoltageBases command is a solution type that will automatically instantiate all the buses currently defined.&nbsp;

•&nbsp; You can’t define a bus’s coordinates until the bus exists.&nbsp;

• Once the bus list exists, properties are automatically copied to new bus objects when a change occurs that requires rebuilding the bus list. However, if there are new buses created by the changes, they will not have any of the special properties such as voltage base or coordinates defined. That must be done subsequently, if necessary.&nbsp;

• It does not hurt to redefine base voltage or coordinates if there is any question whether they have the proper value.&nbsp;

• Once instantiated, a bus object will persist until another command forces rebuilding the bus list. Thus, if there are edits performed on the circuit elements, the bus list could be out of synch with the present configuration.&nbsp;

• There is also a Node list that is constructed at the same time as the bus list. The order of elements in the system Y matrix is governed by the order of the Node list. The Node list order is basically the order in which the nodes are defined during the circuit model building process.&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
