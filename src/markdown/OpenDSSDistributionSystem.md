# OpenDSS Distribution System

&nbsp;

![Image](<lib/NewItem285.png>)

&nbsp;

Prior to the 1990's, Distribution System Analysis was typically performed on the area of the power delivery system designated "Traditional Distribution" in the figure above. This includes the distribution substation and the MV feeders and loads served by that substation. The feeders generally emanate radially from the MV bus in the substation. By the mid-1990's the distribution planning problem had expanded to include part for the HV system, typically called "subtransmission" in the US. This need developed from the inclusion of distributed energy resources (DER) in the planning area among other things. This is the area that is labelled "OpenDSS Distribution". **This is the part of the power delivery system that OpenDSS was designed to analyze**: one or more traditional radial MV systems and a part of the subtransmission systems that interconnected them. Many of the benefits for DER installed at the MV buses were for the HV subtransmission system and it is necessary to model both the HV and MV circuits to see these benefits.

&nbsp;

While the MV feeders were generally configured as radials and can be simulated by relatively simple forward-backward sweep techniques, the subtransmission system is often meshed. This requires a solver with different capabilities. Thus, the DSS was created with a full 3-phase nodal admittance, or Y-matrix, solver. Electrotek had experience doing this kind of modeling in its SuperHarm harmonics analysis application and many of the same modeling techniques were employed. The 3-phase model was extended to a general n-phase model to accommodate the various transformer models and parallel circuits sharing neutral conductors.

&nbsp;

It wasn't long using this model that we discovered we were not getting the correct answer due to the varying renewable generation installed in the planning area. Overloads and overvoltages were not discoverable using the traditional static power flow analysis for one instant in time. Therefore, extensive capabilities for modeling Daily and Yearly load shapes were added to the DSS to make it a unique distribution system analysis tool for its time.

&nbsp;

The power flow solution technique was fine-tuned to execute long quasi-static time series (QSTS) simulations such as 8760-hour yearly simulations efficiently. The solution techniques have been improved over the years with additions such as parallel processing capabilities. By making the DSS open source, EPRI has allowed other researchers to take advantage of our learnings as we've sought to improve distribution system analysis.

***
_Created with the Standard Edition of HelpNDoc: [Experience a User-Friendly Interface with HelpNDoc's Documentation Tool](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
