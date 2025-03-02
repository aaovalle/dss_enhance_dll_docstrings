# Violation of Inverter Capability Curve Limits

Whenever the total complex power determined by the combination of the available (for PVSystem) or the desired (for Storage) active power output and the reactive power resulting from the application of the functions described in this document exceeds the inverter capability curve, OpenDSS ensures that it will return to the allowed operating region. This “returning” can be controlled by the user by assigning different priorities. There are three types of priorities: active power, reactive power, and power factor. They can be selected through two parameters of the PCE:

* *WattPriority* \[Yes#8202;*\|*&#8202;No or True#8202;*\|*&#8202;False\]: If set to True, priority is given to active power. If set to False, priority is given to reactive power. Defaults to False.
* *PFPriority* \[Yes#8202;*\|*&#8202;No or True#8202;*\|*&#8202;False\]: If set to True, priority is given to power factor and *WattPriority* is neglected. It works only if operating in either constant PF or constant kvar modes. Defaults to False.

Depending on the region where the desired complex power is located, different priorities lead to different final operating points, as follows:

&nbsp;

* *kV A* Violation: The desired active and reactive power are less than their limits, *kvarMax* and *kWRated*, respectively. In this case, all three priorities are applicable, as shown in [Figure 4a](<OpenDSSDocumentation.md#\_bookmark5>).

&nbsp;

* *kWRated* Violation: The final operating point will be on the *kWRated* axis regardless the priority selected, as shown in [Figure 4b](<OpenDSSDocumentation.md#\_bookmark5>). If either VW or Limit DER Power Output functions are also active, the most restricting limit applies.

&nbsp;

* *kWRated* and *kV A* Violation: In this region, first the active power output is limited by *kWRated*, and then, the same rules apply as for *kV A* violation case. If *WattPriority* is set to True, the final operating point will be at the intersection of *kV A* and *kWRated*, as shown in [Figure 4c](<OpenDSSDocumentation.md#\_bookmark5>).

&nbsp;

* *kvarMax* Violation: In this region, only active power and power factor priorities apply. In both cases the final reactive power is limited by *kvarMax*, as shown in [Figure 4d](<OpenDSSDocumentation.md#\_bookmark5>).

&nbsp;

* Reactive Power Violation on Region of Ascending Linear Limit: The power factor priority is not applicable in the region of ascending linear reactive power limit because the limit crosses the complex plane origin. Thus, only active power priority applies, as shown in [Figure 4e](<OpenDSSDocumentation.md#\_bookmark5>).

&nbsp;

* *kvarMax* and *kV A* Violation: In this region, first the reactive power output is limited by *kvarMax*, and then, the same rules apply as for *kV A* violation case. With *WattPriority* set to False, the final operating point will be at the intersection of *kV A* and *kvarMax*, as shown in [Figure 4f](<OpenDSSDocumentation.md#\_bookmark5>).

&nbsp;

* *kWRated*, *kvarMax* and *kV A* Violation: First, *kWRated* limit is applied, then *kvarMax*, and finally, *kV A*. The final operating point will be at the intersection of *kV A* and *kWRated* if *WattPriority* is True, and at the intersection of *kV A* and *kvarMax* if *WattPriority* is False, as shown in [Figure 4g](<OpenDSSDocumentation.md#\_bookmark5>).

&nbsp;

![A graph of a function

Description automatically generated](<lib/NewItem565.png>)

**Figure 4: Response for Violations in Different Regions of the Inverter Capability Curve and for Different Priorities**


***
_Created with the Standard Edition of HelpNDoc: [Add an Extra Layer of Security to Your PDFs with Encryption](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
