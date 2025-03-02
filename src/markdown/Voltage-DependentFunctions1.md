# “Voltage-Dependent” Functions

These are the functions which are defined through an InvControl CE. This section intends to provide a quick presentation of how they can be enabled and interact with each other. For a detailed explanation of their implementation, see \[[2](<References7.md#\_bookmark21>)\]. The “voltage-dependent functions” currently implemented in InvControl are:

&nbsp;

* **Volt-Watt (VW)**: it can be enabled in two different ways. If operating alone, by setting InvControl’s *mode* property to VW. If operating with VV, by setting InvControl’s *combimode* property to VV VW;
* &nbsp;
* **Volt-Var (VV)**: it can be enabled in three different ways. If operating alone, through In- vControl’s *mode* property, by setting it to VV. If operating with DRC, by setting InvControl’s *combimode* property to VV DRC. If operating with VW, by setting *combimode* to VV VW;
* &nbsp;
* **Dynamic Reactive Current (DRC)**: it can be enabled by two different ways. If operating alone, by setting InvControl’s *mode* property to DRC. If operating with VV, by setting InvControl’s *combimode* property to VV DRC;


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
