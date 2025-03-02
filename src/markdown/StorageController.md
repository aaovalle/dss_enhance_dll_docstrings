# StorageController

The StorageController element is designed to control a fleet of Storage elements, which can be as small as composed by a single element, and perform such tasks as dispatching the Storage elements to follow load. For example, it can be difficult to perform load following based on local intelligence only at each Storage element location because the local load may not reflect the load, e.g. at the substation, for example, that needs capacity relief. The StorageController was created to perform such tasks as load following and peakshaving.

The model concept is depicted in Figure 1. The “fleet” may consist of one or more Storage devices.

&nbsp;

![Image](<lib/NewItem407.jpg>)

**Figure 1: StorageController concept**

&nbsp;

Like other controllers in OpenDSS, the user defines a StorageController as monitoring a terminal of one of the current-carrying devices in the circuit. This is usually a Line or Transformer object, but could be any circuit element including a Generator object representing, for example, a solar PV installation with varying power output.

Another key property is *ElementList*. This is a list of Storage-class elements controlled by this controller. If the list is not defined, all Storage elements in the circuit are assumed to be controlled by this controller. You may list the elements as an array of names or you may use the “file=” syntax within the array delimiters:

ElementList = \[MyElement1, MyElement2, MyElement3,...\] ElementList = \[File=*listfile.txt* \]

Where *listfile.txt* is a file containing the names of the Storage elements one to a line. (Only the name of the element should be given; the class name “Storage” is assumed.)

You will get an error message if more than one StorageController attempts to control the same Storage device.

OpenDSS StorageController element has passed through a major update in 2018/2019. This technical note has been elaborated to detail some of the new features, but also to expand the previous StorageController documentation \[[1](<References2.md#\_bookmark37>)\] with a comprehensive description of the model of the controller. The new features are:

* Addition of *I-PeakShave*, *I-PeakShaveLow* and *PeakShaveLow* dispatch modes;
* Possibility to operate simultaneously with InvControl control element controlling the same Storage elements;
* Addition of *DispFactor* property to aid in convergence;
* Possibility to select the regulated measure (power or current) from a specific phase or a combination between different phases of the monitored element through the property *MonPhase*;
* Possibility to specify the deadband as an absolute value. Useful when the desired target value is low. See properties *kWBand* and *kWBandLow*;
* Improved control actions description in Event Log report for better interpretation of operation within each control loop iteration;
* Full compatibility with recently updated Storage element;

***
_Created with the Standard Edition of HelpNDoc: [Converting Word Documents to eBooks: A Step-by-Step Guide with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
