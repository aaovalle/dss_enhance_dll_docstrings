# Registers 9 and 10: Overload EEN and UE

&nbsp;

As the Energymeter element sweeps through its zone, it queries each series power delivery element encountered for the kW above Normal and Emergency limits. The value recorded in these two registers is the largest kW amount encountered. In other words, the value is the maximum overload in terms of actual kW.

&nbsp;

Most of the time, this is what you want. However, there are cases where data errors can skew the results. For example, if the data show a 15 kVA transformer serving an apartment building with over 150 kVA load, this will consistently show up as a 135 kVA overload, which might be the largest overload in the problem. However, you would not build a new feeder because a small transformer is overloaded. You would change out the transformer (or correct the data error). Such errors are common in distribution data where it may take a while for transformer changeouts to get properly entered.

&nbsp;

**Excess or Total:** There are two ways these registers can record the results. They can simply record the excess kW over the limits. This is the default behavior. However, they can also record the total kW flowing through the element. The latter method is for cases where it is assumed that the feeder branch in question must be switched off completely if an overload occurs. This reflects a more conservative planning approach.

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
