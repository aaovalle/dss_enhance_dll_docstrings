# Calculation of the per-unit monitored voltage

&nbsp;

The monitored voltage in *pu*, *vmon*\[*t*\]*j*, applied to the smart inverter volt-var and volt-watt functions, is calculated using the monitored voltage in *V* , *Vmon*\[*t*\]*j*, through one of the options in the *voltage\_curvex\_ref* property shown below:

**–** For *rated*, the monitored voltage in *pu* is calculated according to [Equation 33](<OpenDSSDocumentation.md#\_bookmark37>).

&nbsp;

![Image](<lib/NewItem516.png>)

&nbsp;

&nbsp;

**–** For *avg*, the monitored voltage in *pu* is calculated according to [Equation 34](<OpenDSSDocumentation.md#\_bookmark38>).

&nbsp;

![Image](<lib/NewItem517.png>)

&nbsp;

**–** For *ravg*, the monitored voltage in *pu* is calculated according to [Equation 35](<OpenDSSDocumentation.md#\_bookmark39>).

&nbsp;

![Image](<lib/NewItem518.png>)

&nbsp;

Where:

&nbsp;

**–** *Vmonavg* \[*t*\] is the mean value of the monitored voltages in *pu* of the previous *m* time steps that can be stored in the moving window with length defined in the *avgwindowlen* property, as can be seen in [Equation 36](<OpenDSSDocumentation.md#\_bookmark40>).

&nbsp;

&nbsp;

![Image](<lib/NewItem519.png>)

&nbsp;

For instance, an averaging window with three time step length, *Vmonavg* \[*t*\] is calculated according to [Equation 37](<OpenDSSDocumentation.md#\_bookmark41>).

&nbsp;

![Image](<lib/NewItem520.png>)

For smart inverter DRC functions, the monitored voltage in *pu* is always calculated according to [Equation 38](<OpenDSSDocumentation.md#\_bookmark42>).

&nbsp;

&nbsp;

![Image](<lib/NewItem521.png>)

&nbsp;

&nbsp;

1. &nbsp;
   * **Calculation of the output active power desired in pu** The smart inverter functions watt- pf and watt-var do not depend on any voltage to operate, instead they just need the output active power desired. The output active power desired is the power that the inverter would provide or absorb if kVA rating of the inverter is not exceed. For the PVSystem, it is calculated as shown in the [Equation 39.](<Calculationoftheper-unitmonitore.md#\_bookmark43>)

&nbsp;

![Image](<lib/NewItem522.png>)

&nbsp;

Where:

![Image](<lib/NewItem523.png>)

&nbsp;

The base active power value used for those functions is the rated active power in which for the PVSystem is the Pmpp, according to the [Equation 40](<OpenDSSDocumentation.md#\_bookmark44>)

&nbsp;

![Image](<lib/NewItem524.png>)

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
