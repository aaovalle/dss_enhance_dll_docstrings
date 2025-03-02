# Common Information Model (CIM100)

&nbsp;

OpenDSS is able to export distribution network models in a candidate “CIM100” version, which is based on extensions of CIM17, which was standardized in 2020. These extensions are important in modeling North American distribution systems. There were plans to conduct interoperability tests in 2020, but these have been delayed by the Covid 19 pandemic until May 2022.

&nbsp;

The CIM extensions and model export functions have been maintained under the U. S. Department of Energy’s GridAPPS-D project \[1-4\]. In particular, \[1\] describes the overall project and the CIM transformer model, \[2\] describes the CIM unbalanced line model and the advantages of a triple-store database for CIM, \[3\] describes the relevant CIM UML while \[4\] contains a Java tool for importing CIM files. This Java tool uses the Blazegraph triple-store; it supersedes the legacy OpenDSS cdpsm\_import code that is archived on SourceForge, but no longer maintained. The tools at \[4\] support CIM import, OpenDSS export from CIM, and GridLAB-D export from CIM. They also include OpenDSS converters from two commercial tools, but these have not been comprehensively tested. Instead, one goal of the GridAPPS-D project is to encourage CIM adoption by many tool vendors, which would lower the burden of model conversion and lower other costs of integration.

&nbsp;

The common distribution power system model (CDPSM) is a CIM profile standardized in IEC 61968-13. To comply with the standard, OpenDSS can export a model into six different sub-profiles:

&nbsp;

• Functional (FUN) – defines nearly all components with names, phasing, grounding, base voltage, feeder containment, terminals, operational limits, DER production source and operating status.

&nbsp;

• Electrical Properties (EP) – voltage and power ratings, control settings, impedances, etc.

&nbsp;

• Topological (TOPO) – adds ConnectivityNodes, i.e., buses. There is a one-to-one correspondence of ConnectivityNodes and TopologicalNodes; OpenDSS doesn’t use TopologicalNodes.

&nbsp;

• Catalog (CAT) – impedances and ratings defined in xfmrcode, linecode, spacing, wiredata, etc.

&nbsp;

• Geographic (GEO) – locations, coordinate system and coordinates

&nbsp;

• Steady-State Hypothesis (SSH) – load and DER p and q values, source voltages, switch states

&nbsp;

A valid power flow model requires all six, with a possible exception of GEO. For convenience, OpenDSS can export all six into a single file. An open-source tool to combine them has been provided at \[5\], in the file utils/CombineModelXMLFiles.py.

&nbsp;

To test the CIM export functions, use the cim\_test.dss file under the Test directory installed with OpenDSSCmd:

&nbsp;

redirect IEEE13\_CDPSM.dss&nbsp;

solve&nbsp;

uuids file=IEEE13Nodeckt\_Base\_UUIDS.dat&nbsp;

export cim100 substation=subname geo=region subgeo=subregion file=ieee13cdpsm.xml&nbsp;

export cim100fragments substation=subname geo=region subgeo=subregion file=ieee13cdpsm&nbsp;

export UUIDS&nbsp;

&nbsp;

redirect IEEE13\_Assets.dss&nbsp;

solve&nbsp;

uuids file=IEEE13NodecktAssets\_Base\_UUIDS.dat&nbsp;

export cim100 substation=subname geo=region subgeo=subregion file=ieee13assets.xml&nbsp;

export cim100frag substation=subname geo=region subgeo=subregion file=ieee13assets

export UUIDS

&nbsp;

Line 1 reads a local copy of the IEEE 13-bus model, with PV, storage, a service transformer, and various switches added. Besides IEEE13\_CDPSM.dss, it includes IEEE13NodeExtra\_BusXY.dat as input for bus coordinates. Line 8 reads a local copy of the IEEE 13-bus model, with transformer codes and line spacings used. Besides IEEE13\_Assets.dss, it includes IEEE13Node\_BusXY.csv as input for bus coordinates. In combination, these two files test most of the CIM classes that can be exported.

&nbsp;

Lines 2 and 9 solve the models, which is a prerequisite for CIM export.

&nbsp;

Lines 3 and 10 read CIM mRID attributes that have been saved from a previous export. Without this, the mRID attributes will be re-generated randomly each time a model is exported. The intent of the mRID is to maintain persistent object identification, so once established, these values need to be reused. (Note: during the very first CIM export, Lines 3 and 10 would be commented out because there are no previous mRID values available. In that case, random mRID values will be generated in Lines 4-5 and 11-12.) The mRID is implemented as a Universally Unique Identifier (UUID) version 4, according to IETF RFC 4122. Every named object in OpenDSS can have a mRID assigned or generated randomly when needed. During CIM export, there are other CIM identified objects that must have mRIDs, even if they are not identified with names in OpenDSS. The CIM Terminal is one example, and the individual Wires Phase objects provide other examples. The uuids command calls in Lines 3 and 10 take care of these extra mRIDs.

&nbsp;

Lines 4-5 and 11-12 create the CIM XML files. The CIM feeder name will be the same as the OpenDSS circuit name. In addition, the CIM models must have substation, geographic region and subgeographic region objects, which are optional named attributes on lines 4-5 and 11-12. If you run these export commands repeatedly on an OpenDSS file that didn’t change, the CIM XML files should not change either, because of the uuids commands invoked on Lines 3 and 10.

&nbsp;

Lines 4 and 11 create single files that contain all six CDPSM profiles within a single file for each circuit, ieee13cdspm.xml and ieee13assets.xml, respectively. This combined file is complete for power flow modeling, but some tools don’t export all six of the CDPSM profiles. An example might be a GIS.

&nbsp;

Lines 5 and 12 export the same information into six separate files for each circuit, using ieee13cdpsm and ieee13assets respectively as the root file names. The rest of the file names will be like ieee13cdspm\_FUN.XML, ieee13cdspm\_EP.XML, ieee13cdspm\_TOPO.XML, ieee13cdspm\_CAT.XML, ieee13cdspm\_GEO.XML or ieee13cdspm\_SSH.XML, indicating the profile contained within. These could be combined with the CombineModelXMLFiles.py script provided at \[5\], to create a file with the same content as ieee13cdpsm.xml. This combination step is needed when two or more tools must collaborate to produce the complete set of six files.

&nbsp;

Lines 6 and 13 write all the mRID, aka UUID, values to the default file names. If there have been changes to the OpenDSS model, copy those UUID files to the file names used in Lines 3 and 10. That way, mRID values will be properly maintained. This step produces one output file, named like IEEE13Nodeckt\_EXP\_UUIDS.CSV.

&nbsp;

The mRID lists are created and freed for each new CIM export, if you follow either of these patterns, after defining and solving the circuit:

&nbsp;

• First export of CIM: export cim100 and then export uuids

• Subsequently: uuids followed by export cim100 and then finally export uuids

&nbsp;

**Modeling Notes**

&nbsp;

When constructing OpenDSS models for CIM export:

&nbsp;

&#49;. Use realistic values for the kVA ratings of line voltage regulating transformers, with XLT=0.01 or lower. If using 10 times the actual kVA rating, as suggested in some other documentation, the operational current limits in CIM will be unrealistically high.

&#50;. Storage elements control their own power, based on the state=\[charging, discharging, idling\]. To maintain a specific value of dispatched power through the CIM export process, use the %charge and %discharge parameters as multipliers on the rated power, rather than specify kW directly.

&nbsp;

**References**

&nbsp;

\[1\] R. B. Melton et al., "Leveraging Standards to Create an Open Platform for the Development of Advanced Distribution Applications," IEEE Access, vol. 6, pp. 37361-37370, 2018, doi: 10.1109/ACCESS.2018.2851186.

\[2\] T. E. McDermott, E. G. Stephan, and T. D. Gibson, "Alternative Database Designs for the Distribution Common Information Model," in 2018 IEEE/PES Transmission and Distribution Conference and Exposition (T\&D), 16-19 April 2018 2018, pp. 1-9, doi: 10.1109/TDC.2018.8440470.

\[3\] Pacific Northwest National Laboratory. "GridAPPS-D." http://gridappsd.readthedocs.io/en/latest (accessed 2020).

\[4\] Pacific Northwest National Laboratory. "CIM Importer and Test Files." https://github.com/GRIDAPPSD/Powergrid-Models (accessed 2020).

\[5\] Pacific Northwest National Laboratory. "CIMHub." https://github.com/GRIDAPPSD/CIMHub/tree/develop (accessed 2020).


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
