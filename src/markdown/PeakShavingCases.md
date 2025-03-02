# PeakShaving Cases

In this example, the storage controller is set to operate in peakshave mode for discharging and time mode for charging. The peakshaving target is 10MW with the default band of +/-1%. The charging is set to start at 2am, with a rate of 50%. The power monitored by the controller in peakshave mode is at the first terminal of the same line where a monitor has been placed in the base script and the fleet reserve has been set to 20%.

&nbsp;

Edit Storage.F kWrated=100&nbsp;

Edit Storage.G kWrated=125

&nbsp;

/\*

s e t&nbsp; casename=NoEnergy

Edit Storage .A kWhrated=250 % stored=70&nbsp;

Edit Storage . B kWhrated=500 % stored=70&nbsp;

Edit Storage . C kWhrated=825 % stored=70

Edit Storage .D kWhrated=625 % stored=70&nbsp;

Edit Storage . E kWhrated=250 % stored=70&nbsp;

Edit Storage . F kWhrated=600 % stored=70&nbsp;

Edit&nbsp; Storage .G kWhrated=625&nbsp; % stored=70

\*/

&nbsp;

\! S o l uti o n&nbsp; S e t t i n g s

Set maxcontroliter=50&nbsp;

Set mode=Daily

Setstepsize=1h

Set number=24

&nbsp;

Solve

&nbsp;

Export monitors m1pq

Export Eventlog

Export monitors storage.Astates

Export monitors storage.Bstates

Export monitors storage.Cstates&nbsp;

Export monitors storage.Dstates&nbsp;

Export monitors storage.Estates

Export monitors storage.Fstates

Export monitors storage.Gstates

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp;

&nbsp;

Three different cases are run. In the first one, named “Complete”, no changes are applied to the fleet ratings, which is enough to completely shave the peak, as shown in [Figure 9](<OpenDSSDocumentation.md#\_bookmark17>). In the second one, “NoPower”, the rated power of each element of the fleet is reduced in 50%. In this case, it can be seen that the fleet is not able to totally shave the peak from 6pm to 8pm. In the last case, the total energy capacity of the fleet has been reduced to 50% of its original value. Because of that, the fleet reaches its reserve energy at 9pm, and cannot continue to shave the peak after that.

Note that the total necessary time to charge the fleet at the beginning of the day is different for each case due to different power and energy rated capacities. Also note the little increase in the power measured when the fleet is idling, due to the existence of idling losses.

[Figure 10](<OpenDSSDocumentation.md#\_bookmark18>) shows the power dispatched by each element of the fleet for the complete shaving case. At the beginning of the day, indeed, each element charges with 50% of their respective rated power. In time mode, as explained in section [5.3.2](<References2.md#\_bookmark9>), the fleet remain in the state set by the controller until there is no longer enough capacity left in the fleet, which can occur at different time instants for each element depending on each element’s ratings. For instance, element *E* takes only three hours to be fully charged, while element *F* takes 5 hours. This can also be seen in [Figure 11](<OpenDSSDocumentation.md#\_bookmark19>).

[Table 2](<PeakShavingCases.md#\_bookmark20>) shows the event log with all control actions executed by the controller. Note that the controller sets the fleet to discharge the first time at 6pm, when the regulated power is greater

&nbsp;

![A graph of a number of different colored lines

Description automatically generated with medium confidence](<lib/NewItem399.png>)

**Figure 9: Powers at the monitored line element for each PeakShaving case**

![A graph with colorful lines and numbers

Description automatically generated](<lib/NewItem398.png>)

**Figure 10: Power output at each element of the fleet for the case with complete shaving**

&nbsp;

than the specified target band for the first time (see the power monitored in the case without any storage elements and controller in the circuit). The power requested by the controller to element A is limited to its rated power ([*Equation 2*](<OperationinPower-FlowDrivenModes.md>)). All other elements are requested the same power increment. Take elements *B* and *F* , for instance. The total power needed to drive the regulated power to the target is 969#8202;*.*&#8202;34*kW* . As the fleet is constituted by 7 elements and they are all given the same weight (see *Weights* property), the incremental change of power requested is 138#8202;*.*&#8202;48*kW* . As their power consumption during idling state is 2*kW* (1% of *kWRated*) due to idling losses plus 0.43kW due to the corresponding inverter losses (taken from the data exported from monitors *storage B states* and *storage F states*), the power requested to these two elements is 138#8202;*.*&#8202;48 *−* 2#8202;*.*&#8202;43 = 136#8202;*.*&#8202;05*kW* .

As the system’s loading increases to the peak, at 7pm, the controller requests more power from elements *B* to *G*. The amount of incremental power requested is enough to reach storage’s *E*, *F* and *B* rated power, 150*kW* , 200*kW* and 200*kW* , respectively. The other three remaining elements’ rated power is enough to fulfill the requested power necessary to fully shave the peak. See in [Table 2](<PeakShavingCases.md#\_bookmark20>) that it requires an extra control iteration to accomplish this.

At 8pm, the system’s loading starts to decrease. Thus, the controller requests the fleet to reduce its dispatch. Note that because the controller operates by requesting incremental changes in the power dispatched, the entire fleet gets its dispatched power reduced by the same amount: 215#8202;*.*&#8202;108 = 30#8202;*.*&#8202;73*kW* .

At 9pm, storage *E* is completely depleted, as shown in [Figure 11](<OpenDSSDocumentation.md#\_bookmark19>). Thus, the controller does not send any dispatch request to this element. However, the decrement in the power requested to the other six elements is enough to drive the regulated power to the band around the 10.2 MW target. Then, the controller does not push any other actions to the control queue in the second control iteration.

![A graph of a line graph

Description automatically generated with medium confidence](<lib/NewItem397.png>)

**Figure 11: State of charge of each element of the fleet for the case with complete shaving**

&nbsp;

At 10pm, the total loading reduction leads the controller to decrement the total requested power in 778#8202;*.*&#8202;753*kW* , which means that each element is requested to reduce its dispatch by more than 110*kW* in the first control iteration. However, as storage *E* is already idling, only the other 6 elements receive the request. As storage *A* is dispatching less than 50kW at 9pm, the resulting power would be negative, so the element goes into idling state.

The resulting reduction (lower than the required) in the regulated power from the power flow of the next control iteration is not enough to drive it to the target value. Thus, the controller sends new actions (dispatch requests) in the second control iteration. In this iteration, the necessary power

&nbsp;

dispatch reduction is only 149.9kW. The power change requested to the fleet also leads storages *B*

and *F* to go into idling state.

In the third control iteration, the power flow is solved again and the regulated power is finally within the target band. Thus, no more control action are required. Then, at 10pm only storages *C*, *D* and *G* remain in discharge mode and are responsible for shaving the peak.

Finally, at 11pm the system’s loading reduces significantly and the controller sets these three element to idling state as well.

Table 2: Event log of PeakShaving in the simulation case with complete shaving

&nbsp;

| **Hour** | **Control** **Iter.** | **Action** |
| :---: | :---: | --- |
| &#50; | &#49; | FLEET SET TO CHARGING BY TIME TRIGGER |
| &#49;8 | &#49; | ATTEMPTING TO DISPATCH 969.34 KW WITH 7350 KWH REMAINING AND 1470 KWH RESERVE. |
| &#49;8 | &#49; | REQUESTING STORAGE.A TO DISPATCH 100 KW. FINAL KWOUT IS 100 KW |
| &#49;8 | &#49; | REQUESTING STORAGE.B TO DISPATCH 136.05 KW. FINAL KWOUT IS 136.05 KW |
| &#49;8 | &#49; | REQUESTING STORAGE.C TO DISPATCH 134.23 KW. FINAL KWOUT IS 134.23 KW |
| &#49;8 | &#49; | REQUESTING STORAGE.D TO DISPATCH 134.836 KW. FINAL KWOUT IS 134.836 KW |
| &#49;8 | &#49; | REQUESTING STORAGE.E TO DISPATCH 136.657 KW. FINAL KWOUT IS 136.657 KW |
| &#49;8 | &#49; | REQUESTING STORAGE.F TO DISPATCH 136.05 KW. FINAL KWOUT IS 136.05 KW |
| &#49;8 | &#49; | REQUESTING STORAGE.G TO DISPATCH 135.443 KW. FINAL KWOUT IS 135.443 KW |
| &#49;9 | &#49; | ATTEMPTING TO DISPATCH 486.586 KW WITH 6263.18 KWH REMAINING AND 1470 KWH RE- SERVE. |
| &#49;9 | &#49; | REQUESTING STORAGE.B TO DISPATCH 200 KW. FINAL KWOUT IS 200 KW |
| &#49;9 | &#49; | REQUESTING STORAGE.C TO DISPATCH 203.742 KW. FINAL KWOUT IS 203.742 KW |
| &#49;9 | &#49; | REQUESTING STORAGE.D TO DISPATCH 204.349 KW. FINAL KWOUT IS 204.349 KW |
| &#49;9 | &#49; | REQUESTING STORAGE.E TO DISPATCH 150 KW. FINAL KWOUT IS 150 KW |
| &#49;9 | &#49; | REQUESTING STORAGE.F TO DISPATCH 200 KW. FINAL KWOUT IS 200 KW |
| &#49;9 | &#49; | REQUESTING STORAGE.G TO DISPATCH 204.955 KW. FINAL KWOUT IS 204.955 KW |
| &#49;9 | &#50; | ATTEMPTING TO DISPATCH 128.888 KW WITH 6263.18 KWH REMAINING AND 1470 KWH RE- SERVE. |
| &#49;9 | &#50; | REQUESTING STORAGE.C TO DISPATCH 222.154 KW. FINAL KWOUT IS 222.154 KW |
| &#49;9 | &#50; | REQUESTING STORAGE.D TO DISPATCH 222.761 KW. FINAL KWOUT IS 222.761 KW |
| &#49;9 | &#50; | REQUESTING STORAGE.G TO DISPATCH 223.368 KW. FINAL KWOUT IS 223.368 KW |
| &#50;0 | &#49; | ATTEMPTING TO DISPATCH -215.108 KW WITH 4726.16 KWH REMAINING AND 1470 KWH RE- SERVE. |
| &#50;0 | &#49; | REQUESTING STORAGE.A TO DISPATCH 69.2703 KW. FINAL KWOUT IS 69.2703 KW |
| &#50;0 | &#49; | REQUESTING STORAGE.B TO DISPATCH 169.27 KW. FINAL KWOUT IS 169.27 KW |
| &#50;0 | &#49; | REQUESTING STORAGE.C TO DISPATCH 191.425 KW. FINAL KWOUT IS 191.425 KW |
| &#50;0 | &#49; | REQUESTING STORAGE.D TO DISPATCH 192.032 KW. FINAL KWOUT IS 192.032 KW |
| &#50;0 | &#49; | REQUESTING STORAGE.E TO DISPATCH 119.27 KW. FINAL KWOUT IS 119.27 KW |


| &#50;0 | &#49; | REQUESTING STORAGE.F TO DISPATCH 169.27 KW. FINAL KWOUT IS 169.27 KW |
| :---: | :---: | --- |
| &#50;0 | &#49; | REQUESTING STORAGE.G TO DISPATCH 192.638 KW. FINAL KWOUT IS 192.638 KW |
| &#50;1 | &#49; | ATTEMPTING TO DISPATCH -351.972 KW WITH 3496.27 KWH REMAINING AND 1470 KWH RE- SERVE. |
| &#50;1 | &#49; | REQUESTING STORAGE.A TO DISPATCH 18.9886 KW. FINAL KWOUT IS 18.9886 KW |
| &#50;1 | &#49; | REQUESTING STORAGE.B TO DISPATCH 118.989 KW. FINAL KWOUT IS 118.989 KW |
| &#50;1 | &#49; | REQUESTING STORAGE.C TO DISPATCH 141.143 KW. FINAL KWOUT IS 141.143 KW |
| &#50;1 | &#49; | REQUESTING STORAGE.D TO DISPATCH 141.75 KW. FINAL KWOUT IS 141.75 KW |
| &#50;1 | &#49; | REQUESTING STORAGE.F TO DISPATCH 118.989 KW. FINAL KWOUT IS 118.989 KW |
| &#50;1 | &#49; | REQUESTING STORAGE.G TO DISPATCH 142.357 KW. FINAL KWOUT IS 142.357 KW |
| &#50;2 | &#49; | ATTEMPTING TO DISPATCH -778.753 KW WITH 2673.63 KWH REMAINING AND 1470 KWH RE- SERVE. |
| &#50;2 | &#49; | REQUESTING STORAGE.A TO DISPATCH -92.2619 KW. SETTING STORAGE.A TO IDLING STATE. FINAL KWOUT IS -1.21359 KW |
| &#50;2 | &#49; | REQUESTING STORAGE.B TO DISPATCH 7.73813 KW. FINAL KWOUT IS 7.73813 KW |
| &#50;2 | &#49; | REQUESTING STORAGE.C TO DISPATCH 29.8925 KW. FINAL KWOUT IS 29.8925 KW |
| &#50;2 | &#49; | REQUESTING STORAGE.D TO DISPATCH 30.4993 KW. FINAL KWOUT IS 30.4993 KW |
| &#50;2 | &#49; | REQUESTING STORAGE.F TO DISPATCH 7.73813 KW. FINAL KWOUT IS 7.73813 KW |
| &#50;2 | &#49; | REQUESTING STORAGE.G TO DISPATCH 31.1061 KW. FINAL KWOUT IS 31.1061 KW |
| &#50;2 | &#50; | ATTEMPTING TO DISPATCH -149.93 KW WITH 2673.63 KWH REMAINING AND 1470 KWH RE- SERVE. |
| &#50;2 | &#50; | REQUESTING STORAGE.B TO DISPATCH -13.6804 KW. SETTING STORAGE.B TO IDLING STATE. FINAL KWOUT IS -2.42718 KW |
| &#50;2 | &#50; | REQUESTING STORAGE.C TO DISPATCH 8.474 KW. FINAL KWOUT IS 8.474 KW |
| &#50;2 | &#50; | REQUESTING STORAGE.D TO DISPATCH 9.0808 KW. FINAL KWOUT IS 9.0808 KW |
| &#50;2 | &#50; | REQUESTING STORAGE.F TO DISPATCH -13.6804 KW. SETTING STORAGE.F TO IDLING STATE. FINAL KWOUT IS -2.42718 KW |
| &#50;2 | &#50; | REQUESTING STORAGE.G TO DISPATCH 9.6876 KW. FINAL KWOUT IS 9.6876 KW |
| &#50;3 | &#49; | ATTEMPTING TO DISPATCH -1526.14 KW WITH 2627.38 KWH REMAINING AND 1470 KWH RE- SERVE. |
| &#50;3 | &#49; | REQUESTING STORAGE.C TO DISPATCH -209.546 KW. SETTING STORAGE.C TO IDLING STATE. FINAL KWOUT IS -4.24757 KW |
| &#50;3 | &#49; | REQUESTING STORAGE.D TO DISPATCH -208.939 KW. SETTING STORAGE.D TO IDLING STATE. FINAL KWOUT IS -3.64078 KW |
| &#50;3 | &#49; | REQUESTING STORAGE.G TO DISPATCH -208.332 KW. SETTING STORAGE.G TO IDLING STATE. FINAL KWOUT IS -3.03398 KW |


&nbsp;

1. &nbsp;

   1. &nbsp;
      1. **Effect of *MonPhase*** **property**

In the previous example, as the property *MonPhase* has been set to *AV G*. This means that the regulated measure used by the controller is the total three-phase power of the monitored line at the specified terminal, which is, in fact, the power shown in [Figure 9](<OpenDSSDocumentation.md#\_bookmark17>). However, as shown in [Figure 12](<OpenDSSDocumentation.md#\_bookmark21>),

&nbsp;

![A graph showing a number of controllers

Description automatically generated with medium confidence](<lib/NewItem396.png>)

**Figure 12: Powers at the monitored element without controller**

&nbsp;

the simulated circuit is unbalanced. In this case, *MonPhase* may be useful. It allows the user to select a measure in a specific phase to be the controller input value. Consider that we would like to shave the peak adopting the most loaded phase, which is phase B (nodes “2” in the MV level, *MonPhase* = 2). As the monitored element is a 3-phase line, the controller will assume the actual power at the specific location is 3 times the measured quantity, shown in Figures [12](<OpenDSSDocumentation.md#\_bookmark21>) and [13](<OpenDSSDocumentation.md#\_bookmark22>).

![A graph with red lines and numbers

Description automatically generated](<lib/NewItem395.png>)

**Figure 13: Powers at the monitored element for PeakShaving with *MonPhase* = 2**

&nbsp;

[Figure 13](<OpenDSSDocumentation.md#\_bookmark22>) shows that, indeed, the controller regulates the monitored value to the target band. The practical effect is that the actual three-phase power measured stays below the specified target. This would be useful if there is a meter monitoring only a single phase. Supposing that the loading of each phase varies throughout the day such that one phase is the most loaded one during a specific period but not for others, the user could also use *MonPhase* = *MAX* instead (which is the default value), and the controller would look for the most loaded phase at every single time step.

The intent of this property is to guarantee that the controller would not let the power in any individual phase to be overloaded. Note that if *MonPhase* = *AV G*, the regulation of the total 3-phase active power does not mean that the single-phase power in each phase is within the acceptable range if there is significant unbalance.


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation Process with HelpNDoc's Advanced Features](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
