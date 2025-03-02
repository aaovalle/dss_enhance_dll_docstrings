# Brief History and Objectives

&nbsp;

Development of the OpenDSS program began in April 1997 at Electrotek Concepts, Inc. At that time the program was simply called “DSS” for Distribution System Simulator. Roger Dugan was the principal author of the software supported shortly thereafter by Tom McDermott. The two comprised the development team until late 2001 when Tom left Electrotek. Roger continued maintaining and evolving the program alone until recently when Tom again became part of the development team through the OpenDSS project. The DSS had been acquired by EPRI Solutions in 2004, which was united with EPRI in 2007. In 2008, EPRI released the software under an open source license to cooperate with other grid modernization efforts active in the Smart Grid area.

&nbsp;

There were two events that triggered the development of the DSS in 1997:

&nbsp;

**&#49;**. EPRI had issued an RFP earlier for software to support the application of distributed generation to distribution systems. While Electrotek was not awarded a contract there had been enough thinking about the project to have arrived at a functional spec for a simulator that would support most of the electrical system analysis for evaluating DG or DER for distribution planning purposes.

&nbsp;

**&#50;**. Roger Dugan was serving as Chair of the IEEE PES Software Engineering Working Group and one of the hot topics at that time was object-oriented programming and data representations. The late Mark Enns of Electrocon had issued a challenge to the group for someone to implement some of the principles we had been discussing in a power system analysis program. The distribution system simulator concept seemed the perfect vehicle to experiment with some of those ideas and provide a useful tool to support the needs of a consulting company that was involved in leading-edge research in distribution system analysis.

&nbsp;

Prior to 1997, Electrotek had been performing DG studies for distribution planning using conventional distribution system analysis methods that are still employed by many tools today. We were well aware of the limitations of these methods and wanted a tool that was more powerful and flexible. One issue we discovered early on is that no two DER planning studies were exactly alike, and we were frequently having to adjust our models and add new features to our tools. Thus, we needed a tool that would not lock us in to only the limited number of analysis types we could think of at the moment. Other issues we set out to address were:

&nbsp;

**\-** The distribution system model data we received from utilities came in all sorts of different formats, each with different strengths and various modeling limitations. One design goal was to develop an object-oriented circuit description language that minimized the conversion effort.

&nbsp;

**\-** Window-based programs can be very user friendly, but we noticed some of the distribution system analysis tools really limited what you can do by limiting the interaction to what is available on the dialog forms. By being fundamentally script-driven, the DSS program approach gets around much of the limited-dialog issue and allows the user to better adapt the analysis process to the problem at hand.

&nbsp;

**\-** The greater value of DER is often found on the subtransmission system serving a distribution planning area. Many distribution planning tools represent only the radial distribution system. Because of the methods employed by the economists we were working with at the time, we wanted a tool that would allow us to model several substations and the distribution circuits between them simultaneously. This is the concept of “distribution” used by much of the rest of the world outside North America. See the next section in this chapter.

&nbsp;

**\-** A key capability desired for the tool was to capture both the time- and location-dependent value of DG. The location-dependent value is captured by modeling the DER in its actual location on the circuit. Capturing the time-dependent value requires extraordinary loadshape modeling capability to support sequential-time simulations.

&nbsp;

**\-** There are many instances where it becomes necessary to model elements with many phases – not just one, two, or three. For example, power poles in North America with multiple circuits may have as many as 4 circuits sharing a common neutral. Also, we wanted to be able to model what happens when a 69 kV line falls into the 13.2 kV distribution line. Or to model a communications signal passing from one voltage level to another through the interwinding capacitance of the transformer – this was not possible with many traditional distribution system analysis tools.

&nbsp;

**\-** We wanted a tool that could seamlessly incorporate harmonics analysis into the power flow analysis without requiring the user to laboriously enter nonlinear device models. We also recognized that we would need at least simple dynamics analysis enough for DER interconnection evaluation. Simple dynamics models were built into the program in the beginning and this feature continues to be developed.

&nbsp;

**\-** Recognizing that distribution automation was going to become increasingly important, we wanted a testbed upon which to evaluate control algorithms and their impact on the operation of the system.&nbsp;

**\-** Recognizing that it was impossible to satisfy all possible user needs, we wanted a program that would allow users to write their own models or solution procedures commensurate with their capabilities.&nbsp;

**\-** We wanted a program that would simulate the behavior of devices on the distribution system as they would occur for changing load and system faults and other disturbances. This is important for modeling DG interactions, and it also allows the tool to be used for many other things as well, such as energy efficiency analysis.&nbsp;

&nbsp;

The present version of the OpenDSS has achieved most of these goals and has evolved into an extraordinary tool that has acquired many other features not commonly found in other distribution system analysis tools. While DER analysis continues to be one of its key uses, many other types of analysis have been performed with the tool. New features are continually being added to support ongoing research into distribution system planning and analysis at EPRI.

&nbsp;

The OpenDSS is a general-purpose frequency-domain simulation engine that has special features for creating models of electric power distribution systems and performing many types of analyses related to **distribution planning** and **power quality**. It does not perform electromagnetic transients (time domain) simulations; all types of analysis are currently in the frequency domain (i.e., sinusoidal steady state, but not limited to 60 Hz). It does perform electromechanical transients, or dynamics analysis. A recent capability added is the ability to represent geomagnetically-induced currents (GIC).

&nbsp;

Most electrical engineers learned how to write nodal admittance equations in their early University courses, and this is how OpenDSS represents circuits. Each element of the system is represented by a “primitive” nodal admittance (Y) matrix. This is generally straightforward, although it can be tricky for some power system elements such as transformers. Each primitive Y is then coalesced into one large system Y matrix, and the system of equations representing the distribution system is solved using a sparse matrix solver. One trick is that nonlinear behaviors of some devices (e.g., some load models) are modeled by current source injections, which some refer to as “compensation” currents. That is, the current predicted from the linear portion of the model that resides in the system Y matrix is compensated by an external injection to iteratively obtain the correct current. This is a common technique for representing loads in distribution system analysis tools. One advantage of this method is that it allows for quite flexible load models, which is important for performing some types of analysis such as done in energy efficiency studies.

&nbsp;

The program’s heritage is closer to a harmonic flow analysis program, or even a dynamics program, than a typical power flow program. One of the most visible products of this representation is the somewhat “back seat” role buses play in the model. While in most power flow programs, buses are the central element on which everything else is built, buses are dynamically created as needed in OpenDSS. This may seem a strange place to start designing a tool that will be used mostly for power flow studies, but it gives the tool extraordinary modeling flexibility, particularly for accommodating all sorts of load models and unusual circuit configurations. It is easier to make a harmonics flow simulation program solve the power flow problem than the opposite.

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Output with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
