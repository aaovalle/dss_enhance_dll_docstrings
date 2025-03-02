# Isource 

&nbsp;

Current source. This is a one-terminal current source object that can be connected to any bus. Its most common use is likely to be used to represent harmonic sources and to be used in frequency response scans of circuit models. You can perform positive- or zero-sequence scans. Isource objects can also be controlled through the COM interface or other APIs and controlled to represent many different kinds of circuit element for various studies. A very flexible circuit element.

&nbsp;

Note that if the device you are trying to model produces or consumes power, it is generally better to model it with a Load or Generator object. The power flow algorithm will automatically determine the phase angle of the current source in the Norton equivalent used to represent these devices. This is sometimes difficult to do correctly with an Isource object.

&nbsp;

You can generally attach as many Isource objects to a bus as you want. An Isource object is assumed to be ideal and its Yprim matrix is zero.

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
