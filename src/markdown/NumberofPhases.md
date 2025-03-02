# Number of Phases

&nbsp;

&nbsp;

***A Question From a User***

&nbsp;

Dear Dr. DSS,

I’m using the DSS and its new line constants calculator in the EPRI NEV Modeling and Simulations Guideline project. I’ve modified some of Tom Short’s R code that autogenerates a DSS file. I’ve got a question concerning the number of phases parameter for lines and transformers. I’m modeling a multigrounded wye system. I have explicitly modeled (and need results from) neutral conductor(s). If I have one neutral conductor is the number of phases still 3, or should it be 4?

*\-Little Rock User*

&nbsp;

*\----------------------*

&nbsp;

The present LINE model calls all conductors "phases". So if you are explicitly modeling neutrals, you declare that a LINE object has 4 "phases" or however many you need. You have to keep track on your own which are actually neutral conductors; the DSS makes no special distinction.

&nbsp;

Now this is where it can get confusing. If you ask for the sequence currents, it considers only the first 3 "phases". If you ask for the sequence voltages, it takes the first 3 nodes defined at a bus. If for some reason you declares something like a grounding resistor to node 4 of a bus before you connect anything else, the first three nodes will likely be 4, 1, 2. This is a potential gotcha. I may change this at some point. Check the detailed node voltages first so that you can see the order assumed by the DSS. While the LINE element calls everything "phases",

LINECODE and LINEGEOMETRY classes can work differently:

&nbsp;

\-LINECODE

&nbsp;

If you specify Kron=yes the LINECODE object will perform a Kron reduction, reducing the order of the defined matrix by one. It reduces the matrix by eliminating the row and column associated with the conductor, if any, designated as a Neutral. (See Neutral property in the Help.) When the LINE object loads a LINECODE object that has been reduced, the number of phases will be one less than the LINECODE was originally defined for. This only works for LINECODE objects defined using matrix properties. "Kron=Yes" is ignored if you define the LINECODE object by symmetrical components (what sense would it make?). The Kron property is an execute-on-setting property. That is, it executes the Kron reduction immediately and then resets the property to NO. Likewise it resets the Neutral property to zero after it executes. The Kron reduction will not do anything until the Neutral property is reset to a legimate value.

&nbsp;

\-LINEGEOMETRY

&nbsp;

The new LINEGEOMETRY class allows you to specify a different number of conductors and number of phases. If you specify "reduce=yes" all conductors over the number of phases are eliminated by Kron reduction. That is, they are assumed to be connected to the zero voltage reference at both ends of the line. So, if you specify 5 conductors and 3 phases, the last two conductors are assumed to be grounded neutrals.

Of course, if you do not reduce the matrix, when the LINE object loads the LINEGEOMETRY object, it will set the number of "phases" for the LINE equal to the number of conductors in the LINEGEOMETRY object.

&nbsp;

Dr. DSS

&nbsp;

\--------------------------

&nbsp;

**A Follow-up Question**

&nbsp;

Dear Dr. DSS,

Thanks for the clarification, even though it makes my head hurt a little. What if I have a transformer and I want to bring back the 1st and 2nd neutral to its neutral terminal? Right now, I have a transformer defined as:

&nbsp;

New Transformer.Sub phases=3 XHL=10 XHT=30 XLT=28

\~ wdg=1 bus=sourcebus conn=delta kVA=100000 kV=138

\~ wdg=2 bus=distbus.1.2.3.4.5 conn=wye kVA=100000 kV=12.5

&nbsp;

In this case, does the DSS assume that the .4 and .5 terminals are solidly grounded? Or does the DSS assume that the .4 is connected to the neutral point of the transformer and .5 is connected to the ground (.0) terminal? I’ve read over the documentation (ver 4.5), and I think the second way is how things are working, but I’m still a bit confused as to how to achieve my objective of connecting two neutrals back to the neutral point of the transformer winding 2…unless I use a very low impedance jumper wire and go back to ‘distbus.1.2.3.4’ on the transformer secondary bus definition.

*\-LRU*

*\---------------------------------*

&nbsp;

Dear LRU,

&nbsp;

No, ".4" and ".5" are simply connection points on a barrier strip. Only ".0" is defined specially. It is equal to the system voltage reference = 0V.

&nbsp;

The 3phase transformer has 4 conductors per terminal. Thus, the ".5" in "bus=distbus.1.2.3.4.5" is ignored. The 3phase LINE with two neutrals does not automatically connect to ".1.2.3.4.5"; It defaults to ".1.2.3.0.0". I think what you want to do is define the 5-conductor LINE as connected to ".1.2.3.4.4"

&nbsp;

No need to add a low impedance separately. Here's something another user did for a 3phase line with lots of neutral conductors on the pole, similar to what you may have:

&nbsp;

New line.A2\_A3 bus1=A2.1.2.3.4.4.4.4.4.4 bus2=A3.1.2.3.4.4.4.4.4.4 LineCode=HC2\_No2\_1neut\_5Mess&nbsp;

\~ length=0.048006

&nbsp;

Here's a double-circuit line with neutrals all connected to 4; phases of the two circuits are .1.2.3 and .5.6.7:

&nbsp;

New line.9\_10 bus1=9.1.2.3.5.6.7.4.4.4.4.4 bus2=10.1.2.3.5.6.7.4.4.4.4.4 LineCode=vcdbl\_1neut\_4mess length=...

&nbsp;

Remember: buses are just barrier strips with places to interconnect conductors from various objects. There is no practical limit to the number of node connection points you can have.

&nbsp;

Dr.DSS


***
_Created with the Standard Edition of HelpNDoc: [Step-by-Step Guide: How to Turn Your Word Document into an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
