# Calculation of base values of power

&nbsp;

Two base values of reactive power are defined, one used when the reactive power is positive or provided. And another, when the reactive power is negative or absorbed. These values depend on the options of the *RefReactivePower* property as shown below:

* For *VARMAX*, the base values of reactive power are calculated according to [Equation 46](<Calculationofbasevaluesofpower.md#\_bookmark49>) and [Equation 47](<OpenDSSDocumentation.md#\_bookmark50>) to be used when the reactive power is positive (capacitive) and negative (inductive), respectively.

&nbsp;

![Image](<lib/NewItem530.png>)

&nbsp;

&nbsp;

![Image](<lib/NewItem531.png>)

* For *VARAVAL*, both base values are calculated according to [Equation 48](<OpenDSSDocumentation.md#\_bookmark51>).

&nbsp;

![Image](<lib/NewItem532.png>)

If *Qbase*\[*t*\]*j* calculated above results in 0, then *Qbase*\[*t*\]*j* is set to be equal to *kvarMax*.

The base value of active power depends on the options of the *VoltwattYAxis* property as shown below:

* For *PMPPPU*, the base value is equal to the *Pmpp* property of the PVSystem, as can be seen in the [Equation 49](<OpenDSSDocumentation.md#\_bookmark52>).

&nbsp;

![Image](<lib/NewItem533.png>)

&nbsp;

* For *PAVAILABLEPU*, the base value corresponds to the available active power of the PVSystem in the time step *t*, which is calculated according to [Equation 50](<OpenDSSDocumentation.md#\_bookmark53>).

&nbsp;

![Image](<lib/NewItem534.png>)

&nbsp;

&nbsp;

Where *Pdc*\[*t*\] = *Pmpp \* irradiance \* irradiance*\[*t*\] \* *PTCurve*(*Temperature*\[*t*\]), as shown in *Equation 1*.

* For *PCTPMPPPU*, the base value is calculated according to [Equation 51](<OpenDSSDocumentation.md#\_bookmark54>).

&nbsp;

![Image](<lib/NewItem535.png>)

&nbsp;

* For *KVARATING*, the base value corresponds to the kVA rating of the inverter, as can be seen in the [Equation 52](<OpenDSSDocumentation.md#\_bookmark55>).

&nbsp;

![Image](<lib/NewItem536.png>)

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
