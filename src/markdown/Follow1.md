# Follow

The control is triggered by time (see *TimeDischargeTrigger* property) and resets the *kWTarget* property value to the present monitored element power. In this mode, the fleet tends to be dispatched more often than in PeakShave mode by being dispatched near the peak, even if the daily peak itself significantly varies throughout the simulation period, for instance, throughout the year (in simple PeakShave mode, the fleet may only be dispatched a few days per year). Even though it is triggered by time, it has been classified as a “power flow-driven” mode since, once triggered, and the target value updated, it operates exactly the same as the PeakShaveMode, i.e, it attempts to discharge the fleet to keep power in the monitored element no greater than the new target. *kWThreshold* property can be used in this mode to prevent the fleet to discharge on days when the load is less than the specified value.[ Figure 3](<Schedule.md>) illustrates the operation of the controller in this mode.

***
_Created with the Standard Edition of HelpNDoc: [Easily create PDF Help documents](<https://www.helpndoc.com/feature-tour>)_
