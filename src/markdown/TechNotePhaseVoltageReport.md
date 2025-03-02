# TechNote Phase Voltage Report

&nbsp;

***New EnergyMeter Property: PhaseVoltageReport***

&nbsp;

*Applies to version 7.3.3 Build 56 or later.*

&nbsp;

This report was added to evaluate the phase voltages during a yearly simulation. The per unit min, max, and average voltage are reported for each phase (phases 1, 2, and 3 only) at each hour of the simulation. The results are segregated by voltage base within the meter's zone. This is an EnergyMeter object function and must be turned on for each energy meter for which you wish to see the report. The report applies only to a meter's zone, not to any other part of the circuit. Therefore, you can position.&nbsp;

&nbsp;

This property may be found under the Energy Meter help listing, which is the following:

&nbsp;

{Yes \| No} Default is NO. Report min, max, and average phase voltages for the zone and tabulate by voltage base. Demand Intervals must be turned on (Set Demand=true) and voltage bases must be defined for this property to take effect. Result is in a separate report file.

&nbsp;

The Phase Voltage Report is generated during Yearly simulations in which Demand Interval (DI) metering is turned on and Verbose mode is specified. The default is no report. The report is a csv file with the min, max, and avg for the per unit voltages at each of the first three phases. So the conditions for getting the report are:

&nbsp;

&#49;. Voltage Bases defined

&#50;. Verbose Demand Intervals turner on (Set Demand=true DIVerbose=true)

&nbsp;

Compile (C:\\DSSdata\\IEEETest\\8500Node\\master.dss)

New Energymeter.m1 Line.ln58159001

&#49; PhaseVoltageReport=yes \! Turn report flag on

Set Maxiterations=20 \! Sometimes the solution takes more than the default 15 iterations

Solve

set casename=ExampleCase

set mode=yearly number= 168 \! one week of hourly simulation (omit "number=168' to get the whole year)

Set overloadreport=true \! TURN OVERLOAD REPORT ON

Set voltexcept=true \! voltage exception report

set demand=true \! demand interval ON

set DIVerbose=true \! verbose mode is ON

Set Year=1 \! This statement resets all meters

solve

closeDI \! Close any open DI files

"Hour", 12.5kV\_Phs\_1\_Max, 12.5kV\_Phs\_2\_Max, 12.5kV\_Phs\_3\_Max, 12.5kV\_Phs\_1\_Min, 12.5kV\_Phs\_2\_Min, 12.5kV\_Phs\
&#49;, 1.04914, 1.0498, 1.0501, 1.04914, 1.0498, 1.0501, 1.04914, 1.0498, 1.0501

&#50;, 1.04914, 1.0498, 1.0501, 1.04914, 1.0498, 1.0501, 1.04914, 1.0498, 1.0501

&#51;, 1.04914, 1.0498, 1.0501, 1.04914, 1.0498, 1.0501, 1.04914, 1.0498, 1.0501

&#52;, 1.049, 1.04977, 1.05012, 1.049, 1.04977, 1.05012, 1.049, 1.04977, 1.05012

&#53;, 1.04897, 1.04976, 1.05012, 1.04897, 1.04976, 1.05012, 1.04897, 1.04976, 1.05012

&#54;, 1.04888, 1.04974, 1.05013, 1.04888, 1.04974, 1.05013, 1.04888, 1.04974, 1.05013

&#55;, 1.04882, 1.04973, 1.05014, 1.04882, 1.04973, 1.05014, 1.04882, 1.04973, 1.05014

&#56;, 1.04862, 1.04968, 1.05016, 1.04862, 1.04968, 1.05016, 1.04862, 1.04968, 1.05016

&#57;, 1.0485, 1.04965, 1.05017, 1.0485, 1.04965, 1.05017, 1.0485, 1.04965, 1.05017

&#49;0, 1.0483, 1.04961, 1.05019, 1.0483, 1.04961, 1.05019, 1.0483, 1.04961, 1.05019

&#49;1, 1.04821, 1.04959, 1.0502, 1.04821, 1.04959, 1.0502, 1.04821, 1.04959, 1.0502

&#49;2, 1.04727, 1.04937, 1.0503, 1.04727, 1.04937, 1.0503, 1.04727, 1.04937, 1.0503

&nbsp;

The output file will be written to a directory under the home directory for the circuit along with the rest of the demand interval (DI) data. The relative path is:&nbsp;

&nbsp;

casename\\DI\_YR\_nn\\&nbsp;

&nbsp;

where nn= the year being solved.&nbsp;

&nbsp;

You can easily paste this file into a spreadsheet program for further processing.

***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
