# Follow

As the name suggests, in this mode, storage charging and discharging follow a loadshape until the storage is either fully charged or discharged. As in the Default mode, the specified loadshape must correspond to the present solution mode (properties *daily*, *yearly* and *dutycycle*). For positive values, the storage is set to discharge and for negative values it is set to charge. A zero value sets the element to idling state. Contrary to the Default mode, the charging and discharging rates are variable and determined by the multiplication of the rated active power of the element, *kWrated*, and the multipliers from the loadshape.


***
_Created with the Standard Edition of HelpNDoc: [Make Documentation Review a Breeze with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
