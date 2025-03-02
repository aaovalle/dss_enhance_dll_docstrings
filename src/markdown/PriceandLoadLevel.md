# Price and LoadLevel

In these two modes, the charging and discharging triggers are also utilized, however they are compared to global properties, which can be used, for instance, to model the effect of a control center responsible for managing multiple energy storage elements.

Price mode uses, instead of a loadshape object, a PriceShape object, which represents of an array of prices. The PriceShape object is assigned to the pricecurve global property. The triggers are defined as prices and the rule is that whenever the energy price assigned to *ChargeTrigger* is greater than the price from the global PriceShape, the storage is set to charging state. In other words, the *ChargeTrigger* represents the maximum energy price the storage owner is willing to pay to charge the storage. The storage charging is naturally limited by the storage energy capacity. The *DischargeTrigger* works in an opposite way representing the minimum price that the storage owner is willing to accept to sell energy to the grid. So the element is set to discharging state whenever the price assigned is less than the global energy price. The global property *pricesignal* can also be used to manually set the price of energy during the simulation, which can be useful when, e.g., the prices are determined by an external algorithm. When manually setting the *pricesignal* property, the pricecurve should not be defined as otherwise, it would be used.

The same logic applies to Loadlevel dispatch mode. In this mode, the global loadshape is defined through a loadshape object that must be assigned to either *defaultdaily* or *defaultyearly* global properties, depending on the solution mode being considered.

The commands used for defining the aforementioned properties are illustrated below.

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp;

New PriceShape.Priceinterval=1 npts=24

\~ price=\[75,68,67,69,71,75,75,80,80,80,90,90,90,95,95,95,105,105,110,110,110,90,90,90\]

&nbsp;

//Assigning a global price curve to the simulation Set pricecurve=&nbsp; &nbsp; Price

&nbsp;

//Assigning a specific global price

Set pricesignal=100 \!use this when you desire to

\!manually assign a global price

&nbsp;

//Assigningagloballoadshapetothesimulation

Set defaultdaily="MyDailyLoadShapeName" \!this will be considered in

\!adailymodesimulation

Set defaultyearly="MyYearlyLoadShapeName" \!this will be considered in

\!ayearlymodesimulation

&nbsp;

\!Optional

Set loadmult=pernunitvalue&nbsp; &nbsp; \!loadmult global property also applies

\!to loadshapes assigned to default daily and default yearly

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Produce Kindle eBooks easily](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
