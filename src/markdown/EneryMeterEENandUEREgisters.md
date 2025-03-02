# EneryMeter EEN and UE REgisters

&nbsp;

Register 9 through 12 on the EnergyMeter are confusing to both new and experienced OpenDSS users. Hopefully, this explanation will help shed some light on the contents of these registers.

&nbsp;

•**EEN** = Energy Exceeding Normal: The energy served over a selected period of time above the “Normal” rating of power delivery devices (lines, transformers, switches, etc.). It is assumed that there is sufficient engineering margin in the power system to continue to operate, but that a failure (1st contingency) will require curtailment of load. This is the primary quantity used for measure of risk.

&nbsp;

•**UE** = Unserved Energy: The energy over a selected period of time projected to be above the Emergency, or Maximum, rating of power delivery equipment. It is assumed that some load will have to be curtailed to bring the power down to a manageable level.

&nbsp;

These concepts have evolved since 1994 as we began to look for some means to measure risk in planning, particularly as it applies to distributed generation. We quickly learned that distribution planners were not comfortable with pure probabilistic planning. They prefer methods based on concrete limits. Therefore, we adapted some traditional planning concepts to achieve a measure of risk. Many traditional methods used two limits for power delivery equipment: Normal and Emergency. Planning studies are triggered when the peak demand exceeds the Normal limits. Exceeding the Emergency limit requires immediate curtailment. The usual intent was to get something built before the Emergency limit was projected to be exceeded. By using power demand alone, new construction is frequently very conservative. Distributed generation muddies the waters for planning with demand alone because it is often unclear how much capacity is actually achieved by DG.

&nbsp;

Our extension of the concept was to use energy in addition to simply power to determine the risk. One would defer investing in new infrastructure until the energy exceeding the limits was sufficient to justify it.

&nbsp;

For more on this subject, see the following papers for reference on this subject:

&nbsp;

[R. C. Dugan, “Computing Incremental Capacity Provided By Distributed Resources For Distribution Planning,” IEEE PES General Meeting, 2007.](<https://ieeexplore.ieee.org/abstract/document/4275881> "target=\"\_blank\"")

[Roger Dugan and Marek Waclawiak, “Using Energy as a Measure of Risk in Distribution Planning,” Paper 0822, CIRED 2007, Vienna.](<http://www.cired.net/publications/cired2007/pdfs/CIRED2007\_0822\_paper.pdf>)

&nbsp;

***Registers 9 and 10: Overload EEN and UE***

&nbsp;

As the Energymeter element sweeps through its zone, it queries each series power delivery element encountered for the kW above Normal and Emergency limits. The value recorded in these two registers is the largest kW amount encountered. In other words, the value is the maximum overload in terms of actual kW.

&nbsp;

Most of the time, this is what you want. However, there are cases where data errors can skew the results. For example, if the data show a 15 kVA transformer serving an apartment building with over 150 kVA load, this will consistently show up as a 135 kVA overload, which might be the largest overload in the problem. However, you would not build a new feeder because a small transformer is overloaded. You would change out the transformer (or correct the data error). Such errors are common in distribution data where it may take a while for transformer changeouts to get properly entered.

&nbsp;

**Excess or Total**: There are two ways these registers can record the results. They can simply record the excess kW over the limits. This is the default behavior. However, they can also record the total kW flowing through the element. The latter method is for cases where it is assumed that the feeder branch in question must be switched off completely if an overload occurs. This reflects a more conservative planning approach.

&nbsp;

**Registers 11 and 12: Load EEN and UE**

&nbsp;

These two registers record a different approach to compute EEN and UE values: They ask each Load element in the zone if it is “unserved.” The nominal criterion is undervoltage.

&nbsp;

If you set Option=Voltage for an Energymeter object, only the voltage is used. The global options NormVminpu and EmergVminpu are used for this value. If the voltage is between NormVminpu and EmergVminpu, the EEN is proportioned to how far below the NormVminpu it is. If the voltage is less than EmergVminpu, the UE value for the load is computed in proportion to the degee it is below EmergVminpu, continuing on the same slope as the EEN calculation. In multiphase elements, the lowest phase voltage is used.

&nbsp;

The default behavior Option=Combined is to consider both line overload and undervoltage. If a line, or other power delivery element, serving the load is overloaded, the load is considered unserved in the same percentage that the line is overloaded. This actually takes precedence over the voltage criteria, which assumes that any undervoltage is due to the line overload. A line is considered to serve the load if it is between the EnergyMeter and the load. Note that some inaccuracies can occur if the meter zone is not properly defined, such as if loops exist.

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily create HTML Help documents](<https://www.helpndoc.com/feature-tour>)_
