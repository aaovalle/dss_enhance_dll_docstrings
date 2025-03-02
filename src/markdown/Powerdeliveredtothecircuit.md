# Power delivered to the circuit

&nbsp;

The steps taken to obtain the power delivered to the circuit in the time step, *t*, are presented in this section. This process can be repeated multiple times for the same time step, *t*, within the control loop if there is an InvControl element controlling this PVSystem.

&nbsp;

**Step 1: Calculation of PV array’s output power** The irradiance at a time step, *t*, is converted into PV array’s DC output power, *Pdc*\[*t*\], according to [Equation 1](<OpenDSSDocumentation.md#\_bookmark5>).

&nbsp;

![Image](<lib/NewItem482.png>)

&nbsp;

Where:

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *irradiance*: Base value of irradiance in *kW/m*2. For static simulations, this value represents the present irradiance on PV array and therefore there is no need to define *irradiance*\[*t*\];
         * *irradiance*\[*t*\]: Value of the yearly, daily or duty irradiance curve in the time step, *t*;
         * *PTCurve*(*Temperature*\[*t*\]): Value of the correction factor in the time step *t* due to the tem- perature *Temperature*\[*t*\];
         * *Temperature*\[*t*\]: Value of the temperature curve in time step *t*. For static simulations, however, the user must set the present temperature *Temperature* instead of this property.

Besides the inverter efficiency curve, another simplification of the model considers that the ratio of PV array’s output power, *Pdc*, to irradiance is linear, as can be seen in the Simplified curve (red curve) of [Figure 6](<Powerdeliveredtothecircuit.md#\_bookmark8>), however, the relationship between them, Real curve, is not constant for the entire range of irradiance values. It should be noted that the Real curve (blue curve) of [Figure 6](<Powerdeliveredtothecircuit.md#\_bookmark8>) does not correspond to a measured curve, it is just illustrative.

&nbsp;

**Step 2: Checking the PV inverter status** The inverter status at time step *t* depends on its status in the previous time step, *t −* 1, as shown below.

When the inverter status is OFF in *t -* 1, it means that *Pac*\[*t -* 1\] = 0. It is turned ON in *t* according to [Equation 2](<Powerdeliveredtothecircuit.md#\_bookmark6>).

&nbsp;

&nbsp;

![Image](<lib/NewItem483.png>)

&nbsp;

When the inverter status is ON in *t -* 1, it means that *Pac*\[*t -* 1\] *\>* 0. It is turned OFF in *t* according to [Equation 3](<Powerdeliveredtothecircuit.md#\_bookmark7>).

&nbsp;

![Image](<lib/NewItem484.png>)

&nbsp;

![A graph of a function

Description automatically generated](<lib/NewItem476.png>)

**Figure 6: PV array output power vs Irradiance**

&nbsp;

One model constraint is the need to have *%cutout* less than or equal to *%cutin*.

&nbsp;

**Step 3: Calculation of the inverter desired active output power** The inverter desired active output power is calculated by [Equation 4](<Powerdeliveredtothecircuit.md#\_bookmark9>). In this step, the maximum active power limit is also verified by means of the *%Pmpp* property of the PVSystem and the active power limit, *PLimit*\[*t*\], resulting from an eventual operation of the volt-watt function of an InvControl element that might be controlling the PVSystem.

&nbsp;

![Image](<lib/NewItem485.png>)

&nbsp;

&nbsp;

Where:

&nbsp;

![Image](<lib/NewItem486.png>)

&nbsp;

**Step 4: Specification of inverter desired reactive power** The inverter desired reactive power, Qtac, is defined separately from the active power and can be specified as either a fixed kvar value,

using the *kvar* property, or as a function of a constant power factor using *PF* property. In the first case, the inverter must try to keep the value of the reactive power constant and equal to *kvar*, regardless of the present value of the output active power. In the second case, which corresponds to the smart inverter function named as constant power factor, the inverter changes the reactive power to maintain the nominal power factor. Another way of setting the desired value of the reactive power, Qtac, is done by the operation of a few functions of the InvControl element, as shown in the section 2.

&nbsp;

**Step 5: Checking the inverter reactive power limits** The desired reactive power after the verification of its limits is presented in equations [6](<OpenDSSDocumentation.md#\_bookmark10>) and [7](<OpenDSSDocumentation.md#\_bookmark11>).&nbsp; [Equation 6](<OpenDSSDocumentation.md#\_bookmark10>) is used when the desired reactive power, *Qt* \[*t*\], is positive and, [Equation 7](<OpenDSSDocumentation.md#\_bookmark11>), when it is negative.

&nbsp;

&nbsp;

![Image](<lib/NewItem487.png>)

&nbsp;

![Image](<lib/NewItem488.png>)

[Equation 8](<OpenDSSDocumentation.md#\_bookmark12>) and [Equation 9](<OpenDSSDocumentation.md#\_bookmark13>) present the limits of the provided and absorbed reactive power, respectively, as a function of the active power delivered to the grid.

&nbsp;

![Image](<lib/NewItem489.png>)

&nbsp;

&nbsp;

![Image](<lib/NewItem490.png>)

&nbsp;

Where:

&nbsp;

* ![Image](<lib/NewItem491.png>)

&nbsp;

&nbsp;

* ![Image](<lib/NewItem492.png>)

&nbsp;

If the inverter status is OFF, *Qttac*\[*t*\] can only be non-zero when the *VarFollowInverter* property is set to NO or False.

&nbsp;

**Step 6: Checking inverter capability** The maximum inverter capacity corresponds to its kVA rating. Active and reactive power that are delivered to the grid can be defined according to Equations [10](<OpenDSSDocumentation.md#\_bookmark14>) and [11](<OpenDSSDocumentation.md#\_bookmark15>) when the inverter capacity is not exceeded.

&nbsp;

![Image](<lib/NewItem493.png>)

&nbsp;

![Image](<lib/NewItem494.png>)

&nbsp;

If its capacity is exceeded, the PV inverter limits the value of&nbsp; its kVA rating, *kV A* property. As a result, *P’ac\[t\]* and/or *Q”ac\[t\]* should be reduced to meet one of the following 3 priorities:

&nbsp;

* **Power factor priority** Equations [12](<OpenDSSDocumentation.md#\_bookmark16>) and [13](<OpenDSSDocumentation.md#\_bookmark17>) present the values of the active and reactive power that are delivered to the grid when the inverter capacity is exceeded under power factor priority.

&nbsp;

![Image](<lib/NewItem495.png>)

&nbsp;

![Image](<lib/NewItem496.png>)

&nbsp;

* **Active power priority [**Equation 14](<OpenDSSDocumentation.md#\_bookmark18>) presents the new reduced value of the reactive power that is delivered to the circuit when the inverter capacity is exceeded under active power priority. If the active power is greater than or equal to the capacity of the inverter, the new value of the active power that is delivered to the grid becomes the kVA rating and therefore, there is no room for reactive power, according to [Equation 15](<OpenDSSDocumentation.md#\_bookmark19>).

&nbsp;

&nbsp;

![Image](<lib/NewItem497.png>)

&nbsp;

![Image](<lib/NewItem498.png>)

&nbsp;

* **Reactive power priority [**Equation 16](<OpenDSSDocumentation.md#\_bookmark20>) presents the new reduced value of the active power that is delivered to the circuit when the inverter capacity is exceeded under reactive power priority. If the reactive power is greater than or equal to the capacity of the inverter, the new value of the reactive power becomes the capacity of the inverter itself, according to [Equation 17](<OpenDSSDocumentation.md#\_bookmark21>), but this can only happen if the inverter is capable of providing or absorbing reactive power without any active power, in other words, when the *VarFollowInverter* property is set to either NO or False.

&nbsp;

![Image](<lib/NewItem499.png>)

&nbsp;

![Image](<lib/NewItem500.png>)

&nbsp;

Finally, the apparent power provided by the PVSystem in a time step *t* can be written according to [Equation 18](<OpenDSSDocumentation.md#\_bookmark22>).

&nbsp;

![Image](<lib/NewItem501.png>)

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
