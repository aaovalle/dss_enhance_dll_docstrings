# Circuit Model Concept

&nbsp;

&nbsp;

The OpenDSS consists of a model of the electrical power distribution system in the rms steady state, overlaid with a communications network that interconnects controls on power delivery elements and on power conversion elements.

![Image](<lib/NewItem10.png>)

&nbsp;

*\[The communications message queues are not completely developed in this version -- one of the control queues is functional and used by the controls that are implemented. Preliminary simulations of packets in a communications network have been performed using separate tools and the scripting capability of OpenDSS. This work continues.\]*&nbsp;

&nbsp;

The OpenDSS consists of a model of the electrical power distribution system in the rms steady state, overlaid with a communications network that interconnects controls on power delivery elements and on power conversion elements. The basic “building blocks” of the circuit model are “Power Delivery” elements (devices like lines, transformers, and capacitors) and “Power Conversion” elements (devices like generators and loads). Support models – such as control, shape, meter, and parameter abstractions – can be created to further refine Power Delivery and Power Conversion models. Further information on all of these models is available in the OpenDSS Manual. From these elements, the bus and nodes necessary to represent the interconnected system are dynamical created; this is a significant paradigm shift over traditional load flow engines which are more bus centered.

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
