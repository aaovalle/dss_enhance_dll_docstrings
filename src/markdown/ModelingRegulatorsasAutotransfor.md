# Modeling Regulators as Autotransformers

&nbsp;

&nbsp;

Single‐phase voltage regulators are actually autotransformers. Since the beginning of DSS in 1997, we have traditionally modeled regulators as conventional, but low‐impedance, two‐winding transformers and controlled one of the windings with a RegControl device. The is the same approach we use for substation LTC models. This is easier than constructing an autotransformer by connecting the windings in a special way and, for the most part, it gives the same answer for distribution system analysis purposes.

&nbsp;

There have been a few cases where it would have been advantageous to model line regulators as autotransformers. While we found workarounds for those cases, we have taken another look at modeling the regulators as autotransformers. This document describes one approach.

&nbsp;

The problem is not that OpenDSS cannot model autotransformers. While there is no builtin autotransformer model (yet), you can construct an autotransformer by connecting the windings of 1‐ phase transformers appropriately. The problem, until recently, was that the RegControl element was not capable of properly controlling the tap position correctly. As of version 7.6.3 build 20, (version 7.6.3.20) this has been remedied and this document illustrates how to use the model.

&nbsp;

The script in Figure 1 has been uploaded to the website under the Test folder. The script file name is TestAuto.DSS.

&nbsp;

Figure 2 shows a schematic diagram of this simple test circuit. It consists of a 12.47 kV 3‐phase source connected to the default SourceBus. Then there is a short line (default OpenDSS Line model) between SourceBus and the bus at the high‐side of the regulator, Hbus.

&nbsp;

One restriction in OpenDSS is that all conductors at a circuit element terminal must be connected to the same bus. They can be connected to different nodes at the bus, but they must be connected to the same bus. The autotransformer connection requires that winding 1 and winding 2 of the transformer share a node in common – where the series winding is connected to the common winding. So we have at least a couple of choices for making the autotransformer connection:

&nbsp;

&#49;. Connect both windings to the same bus with the node connections defined to make up the proper autotransformer connection between the series and common winding.

&nbsp;

&#50;. Connect the windings to different buses and use a short jumper (a Reactor element) to create the tie between the series and common windings.

&nbsp;

Either option will work. For this example, we use the first option and connect both windings of the Transformer element to Xbus. To make things a little cleaner, a jumper is used to connect node 1 of Hbus to node 1 of Xbus. Thus it effectively appears that the regulator is between Hbus and Xbus. The

jumper is a Reactor element with an impedance of 0 +j0.0001 ohms.

&nbsp;

The transformer Auto1 has two windings: 1) the main (common) winding rated 7.2 kV and 2) the series winding rated 1/10 of that, or 0.72 kV. This give a nominal regulation range of +/‐ 10% as is common for standard step voltage regulators. By default, the transformer is assumed to have 32 taps from Mintap to Maxtap. For a standard two‐winding transformer, Mintap defaults to 0.90 and Maxtap defaults to 1.10 to achieve the desired range from 10% buck to 10% boost. With the autotransformer model, we intend to use the entire Winding 2 as our tap winding. The tap range is defined from Mintap=-1.0 to Maxtap=1.0. Assuming the base (common) winding is rated at 1.0-pu voltage, this combination gives the same regulation range as the two‐winding LTC‐type transformer model we have been using traditionally.

&nbsp;

| Clear&nbsp; // Script to Test RegControl on a transformer configured as an autotransformer&nbsp; New Circuit.TestAuto ~ BasekV=12.47&nbsp; New Line.Line1 Bus1=SourceBus.1.2.3 Bus2=Hbus.1.2.3&nbsp; New REACTOR.Jumper phases=1 Bus1=Hbus.1 Bus2=Xbus.2 R=0 X=0.0001&nbsp; New Transformer.Auto1 X12=1 Phases=1 Windings=2 ~ wdg=1 Bus=Xbus.1.0 kV=7.2 kVA=50 ~ wdg=2 Bus=Xbus.1.2 kV=0.72 kVA=50 Maxtap=1.0 Mintap=-1.0 ~ %loadloss=.1&nbsp; New Load.Load1 Phases=1 Bus1=Xbus.1.0 kW=100 PF=.9 kV=7.2&nbsp; Set voltagebases=\[12.47\] calcvoltagebases&nbsp; New REGCONTROL.Reg1 transformer=Auto1 winding=2 bus=Xbus.1 ptratio=60 vreg=125 ~ maxtapchange=1&nbsp; Set maxcontroliter=30&nbsp; solve&nbsp; Show Currents Elements Show Voltage LN Nodes&nbsp; Show Eventlog show taps |
| --- |


Figure 1. Script for Autotransformer Test Case (TestAuto.DSS)

&nbsp;

The impedance of Transformer.Auto1 is defined as 1% on a 50 kVA base. This brings up one difference between this modeling approach and the two‐winding LTC‐type transformer approach. The auto transformer components are designed to transformer 50 kVA, which allows the autotransformer to

regulate about 500 kVA of load at 10% raise or lower. For a two‐winding model, we would have defined the impedance as approximately 0.1% and the transformer kVA = 500 to make an equivalent model.

&nbsp;

Note the polarity of the two windings (see the script and the diagram). This will be important for understanding the example where we actually get a voltage rise across the first winding.

&nbsp;

One change that had to be made to the Transformer and RegControl element models is to allow for the null tap position where the winding 2 tap = 0. Negative tap positions were never a problem with the OpenDSS transformer model, but zero was. When the Regcontrol proposes a zero tap value, the

Transformer automatically replaces that with a small non‐zero value.

&nbsp;

Also, note that the RegControl device is only permitted to make one tap change per control iteration. This is not necessary, but was done in the example so we could verify that the model was working correctly.

&nbsp;

![Image](<lib/NewItem177.png>)\
Figure 2. Autotransformer Test Circuit Schematic

&nbsp;

The final “trick” to making this work is to have the RegControl monitor a bus voltage instead of the transformer’s winding 2 voltage. In the normal OpenDSS model, the RegControl monitors the winding voltage. This is sufficient for the two‐winding LTC‐type transformer equivalent of the regulator, but the series winding voltage of the autotransformer will not necessarily correspond to the voltage we want the regulator to control. Fortunately, the RegControl has the option to monitor a selected bus voltage using the Bus property. This feature is more common used to model voltage regulation schemes that get voltage signals from remote locations. In this case we are having the RegControl monitor node Xbus.1, which is local to the regulator.

&nbsp;

The RegControl controls winding 2 of the autotransformer (the series winding). Its algorithm adjusts the tap (one step at a time in this case) until the voltage being monitored falls within the band specified by the Vreg and Band properties.

&nbsp;

*Note: It is possible in this case that we could have told the RegControl that it was connected to Winding 1 and set the TapWinding property to winding 2. Thus, it would attempt to achieve the target voltage across winding 1 by adjusting taps on winding 2. However, this was not tested.*

&nbsp;

**SOLUTION**

&nbsp;

The solution summary from the test script is shown in Figure 3. It indicates there were 9 adjustments of the taps. The power flow is very easy to solve, so it only took two iterations per tap step.

&nbsp;

| Control Mode =STATIC Total Iterations = 18 Control Iterations = 9 Max Sol Iter = 2 |
| --- |


Figure 3. Solution Summary

&nbsp;

You can see what is happening during the solution process by executing the Show Eventlog command. This is shown in Figure 4. That initial tap for the autotransformer winding 2 is 1.0, creating a 10% rise (see polarity of the series winding). So it must move the tap down to lower the voltage to the desired 125 V on a 120 V base (PTratio = 60). Each tap change is 0.0625 pu (5/8%), which is typical. When the process gets to tap position 0.5 (0.72 \* 0.5 = 0.36 kV), the control objective is met. That is, the series winding adds about 360 V to the incoming 7196 V to get 7574.5 V. The resulting L‐N voltage solution is shown in Figure 5.

&nbsp;

The resulting voltage is 1.0521 pu = 126.25 V, which is within half the bandwith of 3 V specified for the regulation target. Note that if we had started off from a lower tap position and had to raise the tap to achieve the objective, the solution would have been different. With a 3 V bandwidth, it is common for there to be 3 valid solutions for a tapchanging regulator depending on the initial tap position. The present OpenDSS RegControl device stops changing the tap when the voltage enters the band. Other algorithms might try to get closer to the center of the band.

&nbsp;

| Hour=0, Sec=0, ControlIter=1, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.9375. Hour=0, Sec=0, ControlIter=2, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.875. Hour=0, Sec=0, ControlIter=3, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.8125. Hour=0, Sec=0, ControlIter=4, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.75. Hour=0, Sec=0, ControlIter=5, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.6875. Hour=0, Sec=0, ControlIter=6, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.625. Hour=0, Sec=0, ControlIter=7, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.5625. Hour=0, Sec=0, ControlIter=8, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.5. |
| --- |


Figure 4. Event Log for Solution

&nbsp;

| NODE-GROUND VOLTAGES BY BUS \& NODE Bus Node V (kV) Angle p.u. Base kV SOURCEBUS 1 7.1988 /\_ 0.0 0.9999 12.470 - 2 7.1995 /\_ -120.0 0.99999 12.470 - 3 7.1996 /\_ 120.0 1 12.470 HBUS .... 1 7.196 /\_ 0.0 0.9995 12.470 - 2 7.201 /\_ -120.0 1.0002 12.470 - 3 7.1993 /\_ 120.0 0.99996 12.470 XBUS .... 1 7.5745 /\_ 0.0 1.0521 12.470 - 2 7.196 /\_ 0.0 0.9995 12.470 |
| --- |


Figure 5. Voltage solution

&nbsp;

CVR CASE

&nbsp;

Now, let’s do something interesting with the model. Let’s assume we want to go from regulating the voltage high at 125 V to adopting a conservation voltage reduction (CVR) approach and regulating to 118 V.

&nbsp;

Figure 6 shows the script, event log, and tap report for moving from the present solution at 125 V to 118 V. First the Vreg property of RegControl.Reg1 is changed to 118 by the script command

&nbsp;

regcontrol.reg1.vreg=118

&nbsp;

Any property in OpenDSS can be changed using this syntax. This invokes the property editor for the named device and changes the value of the specified property. You can change multiple properties once the property editor is invoked for the specified circuit element, for example:

&nbsp;

regcontrol.reg1.vreg=118 delay=25

&nbsp;

After changing the Vreg property to 118, another power flow solution is made (solve). The resulting tap changes can be seen in the event log as shown in Figure 6.

&nbsp;

| regcontrol.reg1.vreg=118 solve show eventlog&nbsp; Hour=0, Sec=0, ControlIter=1, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.9375. Hour=0, Sec=0, ControlIter=2, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.875. Hour=0, Sec=0, ControlIter=3, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.8125. Hour=0, Sec=0, ControlIter=4, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.75. Hour=0, Sec=0, ControlIter=5, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.6875. Hour=0, Sec=0, ControlIter=6, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.625. Hour=0, Sec=0, ControlIter=7, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.5625. Hour=0, Sec=0, ControlIter=8, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.5. Hour=0, Sec=0, ControlIter=1, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.4375. Hour=0, Sec=0, ControlIter=2, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.375. Hour=0, Sec=0, ControlIter=3, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.3125. Hour=0, Sec=0, ControlIter=4, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.25. Hour=0, Sec=0, ControlIter=5, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.1875. Hour=0, Sec=0, ControlIter=6, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.125. Hour=0, Sec=0, ControlIter=7, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0.0625. Hour=0, Sec=0, ControlIter=8, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO 0. Hour=0, Sec=0, ControlIter=9, Element=Regulator.auto1, Action= CHANGED -1 TAPS TO -0.0625.&nbsp; CONTROLLED TRANSFORMER TAP SETTINGS&nbsp; Name Tap Min Max Step Position |
| --- |


Figure 6. Script and Event Log for Move from 125 V to CVR Mode, 118 V

&nbsp;

Since the regulator needs to lower the voltage to the new set point, it taps down through tap 0 until it ends up one tap below neutral, or the null tap. This yields the voltages shown in Figure 7.

&nbsp;

The voltage at the regulated bus (Xbus.1) is 0.9933 pu = 119.2 V. This is 1.2 V above the desired set point of 118 V, but is less than 1.5 V (half the3 V bandwidth). So it is an acceptable solution.

&nbsp;

| NODE-GROUND VOLTAGES BY BUS \& NODE&nbsp; Bus &nbsp; &nbsp; &nbsp; Node&nbsp; V (kV) &nbsp; Angle &nbsp; &nbsp; &nbsp; p.u. &nbsp; Base kV&nbsp; SOURCEBUS 1 &nbsp; &nbsp; 7.1988&nbsp; /\_ 0.0 &nbsp; &nbsp; 0.9999&nbsp; &nbsp; 12.470&nbsp; &nbsp; -&nbsp; &nbsp; &nbsp; 2 &nbsp; &nbsp; 7.1995&nbsp; /\_ -120.0 0.99999&nbsp; &nbsp; 12.470&nbsp; &nbsp; -&nbsp; &nbsp; &nbsp; 3 &nbsp; &nbsp; 7.1996&nbsp; /\_ 120.0&nbsp; &nbsp; &nbsp; &nbsp; 1&nbsp; &nbsp; 12.470 HBUS .... 1 &nbsp; &nbsp; 7.196 &nbsp; /\_ 0.0&nbsp; &nbsp; 0.99951&nbsp; &nbsp; 12.470&nbsp; &nbsp; -&nbsp; &nbsp; &nbsp; 2 &nbsp; &nbsp; 7.201 &nbsp; /\_ -120.0&nbsp; 1.0002&nbsp; &nbsp; 12.470&nbsp; &nbsp; -&nbsp; &nbsp; &nbsp; 3 &nbsp; &nbsp; 7.1993&nbsp; /\_ 120.0&nbsp; 0.99996&nbsp; &nbsp; 12.470 XBUS .... 1 &nbsp; &nbsp; 7.1513&nbsp; /\_ 0.0 &nbsp; &nbsp; 0.9933&nbsp; &nbsp; 12.470&nbsp; &nbsp; -&nbsp; &nbsp; &nbsp; 2 &nbsp; &nbsp; 7.196 &nbsp; /\_ 0.0&nbsp; &nbsp; 0.99951&nbsp; &nbsp; 12.470 |
| --- |


Figure 7. Voltage Solution for CVR Mode

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
