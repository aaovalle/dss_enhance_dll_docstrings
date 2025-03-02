# Calculation of the smart inverter function

In this section is to calculate the desired reactive power, *qDfun*\[*t*\]*j*, and/or the active power limit, *pLfun*\[*t*\]*j*, according to the modes below:

&nbsp;

**Smart Inverter volt-var Function** For the smart inverter volt-var function, the monitored voltage in *pu* is applied , *vmon*\[*t*\]*j*, in the volt-var curve defined in the *vvc\_curve1* property to obtain the desired reactive power value in *pu*, *qDfun*\[*t*\]*j*. The [Figure 9](<Calculationofthesmartinverterfun.md#\_bookmark58>) below shows an example of an user-defined volt-var curve.

The desired reactive power in *pu* can be written according to [Equation 53](<OpenDSSDocumentation.md#\_bookmark56>).

&nbsp;

![Image](<lib/NewItem537.png>)

&nbsp;

**Smart inverter DRC function** For the smart inverter DRC function, the desired reactive power value is set according to [Equation 54](<Calculationofthesmartinverterfun.md#\_bookmark57>).

&nbsp;

![A line graph with numbers and symbols

Description automatically generated](<lib/NewItem473.png>)

**Figure 9: volt-var curve**

&nbsp;

![Image](<lib/NewItem538.png>)

&nbsp;

Where the voltage difference is calculated according to [Equation 55](<Calculationofthesmartinverterfun.md#\_bookmark59>).

&nbsp;

![Image](<lib/NewItem539.png>)

&nbsp;

And *vwindowdrc* \[*t*\]*j* corresponds to the mean of the voltages of the averaging window of the DRC function. This average voltage is calculated according to [Equation 56](<OpenDSSDocumentation.md#\_bookmark60>) considering that the averaging window can store the voltages of *m* previous time steps. The time-scale length of this window is set in the *DynReacavgwindowlen* property.

&nbsp;

![Image](<lib/NewItem540.png>)

&nbsp;

&nbsp;

**Combined Smart inverter volt-var and DRC function** For the combined mode of the smart volt-var and DRC functions, the desired reactive power value is the sum of the result of [Equation 53](<OpenDSSDocumentation.md#\_bookmark56>) and [Equation 54](<Calculationofthesmartinverterfun.md#\_bookmark57>), according to [Equation 57](<OpenDSSDocumentation.md#\_bookmark61>).

&nbsp;

![Image](<lib/NewItem541.png>)

&nbsp;

**Smart inverter volt-watt function** For the smart inverter volt-watt function, the monitored voltage in *pu* is applied, *vmon*\[*t*\]*j*, in the volt-watt curve defined in the *voltwatt\_curve* property to obtain the active power limit value in *pu*, *pLfun*\[*t*\]*j*. The [Figure 10](<Calculationofthesmartinverterfun.md#\_bookmark62>) shows an example of a user-defined volt-watt curve.

&nbsp;

![A line graph with red line

Description automatically generated](<lib/NewItem472.png>)

**Figure 10: volt-watt curve**

&nbsp;

The active power limit value in *pu* is calculated as shown in the [Equation 58](<Calculationofthesmartinverterfun.md#\_bookmark63>).

&nbsp;

![Image](<lib/NewItem542.png>)

&nbsp;

**Smart inverter watt-pf function** For the smart inverter watt-pf function, the output active power in *pu* is applied, *pdesired*\[*t*\], in the watt-pf curve defined in the *wattpf\_curve* property to obtain the power factor, [Equation 59](<OpenDSSDocumentation.md#\_bookmark64>), and then calculate the desired reactive power value in *pu*, *qDfun*\[*t*\]*j*, according to [Equation 60](<OpenDSSDocumentation.md#\_bookmark65>). The [Figure 11](<Calculationofthesmartinverterfun.md#\_bookmark66>) shows an example of an user-defined watt-pf curve.

&nbsp;

![Image](<lib/NewItem543.png>)

&nbsp;

![Image](<lib/NewItem544.png>)

&nbsp;

&nbsp;

One can notice that the watt-pf curve, [Figure 11](<Calculationofthesmartinverterfun.md#\_bookmark66>), has the nominal/reference point in power factor 1 instead of 0. As a result, the user needs to define this watt-pf curve based on a curve that has its reference in power factor equal to 0, according the [Figure 12](<Calculationofthesmartinverterfun.md#\_bookmark67>). The discontinuity in *p*2 is not a problem due to the reactive power is zero for either power factor equal 1 or -1.

To define this watt-pf curve, the user needs to calculate the *p*2, and include the coordinates (*p*2, 1) and (*p*2, -1) into the OpenDSS XYcurve object.

&nbsp;

![A diagram of a graph

Description automatically generated](<lib/NewItem471.png>)

**Figure 11: watt-pf curve**

![A diagram of a diagram

Description automatically generated](<lib/NewItem470.png>)

**Figure 12: watt-pf curve with reference in zero**

&nbsp;

**Smart inverter watt-var function** For the smart inverter watt-var function, the output active power in *pu* is applied, *pdesired*\[*t*\], in the watt-var curve defined in the *wattvar\_curve* property to obtain the desired reactive power value in *pu*, *qDfun*\[*t*\]*j*, according to [Equation 61](<OpenDSSDocumentation.md#\_bookmark68>). The [Figure 13](<Checkingauxiliaryoptions.md#\_bookmark69>) shows an example of a user-defined watt-var curve.

&nbsp;

![Image](<lib/NewItem545.png>)

***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with HelpNDoc's Clean and Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
