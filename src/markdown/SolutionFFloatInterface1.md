# SolutionF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double SolutionF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Solution.Frequency read

This parameter returns the frequency for the next solution.

&nbsp;

### Parameter 1: Solution.Frequency Write

This parameter sets the frequency for the next solution.

&nbsp;

### Parameter 2: Solution.Seconds read

This parameter returns the seconds from top of the hour.

&nbsp;

### Parameter 3: Solution.Seconds Write

This parameter sets the seconds from top of the hour.

&nbsp;

### Parameter 4: Solution.StepSize read

This parameter returns the step size for the next solution.

&nbsp;

### Parameter 5: Solution.StepSize Write

This parameter sets the step size for the next solution.

&nbsp;

### Parameter 6: Solution.LoadMult read

This parameter returns the default load multiplier applied to all non-fixed loads.

&nbsp;

### Parameter 7: Solution.LoadMult Write

This parameter sets the default load multiplier applied to all non-fixed loads.

&nbsp;

### Parameter 8: Solution.Tolerance read

This parameter returns the solution convergence tolerance.

&nbsp;

### Parameter 9: Solution.Tolerance Write

This parameter sets the solution convergence tolerance.

&nbsp;

### Parameter 10: Solution.pctgrowth read

This parameter returns the percent default annual load growth rate.

&nbsp;

### Parameter 11: Solution.pctgrowth Write

This parameter sets the percent default annual load growth rate.

&nbsp;

### Parameter 12: Solution.GenkW read

This parameter returns the generator kW for AutoAdd mode.

&nbsp;

### Parameter 13: Solution.GenkW Write

This parameter sets the generator kW for AutoAdd mode.

&nbsp;

### Parameter 14: Solution.GenPF read

This parameter returns the pf for generators in AutoAdd mode.

&nbsp;

### Parameter 15: Solution.GenPF Write

This parameter sets the pf for generators in AutoAdd mode.

&nbsp;

### Parameter 16: Solution.Capkvar read

This parameter returns the capacitor kvar for adding in AutoAdd mode.

&nbsp;

### Parameter 17: Solution.Capkvar Write

This parameter sets the capacitor kvar for adding in AutoAdd mode.

&nbsp;

### Parameter 18: Solution.GenMult read

This parameter returns the default multiplier applied to generators (like LoadMult).

&nbsp;

### Parameter 19: Solution.GenMult Write

This parameter sets the default multiplier applied to generators (like LoadMult).

&nbsp;

### Parameter 20: Solution.dblHour read

This parameter returns the hour as a double, including fractional part.

&nbsp;

### Parameter 21: Solution.dblHour Write

This parameter sets the hour as a double, including fractional part.

&nbsp;

### Parameter 22: Solution.StepSizeMin 

This parameter sets the step size in minutes.

&nbsp;

### Parameter 23: Solution.StepSizeHr

This parameter sets the step size in Hours.

&nbsp;

### Parameter 24: Solution.Process\_Time

This parameter retrieves the time required (microseconds) to perform the latest solution time step, this time does not include the time required for sampling meters/monitors.

&nbsp;

### Parameter 25: Solution.Total\_Time read

This parameter retrieves the accumulated time required (microseconds) to perform the simulation.

&nbsp;

### Parameter 26: Solution.Total\_Time Write

This parameter sets the accumulated time (microseconds) register. The new value for this register must be specified in the argument.

&nbsp;

### Parameter 27: Solution.Time\_TimeStep

This parameter retrieves the time required (microseconds) to perform the latest solution time step including the time required for sampling meters/monitors.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
