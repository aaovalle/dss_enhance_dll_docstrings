# Time

In Time mode all storage elements are set to discharge when in the course of simulation the time of day passes the specified hour of day by the *TimeDisChargeTrigger* property (hour is a decimal value, e.g., 10.5 = 1030). The storage elements go into idling mode when their storage declines to the reserve value. The discharging rate is set by the *%RatekW* property.

For charging, it operates similarly, but triggered by *TimeChargeTrigger*. The storage elements switch to the idling mode when the storage is completely charged or the mode is changed by the controller. This is the default mode for charging. The charging rate is set by the *%RateCharge* property.

The algorithm for this mode is quite simple. Whenever the simulation time instant *t* passes either *TimeChargeTrigger* or *TimeDischargeTrigger*, each element of the fleet is set to charge or dis- charge, respectively, by the specified rate if it has enough energy capacity left. It is important to note that the controller sends a request to the fleet at the specific time instant *t* only and, if nothing else changes the state of a particular element of the fleet (for instance, a manual state request or rate of dispatch change through *state* and *kW* storage element properties), it will keep following the request sent at *t*, until its fully charged or depleted down to %*reserve*.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Support Your Windows Applications with HelpNDoc's CHM Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
