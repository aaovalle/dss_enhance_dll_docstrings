# FMonitor

&nbsp;

**Source:** MA-OpenDSS Version 1.3 User Manual&nbsp;

[https://www.ece.ucf.edu/~qu/ma-opendss/](<https://www.ece.ucf.edu/~qu/ma-opendss/> "target=\"\_blank\"")

&nbsp;

&nbsp;

Fmonitor is the model of communication in distribution network that follows the OpenFMB design. To enable the cooperative control scheme, a standard and scalable communication structure is implemented as an upper layer design over physical systems in this platform. A standard interface (‘Cluster’ and ‘node’) is established in this structure which can be used to simulate both distributed or centralized communication topology. The buses in power systems can be arranged with clusters and nodes. Within a cluster, each node can communicate to others which DGs might be attached to. By this approach, the communication could be an independent part of the platform. To study the response time of the cooperative control, we improved the dynamic simulation of MA-OpenDSS.&nbsp;

&nbsp;

FMonitor defines the clusters of a distribution system, which the multi-agent distributed control can be implemented upon. The properties of Fmonitor are the following.

&nbsp;

| **Property** | **Description** |
| --- | --- |
| Cluster\_num | The cluster number |
| Element | Name (Full Object name) of element to which is the virtual leader of this cluster. |
| Terminal | Number of the terminal of the circuit element to which the virtual leader is connected. 1 or 2, typically. |
| Nodes | Nodes connected to this FMonitor. Example:(Nodes=33) |
| ElemTableLine | Define each node within this cluster.&nbsp; The first entry of this vector is the number of node within cluster; The second is bus name; The third is the measured element name; The forth is terminal number; The fifth is voltage base; The last the control gain of network level control. . |
| CommVector | Define the communication vector of each node in this FMonitor. The first entry of this vector is the node number. |
| T\_intvl\_smpl | The time period that indicates the information of each agent will be sampled at each node. T\_intvl\_smpl is also the minimal communication time between neighbor nodes. If T\_intvl\_smpl=0.0, no delay for the communication is enabled in the simulation |
| MaxLocalMem | The max number of local memory size of each agent. No larger than 99. |
| b\_Curt\_Ctrl | Set P curtailment on/off; b\_Curt\_Ctrl=True: P curtailment will be implemented according to the system voltage (default); b\_Curt\_Ctrl=False: P curtailment will not be implemented.Set the time delay between agents in this FMonitor. The first entry of this vector is the number of the node. The example show node #2 can communicate to node #1 and #3 with time delay t1 and t2 seperately |
| CommDelayVector | Set the time delay between agents in this FMonitor. The first entry of this vector is the number of the node. The example show node #2 can communicate to node #1 and #3 with time delay t1 and t2 seperately |
| up\_dly | Delay time to upper level. For example: "up\_dly := 0.05" It can be used to simulate the time delay between clusters |
| Volt\_limits\_pu | Define the voltage limits of this cluster, will be used on the network level control.&nbsp; Exmaple "Volt\_limits\_pu={a0,a1, a2}" a0: the phase number, 0 means pos. seq; a1: upper voltage limit of this cluster, usually 1.05; a2: upper voltage limit of this cluster, usually 0.95 |
| EGen&nbsp; | {kVA\_fm, M\_fm, D\_fm, Tau\_fm, Ki\_fm,init\_time} where equations are: (1):delta''=omega (1):M\_fm \* omega''=puPm - puPe - D\_fm\*omega (1):Tau\_fm\*Pm ''=Ki\_fm \* omega&nbsp; puPm = Pm / kVA\_fm, puPe = Pe/ kVAM\_fm; everything is zero within init\_time(default value is 0.5s); k\_dltP is the coordinator for PV control input: u\_i = k\_dltP \* pu\_DltP + omg\_fm. |


&nbsp;

*Examples*

&nbsp;

New "Fmonitor.FM3" Cluster\_num=3 element=Line.LN5956470-1&nbsp; terminal=1&nbsp; Nodes=2 t\_intvl\_smpl=0.0&nbsp; up\_dly=0.0&nbsp; MaxLocalMem =60 Volt\_limits\_pu={the 0,1.05, 0.96}

Fmonitor.FM3.ElemTableLine={1,&nbsp; M1069311,&nbsp; Line.LN5965099-2, &nbsp; 2,&nbsp; 7.2,&nbsp; 1.0}

Fmonitor.FM3.ElemTableLine={2,&nbsp; L3159448,&nbsp; Line.LN5965099-9,&nbsp; &nbsp; 2,&nbsp; 7.2, 1.0}

&nbsp;

Fmonitor.FM3.CommVector={1,1,1}

Fmonitor.FM3.CommVector={2,1,1}

&nbsp;

Fmonitor.FM3.CommDelayVector={1, 0,&nbsp; 0.1}

Fmonitor.FM3.CommDelayVector={2, 0.1,&nbsp; 0&nbsp;

&nbsp;

Plot monitor object= dg\_g2 channels=(31) \!


***
_Created with the Standard Edition of HelpNDoc: [Don't be left in the past: convert your WinHelp HLP help files to CHM with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
