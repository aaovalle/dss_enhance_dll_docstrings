# EnergyMeter EEN and UE Registers

\
Register 9 through 12 on the EnergyMeter are confusing to both new and experienced OpenDSS users. Hopefully, this explanation will help shed some light on the contents of these registers.

&nbsp;

EEN = Energy Exceeding Normal: The energy served over a selected period of time above the “Normal” rating of power delivery devices (lines, transformers, switches, etc.). It is assumed that there is sufficient engineering margin in the power system to continue to operate, but that a failure (1st contingency) will require curtailment of load. This is the primary quantity used for measure of risk.

&nbsp;

UE = Unserved Energy: The energy over a selected period of time projected to be above the Emergency, or Maximum, rating of power delivery equipment. It is assumed that some load will have to be curtailed to bring the power down to a manageable level.

&nbsp;

These concepts have evolved since 1994 as we began to look for some means to measure risk in planning, particularly as it applies to distributed generation. We quickly learned that distribution planners were not comfortable with pure probabilistic planning. They prefer methods based on concrete limits. Therefore, we adapted some traditional planning concepts to achieve a measure of risk. Many traditional methods used two limits for power delivery equipment: Normal and Emergency. Planning studies are triggered when the peak demand exceeds the Normal limits. Exceeding the Emergency limit requires immediate curtailment. The usual intent was to get something built before the Emergency limit was projected to be exceeded. By using power demand alone, new construction is frequently very conservative. Distributed generation muddies the waters for planning with demand alone because it is often unclear how much capacity is actually achieved by DG.

&nbsp;

Our extension of the concept was to use energy in addition to simply power to determine the risk. One would defer investing in new infrastructure until the energy exceeding the limits was sufficient to justify it.

&nbsp;

For more on this subject, see the following papers for reference on this subject:

&nbsp;

[R. C. Dugan, “Computing Incremental Capacity Provided By Distributed Resources For Distribution Planning,” IEEE PES General Meeting, 2007.](<https://ieeexplore.ieee.org/document/4275881> "target=\"\_blank\"")

&nbsp;

[Roger Dugan and Marek Waclawiak, “Using Energy as a Measure of Risk in Distribution Planning,” Paper 0822, CIRED 2007, Vienna.](<http://www.cired.net/publications/cired2007/pdfs/CIRED2007\_0822\_paper.pdf> "target=\"\_blank\"")


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
