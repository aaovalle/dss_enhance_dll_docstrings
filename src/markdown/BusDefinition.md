# Bus Definition

&nbsp;

&nbsp;

A bus is a circuit element having \[1..N\] nodes. Buses are the connection point for all other circuit elements. In many power system analysis programs, “bus” and “node” are nearly synonymous, but they are distinctively different in OpenDSS. Bus is the container of Node objects. That is to say, a Bus has Nodes.

&nbsp;

The main electrical property of a Bus is voltage. Each node has a voltage with respect to the zero voltage reference (remote ground). There is a nodal admittance equation written for every node (i.e., the current is summed at each node). That basically dictates the size of the problem that must be solved, although there is also computational overhead computing the injection, or compensation, currents.

&nbsp;

It is always assumed that node 0 for a bus is the reference/ground/0 V bus. Additional nodes are traditionally the phases for that bus (for example, node 2 is the B phase). When specifying a bus address, any and applicable nodes should be included (except node 0, which is assumed to always be provided). For example, when specifying the three‐phase bus *BUSNAME*, use: BUSNAME.1.2.3

&nbsp;

![Image](<lib/NewItem18.png>)

Figure 1. Bus Definition&nbsp;

&nbsp;

Unlike many power flow programs, there are no special bus types in OpenDSS. All are the same and are simply locations to connect circuit elements together. There is no special load bus or generator bus or slack bus. Just plain buses, similar to most electromagnetic transients (EMT) programs. The function of a bus depends on what is connected to it. This is a liberating concept to the modeler. I could put 30 loads on a bus or put loads and generators on the same bus. While not all configurations one could imagine will easily converge during the power flow iterations, there is no rule that prevents the user from trying.
***
_Created with the Standard Edition of HelpNDoc: [Converting Word Docs to eBooks Made Easy with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
