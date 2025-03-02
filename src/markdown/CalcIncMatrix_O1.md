# CalcIncMatrix_O

&nbsp;

&nbsp;

This command can be used to calculate the Branch-To-Node incidence matrix (B2N) of the active circuit. However, this command delivers and optimized matrix that is organized inside the algorithm by using the CktTree class. The calculation is performed considering the PDElements as branches (rows) and the buses as nodes (Columns). Additionally, this algorithm calculates the levels of each bus to populate an internal array called BusLevels. The Bus level is an integer that reveals how far in terms of buses is the Bus respect to the feeder’s backbone. The Backbone is a randomly selected continuous path from the feeder head to a point in the feeder selected as feeder end.

***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
