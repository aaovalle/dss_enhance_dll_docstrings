# Zsc and Loads 

&nbsp;

&nbsp;

&nbsp;

The short circuit matrices reported for each bus are computed from the present system Y matrix. Zsc, Ysc, and Zsc10 (Zsc1 and Zsc0 from the COM interface) are the Thevenin impedances looking into the system Y matrix at the bus of interest, which includes the portion of the load models modeled as an admittance.

&nbsp;

•All injection sources are set to zero.

•The ZscRefresh command will force a new calculation of the short circuit matrices at each bus.

&nbsp;

If the circuit contains load elements, the Zsc and Ysc values may not be as expected if you did not expect loads to be represented in the matrix. The short circuit currents computed will be slightly off from what you might get in another program that ignores load.

&nbsp;

You can eliminate or minimize the contribution of Load elements by:

&nbsp;

&#49;. Setting LoadMult=(a small number). This invalidates all PC elements, forcing a recalculation of the primitive Y matrices and a rebuild of the Y matrix. The contribution of the Load elements will be less.

&#50;. You can simply not define any Loads (comment out the Load file in your Master file, for instance).

&#51;. Make a script that disables all loads. The easiest way to do this is to issue the command: "Show Elements load" which will list all the elements in the Load class. Then use a text editor to insert "disable load." in front of each line in the file. Alternatively, you may make a script of all the loads and set the Enabled property:

&nbsp;

Load.MyLoad.enabled=no \! disable a load so it doesn't affect Zsc

***
_Created with the Standard Edition of HelpNDoc: [5 Reasons Why a Help Authoring Tool is Better than Microsoft Word for Documentation](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
