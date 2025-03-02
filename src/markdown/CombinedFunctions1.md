# Combined Functions

OpenDSS allows the combination of some functions. They are the following:

* **PF + VW**: to enable this mode, define a power factor in a DER element and enable VW function at the InvControl element (property *mode*) responsible for controlling the corresponding DER. If VW limits the active power output, the constant power factor will be applied on top of the limited active power, such that at the interface with the grid, the constant power factor desired will be kept constant. The same applies if the active power is further limited by the Limit DER Power function;

&nbsp;

* **kvar + VW**: to enable this mode, define a kvar in a DER element and also enable VW function at the InvControl element (property *mode*) responsible for controlling the corresponding DER;

&nbsp;

* **VV + VW**: to enable this mode, use an InvControl element (property *combimode*) responsible for controlling the corresponding DER. If the inverter capability curve has not been exceeded, the power exchanged with the grid will be the desired active power, which might be limited by the VW function, and the reactive power requested by the VV function;

&nbsp;

* **VV + DRC**: to enable this mode, use an InvControl element (property *combimode*) responsible for controlling the corresponding DER. If the inverter capability curve has not been exceeded, the power exchanged with the grid will be the desired active power and the sum of the reactive power requested by the VV and DRC functions individually;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Efficiency with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
