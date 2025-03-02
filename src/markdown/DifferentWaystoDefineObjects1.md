# Different Ways to Define Objects 

\
\
**Question:** Looking thru the documentation and the data sets, I see (what looks to me) as different variations of data input (scalar or arrays). Is this true throughout the program?\
&nbsp;

***Example:***

&nbsp;

new transformer.reg1a phases=3 windings=2 buses=\[150 150r\] conns=\[wye wye\]

\~ kvs=\[4.16 4.16\] kvas=\[5000 5000\] XHL=.001 %LoadLoss=0.00001 ppm=0.0

&nbsp;

New Transformer.XFM1 Phases=3 Windings=2 Xhl=2.72

\~ wdg=1 bus=61s conn=Delta kv=4.16 kva=150 %r=0.635

\~ wdg=2 bus=610 conn=Delta kv=0.48 kva=150 %r=0.635

&nbsp;

**Answer:**

&nbsp;

While we've made an effort to maintain some uniformity in the way various elements are defined, there is nothing in the program that requires it. The DSS executive parses the "New Transformer.Myname" and once it determines which class is being addressed (in this case, Transformer) it passes everything else to the property editor of the Transformer class. It is the responsibility of that class to process the definitions of the properties. So the different classes can have different ways to define properties.

&nbsp;

Another object class that uses both scalars and arrays is the Capacitor. While most of the time you can get by with a scalar definition, the Capacitor is really a multistep filter bank and you can expressly define each step using arrays.

&nbsp;

The Transformer object is one of the more complex in terms of defining properties. We started off years ago with the second form above, but soon tired of typing all those lines. Then we implemented the array form of entering buses and ratings. However, some prefer the second form because it is often more readable.

&nbsp;

Another reason we allow arrays for the Transformer class is there is no limit on the number of windings you can define. The biggest one we have done had more than a dozen windings. Of course, you have to know how to compute the short circuit matrices for such models.

&nbsp;

Note you can also specify %r for a 2winding transformer by setting %loadloss= .... This sets the %r for the first 2 windings, which are assumed to be the main loadbearing windings. (This is not always true and may require some fixup to the script for some 3winding transformers.)

&nbsp;

Many DSS classes have multiple ways to define the properties. This allows us to get closer to the original form of the data source and minimize the conversion effort (which, unfortunately is never zero).

&nbsp;

We add properties (keywords) to classes with some regularity to improve data conversion. The Green Circuits project and other things we are working on has prompted several additions since OpenDSS was released Sept 2008. The DSS is perhaps unique in its software design to permit this with greater ease than other tools. If you look at the Edit function in any of the classes, you will see that to handle a new property, we simply have to added a new item to the CASE statement and, of course, the new property name and help string.

&nbsp;

We recently turned the Vsource into a 2terminal voltage source by adding one property (Bus2) and the code to handle it. (That is not in the November 2008 release, but if you have the ability to build from the code, you have access to it because the code on SourceForge.Net is up to date.)

***
_Created with the Standard Edition of HelpNDoc: [Achieve Professional Documentation Results with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
