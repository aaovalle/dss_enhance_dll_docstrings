# Precedence of Watt Related Functions/Settings

This example illustrates the precedence of watt related functions and the violation of the element’s *kWRated* limit. The following script has been utilized.

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp;

...

\!kW Rated Violation Only

New LoadShape.dispatchFollow interval=1 npts=24 mult=\[0,0.01,0.08,0.12,0.16,0.30,0.85,0.96,1.05,1.05,0,0,0,0,0.01,0.08,0.12,0.16,0.30,0.85,0.96,1.05,0,0\]

&nbsp;

Edit Storage.A dispmode=follow daily=dispatchFollow kvar=200

&nbsp;

\!VWCurves

\!VWCurve for Discharging

New XYCurve.vwcurvedch npts=4 yarray=\[1 1 0.0 0.0\] xarray=\[1 1.05 1.1 1.3\]

\!VWCurveforCharging

New XYCurve.vwcurvech npts=4 yarray=\[0.0 0.0 1 1\] xarray=\[0.7 0.9 0.95 1\]

&nbsp;

New InvControl.InvCtrl mode=VOLTWATT voltWattcurve=vwcurvedch

\~ voltWattCHcurve=vwcurvech

&nbsp;

\!PPriority

Set casename=Ppriority

Edit Storage.Awattpriority=true

&nbsp;

\!QPriority

\!Setcasename=Qpriority

\!EditStorage.Awattpriority=false

&nbsp;

\!PFPriority

\!Setcasename=PFpriority

\!EditStorage.APFpriority=true

&nbsp;

Set mode=Daily

Set maxcontroliter=50 Setstepsize=1h

&nbsp;

\!15am

Edit VSource.sourcepu=1.02

Set number=5

Solve

&nbsp;

\!6am

Edit VSource.sourcepu=0.94

Set number=1

Solve

&nbsp;

\!7am

Edit VSource.sourcepu=0.95

Solve

&nbsp;

\!8am

Edit VSource.sourcepu=0.982

Edit Storage2.A %kWRated=88

Solve

&nbsp;

\!9am

Edit VSource.source pu=1.0

Edit Storage2.A %kWRated=100&nbsp;

Solve

&nbsp;

\!10am7pm

Edit VSource.source pu=1.02

Set number=10

Solve

&nbsp;

\!8pm

Edit VSource.source pu=1.025

Set number=1

Solve

&nbsp;

\!9pm

Edit VSource.source pu=0.98

Edit Storage2.A %kWRated=88

Solve

&nbsp;

\!10pm

Edit VSource.source pu=0.97

Edit Storage.A %kWRated=100

Solve

&nbsp;

\!11pm12am

Edit VSource.source pu=1.02

Set number=2

Solve

&nbsp;

Export monitors MonStorageAState

Export monitors MonStorageAV

Export eventlog

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp;

&nbsp;

Similarly to the previous example, the storage element is operated with active power dispatch driven by “Follow” mode, however the reactive power dispatch is set to constant kvar mode, with 200 kvar of reactive power generation. Futhermore, the actual active power dispatch may be limited by the smart inverter VW functionality, which is specified in “InvCtrl” InvControl control element. Note that two different Volt-Watt curves (XYCurve object) have been specified. One for operation in discharging state and the other for operation in charging state, as shown in [Figure 7](<OpenDSSDocumentation.md#\_bookmark15>).

The daily simulation is broken in several time intervals with varying sizes (specified through property *number*). The voltage magnitude of the voltage source (*pu* property) is also varied in the simulation. This has been done to force the operation of the VW function in selected time instants to highlight the precedence of functions.

Note that there are 3 different inverter functions from [Table 1](<PrecedenceofFunctionsSettings1.md#\_bookmark8>) being applied in this example:

* Volt-Watt Function (3rd priority): enabled by the InvControl control element;
* Limit DER Power Function (3rd priority): enabled by setting %*kWRated* to a value less than 100, which is done at 8am and 9pm only;

&nbsp;

![A diagram of a number of points

Description automatically generated with medium confidence](<lib/NewItem562.png>)

**Figure 7: Volt-Watt Curve for Discharging (a) and Charging (b)**

&nbsp;

* Storage “Follow” Dispatch Mode (5th priority): enabled when setting *dispmode* = *follow*;

[Figure 8](<OpenDSSDocumentation.md#\_bookmark16>) shows the PQ plane with all operating points for each of the priorities. Note that all operating points lie on the constant power factor line (except for those that fall in the Watts only region) and that there are no differences in the inverter response between all three priorities for the *kWRated* violation, as expected, according to [Figure 4b](<OpenDSSDocumentation.md#\_bookmark5>).

![A diagram of a function

Description automatically generated](<lib/NewItem561.png>)

**Figure 8: PQ Plane with Inverter Capability Curve and Operating Points under Constant kvar Mode (Example [11.2**](<References7.md#\_bookmark14>)**)**

&nbsp;

A few rows and columns of the .csv file exported from monitor *Mon StorageA State* are shown in [Table 4](<PrecedenceofWattRelatedFunction1.md#\_bookmark17>). For a complete description of each column, see \[[3](<References7.md#\_bookmark22>)\].

At 6am, the kW desired by the “follow” dispatch mode to charge the element is 270kW, and the average voltage (see InvControl’s *monV oltageCalc* property) applied at the element’s terminal is 0.9357, which lies within the region where the VW curve for charging tries to limit the active power. The limit imposed can be calculated as (0#8202;*.*&#8202;9357 *−* 0#8202;*.*&#8202;9) *×*&nbsp; 1&nbsp; *×* 900 = 642#8202;*.*&#8202;6*kW* , which is greater than the desired output. Thus, the power that charges the element at the grid interface, *kWIn*, is 270*kW* .

At 7am, the desired power is 765kW. However, the voltage reference to the VW is 0.9299, which leads to a limit imposed by this function of (0#8202;*.*&#8202;92994 *−* 0#8202;*.*&#8202;9) *×*&nbsp; 1&nbsp; *×* 900 = 538#8202;*.*&#8202;9*kW* . Since %*kWRated* at this time instant is 100%, the limit imposed by the Limit DER Power Function is 900kW. Thus, as the limit imposed by the VW function requires the greatest reduction and it has a greater priority than the power desired by the “follow” dispatch function, it takes precedence and the actual power with which the element is charged is 538.9kW.

At 8am, %*kWRated* has been set to limit the output in 88 percent of the rated active power, which is 792kW. Note that the voltage reference for the VW function is 0.9477, which means the limit of (0#8202;*.*&#8202;9477 *−* 0#8202;*.*&#8202;9) *× 1/0.05* *×* 900 = 858#8202;*.*&#8202;6*kW* . However, the controller has access to the limit imposed by the Limit DER Power Function, and thus, the power reported in “kW VW Limit” is the lowest between the power calculated from the VW curve and the one imposed by the direct command. As the desired power at this time instant is higher than the limit imposed by %*kWRated*, the actual power output that charges the element at the grid interface is 792*kW* .

At 9am, the power desired is 1#8202;*.*&#8202;05 *×* 900 = 945*kW* . As none of the limiting functions impose a lower limit, the actual power at the grid interface is limited by the nameplate device setting, *kWRated* (2nd priority).

Finally, at 10am, there is not enough energy capacity left to keep charging the element, which corresponds to a Fundamental Physical Limit (1st priority). Therefore, the element enters in idling state, charging only enough power to sustain its idling and associated inverter losses. Note that because there is no energy capacity left, *kWDesired* shows 0, even though the loadshape multiplier at 10am is -1.05.

Table 4: Selected Rows and Columns of *csv* File Exported from Monitor *Mon StorageA State*

&nbsp;

|  **Hour** |  **State** |  **kWOut** |  **kWIn** |  **kvarOut** | **Inv ON** |  **Vref** | **VW** **Oper** | **kW Desired** | **kW VW** **Limit** | **Limit** **kWOut Function** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| &#49; | &#48; | &#48; | &#50;1.8 | &#50;00 | &#48; | &#49;.0290 | &#48; | &#48; | &#57;999 | &#57;00 |
| &#50; | &#48; | &#48; | &#50;1.8 | &#50;00 | &#48; | &#49;.0290 | &#48; | \-9 | &#57;999 | &#57;00 |
| &#51; | \-1 | &#48; | &#55;2 | &#48; | &#49; | &#49;.0163 | &#48; | \-72 | &#57;00 | &#57;00 |
| &#52; | \-1 | &#48; | &#49;08 | &#50;00 | &#49; | &#49;.0246 | &#48; | \-108 | &#57;00 | &#57;00 |
| &#53; | \-1 | &#48; | &#49;44 | &#50;00 | &#49; | &#49;.0227 | &#48; | \-144 | &#57;00 | &#57;00 |
| &#54; | \-1 | &#48; | &#50;70 | &#50;00 | &#49; | &#48;.9357 | &#48; | \-270 | &#54;42.6 | &#57;00 |
| &#55; | \-1 | &#48; | &#53;38.9 | &#50;00 | &#49; | &#48;.9299 | &#49; | \-765 | &#53;38.9 | &#57;00 |
| &#56; | \-1 | &#48; | &#55;92 | &#50;00 | &#49; | &#48;.9477 | &#48; | \-864 | &#55;92 | &#55;92 |
| &#57; | \-1 | &#48; | &#57;00 | &#50;00 | &#49; | &#48;.9599 | &#48; | \-945 | &#57;00 | &#57;00 |
| &#49;0 | &#48; | &#48; | &#50;2.0 | &#50;00 | &#48; | &#49;.0290 | &#48; | &#48; | &#57;999 | &#57;00 |
| &#49;1 | &#48; | &#48; | &#50;1.8 | &#50;00 | &#48; | &#49;.0290 | &#48; | &#48; | &#57;999 | &#57;00 |
| &#49;2 | &#48; | &#48; | &#50;1.8 | &#50;00 | &#48; | &#49;.0290 | &#48; | &#48; | &#57;999 | &#57;00 |



***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Simplicity of HelpNDoc's User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
