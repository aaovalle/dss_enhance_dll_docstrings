# Norton equivalent

&nbsp;

This section presents the Norton equivalent definition for a three-phase PVSystem connected to the grid through the bus named as Connection Bus, as presented in [Figure 7](<Powerdeliveredtothecircuit.md#\_bookmark23>).

&nbsp;

![A diagram of a diagram

Description automatically generated](<lib/NewItem475.png>)

**Figure 7:&nbsp; &nbsp; A three-phase PVSystem modeled as a Norton Equivalent**

By observing [Figure 7](<Powerdeliveredtothecircuit.md#\_bookmark23>), the following electric quantities can be defined:

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * Nodal voltages:

**˙**&nbsp; &nbsp; ˙

&nbsp;

![Image](<lib/NewItem502.png>)

&nbsp;

&nbsp;

&nbsp;

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * Terminal currents:

&nbsp;

&nbsp;

![Image](<lib/NewItem503.png>)

&nbsp;

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * Norton or compensation currents:

&nbsp;

![Image](<lib/NewItem504.png>)

&nbsp;

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * Linear currents:

&nbsp;

![Image](<lib/NewItem505.png>)

&nbsp;

&nbsp;

The normal power flow solution technique in OpenDSS is based on the [Equation 23](<Nortonequivalent.md#\_bookmark24>).

&nbsp;

![Image](<lib/NewItem506.png>)

&nbsp;

Where:

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * **I˙**: Injected current array;
         * **V˙** : System voltage array.

OpenDSS computes the compensation currents from each PC element to populate the injected current array. Therefore, the main purpose of this section is to understand how OpenDSS calculates the compensation currents for PVSystem. It means: *I*˙*comp*1 , *I*˙*comp*2 and *I*˙*comp*3

&nbsp;

It is possible by means of Kirchhoff’s first law to express the compensation currents in function of the linear and terminal currents, as presented in [Equation 24](<OpenDSSDocumentation.md#\_bookmark25>).

&nbsp;

![Image](<lib/NewItem507.png>)

The linear currents can be written as a function of the nodal voltages, [Equation 25](<OpenDSSDocumentation.md#\_bookmark26>), and the terminal currents as a function of both the three-phase apparent power provided by the PVSystem , *S*¯3*φ*, and the nodal voltages, [Equation 26](<OpenDSSDocumentation.md#\_bookmark27>). (It is assumed that PVSystem operates with constant power).

&nbsp;

![Image](<lib/NewItem508.png>)

&nbsp;

![Image](<lib/NewItem509.png>)

&nbsp;

The Norton or linear admittance, *Y*¯*linear* , is calculated using the apparent power provided by the element, according to [Equation 27](<Nortonequivalent.md#\_bookmark28>).

&nbsp;

![Image](<lib/NewItem510.png>)

&nbsp;

Where:

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *Vn* corresponds the rated voltage of the PVSystem.

The final expression for the calculation of the compensation currents, therefore, is presented in [Equation 28](<OpenDSSDocumentation.md#\_bookmark29>).

&nbsp;

![Image](<lib/NewItem511.png>)

The compensation currents are calculated as shown above if two conditions are satisfied. First, the *model* property of the PVSystem is set equal to 1, the default OpenDSS value for constant power operation. And second, each nodal voltage has to be in the range defined by the *Vminpu* and *Vmaxpu* properties, which by default are 0#8202;*.*&#8202;9 and 1#8202;*.*&#8202;1, respectively. Outside this range, the corresponding phase of the element is modeled as constant impedance.


***
_Created with the Standard Edition of HelpNDoc: [Full-featured EPub generator](<https://www.helpndoc.com/create-epub-ebooks>)_
