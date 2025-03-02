# OpenDSS-X Classes, objects, and hierarchy

The hierarchy tree in OpenDSS is composed by several levels. These levels are derived for feeding the properties and methods used by the circuit elements in OpenDSS. There are 6 groups of elements within OpenDSS-X, these are:

&nbsp;

1. PCE – Power Conversion Elements, these are elements modeled to absorb/deliver energy to the circuit model and are normally connected in shunt (between phases or line to ground – delta/wye), implying that only 1 terminal is enabled for connection to the power system.

&nbsp;

2. &nbsp;PDE – Power delivery Elements, these are elements modeled to transport energy across the circuit model. They have normally 2 terminals but some of them can have more than 2 terminals like in the case of transformers. Normally, these types of elements will be connected in series for interconnecting nodes across the circuit model, however, they can also be connected in shunt like in the case of capacitors and reactors for modeling purposes.

&nbsp;

3. Controls- Control devices are algorithms that emulate control actions affecting PCE and PDE in the same way real controls act in the field. Need to be declared after the PCE/PDE they are linked to, and their actions take place after a successful simulation step.

&nbsp;

4. General-purpose- These elements act as reference libraries that can be used by PCEs and PDEs to inherit configuration, simplifying the amount of code needed for describing a circuit model in OpenDSS-X.

&nbsp;

5. Meters- these objects are created for recording values during the simulation and sometimes, to provide those values to automation built-in OpenDSS. Meters can be assigned to PCE and PDE and have different operational modes.

&nbsp;

6. Containers- These objects are the higher layer in the simulation process, they can contain the whole circuit (PDE, PCE, Meters), implement the solution algorithms and simulation routines, among other high-level operations. These containers are the heart of the simulation and bring together all the other objects around it.

&nbsp;

Depending on their nature, OpenDSS-X objects and classes derive from a different master class. Classes and objects are defined separately, leaving the element class as reference for the element type properties and methods, and the objects are used for creating elements within the circuit and interact with them during the simulation.

***
_Created with the Standard Edition of HelpNDoc: [Full-featured Help generator](<https://www.helpndoc.com/feature-tour>)_
