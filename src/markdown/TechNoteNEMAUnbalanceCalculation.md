# TechNote NEMA Unbalance Calculations Added

\
As of this date, the latest OpenDSS build will include the percent NEMA unbalance calculation on the Export SeqVoltages and Export SeqCurrents reports. It is the last column on the report. The NEMA method is frequently used in the US as a measure of the unbalance on motors. By including it on the reports with sequence voltages and currents, it can easily be compared to the negativesequence

unbalance that is used for the same purpose. The values should be close.

&nbsp;

***NEMA Unbalance Method***

&nbsp;

The NEMA method reports the largest difference in magnitude from the average voltage or current, divided by the average, in percent.

It is typically applied as a measure of the voltage unbalance because that is what causes excess heating in motors. However, the OpenDSS can report the value for currents as well The values are reported only for buses and elements having at least 3 phases. The calculation is done for only the first three phases or nodes on a bus. The code for making this computation may be found in the MathUtils.pas module.

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your CHM Help Files with HelpNDoc's Advanced Customization Options](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
