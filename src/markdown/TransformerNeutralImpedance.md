# Transformer Neutral Impedance

&nbsp;

**Transformer Neutral Impedance**

&nbsp;

***Transformer Neutral Impedance Question***

&nbsp;

Question:

&nbsp;

We are trying to test a modified IEEE 4 bus feeder with a grounded resistance on the secondary of a wye connnection. It seems what ever resistance I put in the DSS engine, it doesn't change the results. Is my script ok? Can the DSS engine accept this type of connection? In this case, we have a 4 Ohm resistance.

&nbsp;

Script

&nbsp;

\! 3PHASE STEPDOWN TRANSFORMER 12.47/4.16 KV YY

new transformer.t1 xhl=6

\~ wdg=1 bus=n2 conn=wye kV=12.47 kVA=6000 %r=0.5 Rneut=0

\~ wdg=2 bus=n3 conn=wye kV=4.16 kVA=6000 %r=0.5 Rneut=4

&nbsp;

Answer:

&nbsp;

Yes, the DSS can handle this connection. The above script has a subtle “gotcha” in it that you will need to correct.&nbsp;

&nbsp;

The script defines a 0 impedance neutral on Winding 1 and a 4ohm resistance on the neutral of Winding 2. However, by using the default connection for the Bus=n3 property you have inadvertently shorted the resistance by defining the neutral point as connected to node 0 at bus n3. The default connection for a 3phase device is

&nbsp;

... bus=n3.1.2.3.0.0.0 ... ad infinitum. \</code

&nbsp;

Instead of taking the default, you should explicitly define the bus-to-node connections as bus=n3.1.2.3.99, for example, where 99 is your designation for the neutral point node. It can be any number. If nothing else is connected to n3.99, the neutral point on winding 2 will float, subject to the Rneut and Xneut values. Note that if Rneut=1, the internal neutral impedance is assumed open (X part, too).

&nbsp;

Rneut=1 is the default. I seldom use the Rneut and Xneut properties, but attach a 1-phase Reactor to the neutral point and ground (that is the default connection for the second terminal of a Reactor). That way I can see the current flowing through the neutral impedance. The neutral impedance of the transformer model is "buried" so you can't see the current directly (you can see the neutral voltage). So here's how I might do it, using 99 for the neutral point:

&nbsp;

Revised Script

&nbsp;

\! 3PHASE STEPDOWN TRANSFORMER 12.47/4.16 KV YY

new transformer.t1 xhl=6

\~ wdg=1 bus=n2 conn=wye kV=12.47 kVA=6000 %r=0.5

\~ wdg=2 bus=n3.1.2.3.99 conn=wye kV=4.16 kVA=6000 %r=0.5

new reactor.t1neutral phases=1 bus1=n3.99 R=4 X=0

&nbsp;

Note that it is not necessary in this case to specify the Bus2 property for the Reactor element since it will default to n3.0, which is what we want.

Also, keep in mind that "99" for the neutral designation is totally arbitrary. The other "gotcha" associated with neutral node numbers is accidentally putting two devices with floating wye points in parallel and connecting the neutrals together. You have to use a different number for each neutral at a bus if they are not connected (sometimes they are\!). This most often happens for capacitors at the same bus. See [TechNote OpenDSS Neutral Rules](<NeutralRules.md>)

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
