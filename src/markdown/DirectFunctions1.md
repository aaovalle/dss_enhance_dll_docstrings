# “Direct Functions”

In the OpenDSS environment, these are the functions specified within the PCE definition. They are the following:

&nbsp;

* **Limit DER Power**: this function establishes an upper limit on the real power that the DER can produce/discharge and charge at its interface with the grid \[[6](<References7.md#\_bookmark25>)\]. For Storage, it is specified by the property %*kWRated*, which currently applies to both charging and discharging states. For PVSystems, it is specified through property %*Pmpp* (as a percentage of *Pmpp*). In both cases, the default value is 100, which means that this function is disabled.

&nbsp;

* **Constant Power Factor (PF)**: it can be enabled by defining the property *pf* of the PCE. The sign convention used in OpenDSS dictates that a positive *pf* means reactive power in the same direction as active power. On the other hand, a negative *pf* means reactive power and active power with opposed signs. Note that for Storage elements, it means that, for a given *pf* , as it charges and discharges the reactive power sign is changed accordingly. For instance, assume that a positive *pf* has been specified and the selected operation mode dictates that the element should charge at the beginning of the day and discharge in the evening. In this case, there would be vars absorption and generation, respectively. Also, during operation in idling state, the reactive power dispatched by a storage element is calculated based on the specified idling losses, if any.

&nbsp;

* **Constant Reactive Power (kvar)**: it can be enabled by defining the property *kvar* at the DER element. The sign follows the generator convention, i.e., a positive *kvar* means generated vars whereas a negative *kvar* means absorbed vars.


***
_Created with the Standard Edition of HelpNDoc: [Easily create PDF Help documents](<https://www.helpndoc.com/feature-tour>)_
