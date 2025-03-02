# External Mode

This example shows how a “manual” control of the storage dispatch can be accomplished. In this example, the simulation is broken into smaller time periods that are each solved by issuing the *solve* command for a desired number of time steps specified with the global property *number*. The storage state and power are set to desired values in the beginning of each time period.

&nbsp;

...

Solve

&nbsp;

//Charges for the next 5hours with 80% of rated power

//3am 7am

Edit Storage.Storage1 state=charging %charge=80\!settingstatedirectly

Set number=5

Solve

&nbsp;

//Idles for the next 10 hours

//8am 5pm

Edit Storage.Storage1 state=idling

Set number=10

Solve

&nbsp;

//Discharges for the next 5 hours with half of rated power

//6pm 10pm

\!setting state directly through kw(positive means discharging)

Edit Storage.Storage1 kW=25

Set number=5

Solve

&nbsp;

//Idles for the last two hours

//11pm 12am

Edit Storage.Storage1 state=idling

Set number=2

Solve

&nbsp;

Plot Monitor object=MonStorage1State channels=(1234567)

Plot Monitor object=MonStorage1Powers channels=(135)

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp;

&nbsp;

![Image](<lib/NewItem379.png>)

**Figure 12. Powers at Storage Interface**

From 3am to 7am, the element is set to charge with a charging rate of 80%, 40 kW. Both are specified directly through *state* and %*charge* properties. This could also be accomplished by setting *kW* to -40. From 6pm to 10pm, the element is set to discharge with 50 kW through *kW* property. In the other time intervals, the element is set to idling state.


***
_Created with the Standard Edition of HelpNDoc: [Produce online help for Qt applications](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
