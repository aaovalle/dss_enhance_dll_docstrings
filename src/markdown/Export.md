# Export

&nbsp;

The voltage and current exports have been updated to be more consistent and useful when you load them into Excel or another program.

&nbsp;

• The output tables now stretch out horizontally instead of vertically. This is also done to fit in better with modifications to the Plot command

• Note: Current exports are keyed on device (Circuit Element) name

• Note: Voltage exports are keyed on bus name

• Residual values are also provided (sum of all conductors or nodes at a branch or bus). This is also true for the sequence current and sequence voltage exports because the residuals can be different than the zero-sequence values.

&nbsp;

|  *Export option*&nbsp; |  *Description* |
| :---: | --- |
| AllocationFactors |  Exports load allocation factors. File name is assigned.&nbsp; |
| BranchReliability |  (Default file = EXP\_BranchReliability.CSV) Failure rate, number of interruptions and other reliability data for each PD element.&nbsp; |
| Buscoords |  \[Default file = EXP\_BUSCOORDS.CSV\] Bus coordinates in csv form.&nbsp; |
| BusLevels |  Exports the names and the level of each Bus inside the Circuit based on its topology information. The level value define show far or close is the bus from the circuits backbone (0 means that the bus is at the backbone)&nbsp; |
| BusReliability |  (Default file = EXP\_BusReliability.CSV) Failure rate, number of interruptions and other reliability data at each bus.&nbsp; |
| Capacity |  (Default file = EXP\_CAPACITY.CSV) Capacity report.&nbsp; |
| CDPSMAsset |  \*\* Deprecated \*\* (IEC 61968-13, CDPSM Asset profile)&nbsp; |
| CDPSMElec |  \*\* Deprecated \*\* (IEC 61968-13, CDPSM Electrical Properties profile)&nbsp; |
| CDPSMGeo |  \*\* Deprecated \*\* (IEC 61968-13, CDPSM Geographical profile)&nbsp; |
| CDPSMStateVar |  \*\* Deprecated \*\* (IEC 61968-13, CDPSM State Variables profile)&nbsp; |
| CDPSMTopo |  \*\* Deprecated \*\* (IEC 61968-13, CDPSM Topology profile)&nbsp; |
| CIM100 |  (Default file = CIM100x.XML) (IEC 61968-13, combined CIM100 for unbalanced load flow profile)&nbsp; \[File=filename fid=\_uuidstring Substation=subname sid=\_uuidstring&nbsp; SubGeographicRegion=subgeoname sgrid=\_uuidstring GeographicRegion=geoname rgnid=\_uuidstring\]&nbsp; |
| CIM100Fragments |  (Default file ROOT = CIM100) (IEC 61968-13, CIM100 for unbalanced load flow profile)&nbsp; produces 6 separate files ROOT\_FUN.XML for Functional profile,&nbsp; ROOT\_EP.XML for Electrical Properties profile,&nbsp; ROOT\_TOPO.XML for Topology profile,&nbsp; ROOT\_CAT.XML for Asset Catalog profile,&nbsp; ROOT\_GEO.XML for Geographical profile and&nbsp; ROOT\_SSH.XML for Steady State Hypothesis profile&nbsp; \[File=fileroot fid=\_uuidstring Substation=subname sid=\_uuidstring&nbsp; SubGeographicRegion=subgeoname sgrid=\_uuidstring GeographicRegion=geoname rgnid=\_uuidstring\]&nbsp; |
| Contours |  Exports the Contours matrix (C) calculated after initializing A-Diakoptics. The output format is compressed coordinated and the values are integers.&nbsp; If A-Diakoptics is not initialized this command does nothing&nbsp; |
| Counts |  \[Default file = EXP\_Counts.CSV\] (instance counts for each class)&nbsp; |
| Currents |  (Default file = EXP\_CURRENTS.CSV) Currents in each conductor of each element.&nbsp; |
| deltaF |  Exports the coefficients of the vector deltaF, which is used for storing the injection current estimation when using the NCIM solution algorithm.&nbsp; |
| deltaZ |  Exports the coefficients of the vector deltaZ, which is used for storing the voltage delta estimation when using the NCIM solution algorithm.&nbsp; |
| ElemCurrents |  (Default file = EXP\_ElemCurrents.CSV)&nbsp; Exports the current into all conductors of all circuit elements&nbsp; |
| ElemPowers |  (Default file = EXP\_elemPowers.CSV)&nbsp; Exports the powers into all conductors of all circuit elements&nbsp; |
| ElemVoltages |  (Default file = EXP\_ElemVoltages.CSV)&nbsp; Exports the voltages to ground at all conductors of all circuit elements&nbsp; |
| ErrorLog |  (Default file = EXP\_ErrorLog.TXT) All entries in the present Error log.&nbsp; |
| Estimation |  (Default file = EXP\_ESTIMATION.CSV) Results of last estimation.&nbsp; |
| EventLog |  (Default file = EXP\_EventLog.CSV) All entries in the present event log.&nbsp; |
| FaultStudy |  (Default file = EXP\_FAULTS.CSV) results of a fault study.&nbsp; |
| Generators |  (Default file = EXP\_GENMETERS.CSV) Present values of generator meters. Adding the switch "/multiple" or "/m" will&nbsp; cause a separate file to be written for each generator.&nbsp; |
| GICMvars |  (Default file = EXP\_GIC\_Mvar.CSV) Mvar for each GICtransformer object by bus for export to power flow programs &nbsp; |
| IncMatrix |  Exports the Branch-to-Node Incidence matrix calculated for the circuit in compressed coordinated format (Row,Col,Value)&nbsp; |
| IncMatrixCols |  Exports the names of the Cols (Buses) used for calculating the Branch-to-Node Incidence matrix for the active circuit&nbsp; |
| IncMatrixRows |  Exports the names of the rows (PDElements) used for calculating the Branch-to-Node Incidence matrix for the active circuit&nbsp; |
| Jacobian |  Exports the Jacobian matrix, this matrix is calculated when using the NCIM solution algorithm. The matrix is exported as triplets.&nbsp; |
| Laplacian |  Exports the Laplacian matrix calculated using the branch-to-node Incidence matrix in compressed coordinated format (Row,Col,Value)&nbsp; |
| Loads |  \[Default file = EXP\_LOSSES.CSV\] Losses for each element.&nbsp; |
| Losses |  \[Default file = EXP\_LOSSES.CSV\] Losses for each element.&nbsp; |
| Meters |  (Default file = EXP\_METERS.CSV) Energy meter exports. Adding the switch "/multiple" or "/m" will&nbsp; cause a separate file to be written for each meter.&nbsp; |
| Monitors |  (file name is assigned by Monitor export) Monitor values. The argument is the name of the monitor (e.g. Export Monitor XYZ, XYZ is the name of the monitor). The argument can be ALL, which means that all the monitors will be exported&nbsp; |
| NodeNames |  (Default file = EXP\_NodeNames.CSV) Exports Single-column file of all node names in the active circuit. Useful for making scripts.&nbsp; |
| NodeOrder |  (Default file = EXP\_NodeOrder.CSV)&nbsp; Exports the present node order for all conductors of all circuit elements&nbsp; |
| Overloads |  (Default file = EXP\_OVERLOADS.CSV) Overloaded elements report.&nbsp; |
| P\_byphase | (Default file = EXP\_P\_BYPHASE.CSV) \[MVA\] \[Filename\] Power by phase. Default is kVA. |
| Powers |  (Default file = EXP\_POWERS.CSV) \[MVA\] \[Filename\] Powers (kVA by default) into each terminal of each element.&nbsp; |
| Profile |  \[Default file = EXP\_Profile.CSV\] Coordinates, color of each line section in Profile plot. Same options as Plot Profile Phases property.&nbsp; Example:&nbsp; Export Profile Phases=All \[optional file name\]&nbsp; |
| PVSystem\_Meters |  (Default file = EXP\_PVMETERS.CSV) Present values of PVSystem meters. Adding the switch "/multiple" or "/m" will&nbsp; cause a separate file to be written for each PVSystem.&nbsp; |
| Result |  (Default file = EXP\_Result.CSV)&nbsp; Exports the result of the most recent command . |
| Sections |  (Default file = EXP\_SECTIONS.CSV) Data for each section between over-current protection devices. &nbsp; Examples:&nbsp; &nbsp; &nbsp; Export Sections \[optional filename\]&nbsp; &nbsp; Export Sections meter=M1 \[optional filename\]&nbsp; |
| SeqCurrents |  (Default file = EXP\_SEQCURRENTS.CSV) Sequence currents in each terminal of 3-phase elements.&nbsp; |
| SeqPowers |  (Default file = EXP\_SEQPOWERS.CSV) Sequence powers into each terminal of 3-phase elements.&nbsp; |
| SeqVoltages |  (Default file = EXP\_SEQVOLTAGES.CSV) Sequence voltages.&nbsp; |
| seqz |  (Default file = EXP\_SEQZ.CSV) Equivalent sequence Z1, Z0 to each bus.&nbsp; |
| Storage\_Meters |  (Default file = EXP\_STORAGEMETERS.CSV) Present values of Storage meters. Adding the switch "/multiple" or "/m" will&nbsp; cause a separate file to be written for each Storage device.&nbsp; |
| Summary |  \[Default file = EXP\_Summary.CSV\] Solution summary.&nbsp; |
| Taps |  (Default file = EXP\_Taps.CSV)&nbsp; Exports the regulator tap report similar to Show Taps.&nbsp; |
| Unserved |  (Default file = EXP\_UNSERVED.CSV) \[UEonly\] \[Filename\] Report on elements that are unserved due to violation of ratings.&nbsp; |
| Uuids |  \[Default file = EXP\_UUIDS.CSV\] Uuids for each element. This frees the UUID list after export.&nbsp; |
| Voltages |  (Default file = EXP\_VOLTAGES.CSV) Voltages to ground by bus/node.&nbsp; |
| VoltagesElements |  (Default file = EXP\_VOLTAGES\_ELEM.CSV) Voltages to ground by circuit element.&nbsp; |
| Y |  (Default file = EXP\_Y.CSV) \[triplets\] \[Filename\] System Y matrix, defaults to non-sparse format.&nbsp; |
| Y4 |  Exports the inverse of Z4 (ZCC) calculated after initializing A-Diakoptics. The output format is compressed coordinated and the values are complex conjugates.&nbsp; If A-Diakoptics is not initialized this command does nothing&nbsp; |
| YCurrents |  (Default file = EXP\_YCurrents.CSV)&nbsp; Exports the present solution complex Current array in same order as YNodeList. This is generally the injection current array&nbsp; |
| YNodeList |  (Default file = EXP\_YNodeList.CSV)&nbsp; Exports a list of nodes in the same order as the System Y matrix.&nbsp; |
| Yprims |  (Default file = EXP\_YPRIMS.CSV) All primitive Y matrices.&nbsp; |
| YVoltages |  (Default file = EXP\_YVoltages.CSV)&nbsp; Exports the present solution complex Voltage array in same order as YNodeList.&nbsp; |
| ZCC |  Exports the connectivity matrix (ZCC) calculated after initializing A-Diakoptics. The output format is compressed coordinated and the values are complex conjugates.&nbsp; If A-Diakoptics is not initialized this command does nothing&nbsp; |
| ZLL |  Exports the Link branches matrix (ZLL) calculated after initializing A-Diakoptics. The output format is compressed coordinated and the values are complex conjugates. If A-Diakoptics is not initialized this command does nothing&nbsp; |



***
_Created with the Standard Edition of HelpNDoc: [Achieve Professional Documentation Results with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
