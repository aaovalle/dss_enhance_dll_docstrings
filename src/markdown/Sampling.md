# Sampling

\
The sampling algorithms are as follows:\
\
**Local Energy and Power Values**: Simply compute the power into the terminal on which the meter is installed and integrate using the interval between the present solution and the previous solution. This operation uses the voltage and current computed from the present solution.

&nbsp;

**Losses in Zone**: Accumulate the kW losses in each power delivery element in the zone.\
\
**Load in Zone:** While sampling the losses in each power delivery element, accumulate the power in all loads connected to the downline bus(es) of the element.

&nbsp;

**Overload Energy in Zone:** For each power delivery element in the zone, compute the amount of power exceeding the rating of the element compared to both normal and emergency ratings.

&nbsp;

**EEN and UE in Zone:** For each load in the zone marked as exceeding normal or unserved, compute the present power. Integrate to get energies.

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring environment](<https://www.helpndoc.com/help-authoring-tool>)_
