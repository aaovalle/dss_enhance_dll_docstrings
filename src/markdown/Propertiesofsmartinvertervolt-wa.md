# Properties of smart inverter volt-watt function

&nbsp;

The following list shows the properties that should be set when the volt-watt function is enabled through one of the ensuing two modes: *VOLTWATT* or *VV\_VW*.

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *voltwatt\_curve*: Name of the XYCurve object containing the volt-watt curve;
         * *VoltwattYAxis*: Defines the *y* axis in *pu* of the volt-watt curve. The options for this property are listed below:

           * *PMPPPU* : The *y* axis corresponds to the value in *pu* of *Pmpp* property of the PVSystem;
           * *PAVAILABLEPU* : The *y* axis corresponds to the value in *pu* of the available active power of the PVSystem;
           * *PCTPMPPPU* : The *y* axis corresponds to the value in *pu* of the power *Pmpp* multiplied 1/100 of the *%Pmpp* property of the PVSystem;
           * *KVARATINGPU* : The *y* axis corresponds to the value in *pu* of the *kVA* property of the PVSystem.

***
_Created with the Standard Edition of HelpNDoc: [Full-featured EPub generator](<https://www.helpndoc.com/create-epub-ebooks>)_
