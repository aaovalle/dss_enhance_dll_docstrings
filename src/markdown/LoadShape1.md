# LoadShape

&nbsp;

In this mode both discharging and charging precisely follow a per-unit LoadShape curve. The con- troller sends a new request to each storage element of the fleet whenever there has been a change in the curve value. When the value is positive all units are discharged at the rate of the per-unit value of the curve. When the value is zero, all units are set to idling. When the value is negative, all units are set to charging at the rate of the per unit value of the curve. This mode has the same operation principle as the “Follow” self-dispatch mode for storage elements \[[2](<References2.md#\_bookmark38>)\].


***
_Created with the Standard Edition of HelpNDoc: [Ensure High-Quality Documentation with HelpNDoc's Hyperlink and Library Item Reports](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
