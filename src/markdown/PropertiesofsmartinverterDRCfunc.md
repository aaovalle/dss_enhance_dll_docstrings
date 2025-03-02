# Properties of smart inverter DRC function

&nbsp;

The following list shows the properties that should be set when the DRC function is enabled through one of the ensuing two modes: *DYNAMICREACCURR* or *VV\_DRC*.

1. &nbsp;

   1. &nbsp;

      1. &nbsp;
         * *DbvMin*: The per-unit voltage lower limit of the deadband of the DRC function. When the monitored voltage is within this deadband, no reactive power can be provided or absorbed;
         * *DbvMax* : The per-unit voltage upper limit of the deadband of the DRC function. When the monitored voltage is within this deadband, no reactive power can be provided or absorbed;
         * *ArGraLowV* : Ratio between the reactive power provided or absorbed and the difference between the monitored voltage and the average voltage of the averaging window of the DRC function. This rate is applied when the monitored voltage is less than *DbvMin*;
         * *ArGraHiV* : Ratio between the reactive power provided or absorbed and the difference between the monitored voltage and the average voltage of the averaging window of the DRC function. This rate is applied when the monitored voltage is greater than *DbvMax* ;
         * *DynReacavgwindowlen*: The time length of the averaging window of the DRC function.


***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with HelpNDoc's Clean and Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
