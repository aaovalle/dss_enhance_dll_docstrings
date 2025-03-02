# TechNote EnergyMeter

&nbsp;

***Zones***

&nbsp;

Normally, the EnergyMeter automatically determines its zone by starting with the opposite side of the branch it is monitoring and then tracing forward thoughout the circuit until it finds an open point, open switch, another meter, or a branch that is already included in another meter's zone. This is illustrated in Figure 1. When the EnergyMeter takes a sample, it gets the local values where it is installed and then scours its zone for losses and loads that are judged to be unserved.

&nbsp;

&nbsp;

![Image](<lib/NewItem49.png>)

&nbsp;

***Zonelist Property:*** The "ZONELIST" property, allows you to specify the exact branches you want included in the zone. This would include any branches for which you want the losses tabulated and/or for which you want the check for unserved loads. You can specify the branches as an array of strings in the two standard DSS methods:

&nbsp;

...Zonelist = \[line.L1, line.L2, Transformer.T5, …\]&nbsp;

...ZoneList = (file=69kVList.txt)

&nbsp;

Where "69kVList.txt" is the name of a text file containing the full element name of the branches you wish to include, one to a line.

&nbsp;

***LocalOnly Property:*** Another feature is the LOCALONLY property. This default to NO or FALSE. When set to YES or TRUE, the EnergyMeter does not inspect the zone for unserved energy quantities, although it continues to accumulate the losses in the zone. The zone is defined either automatically or manually. For Energy exceeding Normal and UE values, it only pays attention to the ratings of the branch in which it is installed. It does not query each load to see if it thinks it is unserved. It goes only by the specified rating of the line or transformer where it is installed. This enables you to effectively set a rating on a feeder without the complications of having various parts of the feeder within bounds or not, which can simplify analyses in some cases. The behavior of the KWNORMAL and KWEMERG properties were modified to work with this property. Normally, setting these properties causes the meter to scour the zone, adding up all the load being served (not the total in the lines, which includes losses). When LOCALONLY is specified, the KWNORMAL and KWEMERG property values are assumed to apply to the total metered value at the local site. The feeder is not searched. This likewise allows certain simplification. For example, if you wanted to declare the maximum rating on a feeder to be 15 MW, you would specify the EnergyMeter as follows:

&nbsp;

New energymeter.M1 element=line.firstbranch terminal=1 ~ kwemerg=15000 localonly=yes

&nbsp;

This meter will establish its own radial zone, which should include the entire feeder past "line.firstbranch" and use the 15000 kW limit for UE calcs. EEN would be estimated from the Normal current rating of the line.

&nbsp;

***Combined and VoltageOnly Options***

&nbsp;

Under the Option property, you will now find "Combined" and "Voltageonly" options for dealing with the Load EEN/UE. Originally, a load decided that it was unserved if either its voltage was too low or if an upline branch was overloaded. The overload supercedes the undervoltage because it was assumed the undervoltage was caused by the overload. The problem this was causing was when the undervoltage occured first. This causes a "hitch" in the UE curves because the two are not computed on exactly the same basis. Usually, the curve drops to a lower value instead of rising continuously. The "Combined" option is the default and computes the Load UE based on both overload and undervoltage as the previous default behavior. The Voltageonly option ignores the line overload. Thus, the loads report only the EEN/UE due to low voltage. The overload UE and EEN is still reported in the energymeter registers as before. The only difference would be in the Load UE/EEN numbers. The overload UE/EEN numbers report the largest overload on a radial feeder or the total of all lines in a meshed network.

&nbsp;

***Overload Report***

&nbsp;

During a Yearly simulation, you can optionally turn on an overload exception report. This is done by setting the global option OverloadReport to Yes. The DemandInterval option must also be turned on. At the end each solution, the overloaded power delivery elements are written to a CSV file that can be found in the demand interval (DI) folder for the appropriate year.

&nbsp;

***Voltage Exception Report***&nbsp;

&nbsp;

During a Yearly simulation, you can optionally turn on a bus voltage exception report. This is done by setting the global option VoltExceptionReport to Yes. The DemandInterval option must also be turned on. At the end each solution, the number of buses seeing overvoltage and undervoltage are written to a CSV file that can be found in the demand interval (DI) folder for the appropriate year. The minimum per unit voltage and maximum per unit voltage is also recorded. Therefore, it is recommended that the voltage bases for each bus be defined either by the CalcVoltageBases command or the SetkVBase command. Buses where the base is not defined are ignored.

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly create a professional-quality documentation website with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
