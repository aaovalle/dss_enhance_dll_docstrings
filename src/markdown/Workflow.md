# Workflow

&nbsp;

In general, the user will want to:

&nbsp;

&#49;. **Define the circuit** they wish to study by creating new lines, transformers, loads, generators, etc…

\
a. Realistically, the best way to do this is by creating a dss script. More details on scripting are provided in the [Basics of the OpenDSS Scripting Language](<BasicsoftheOpenDSSScriptingLangu.md>) section.

b. Once a script has been written, use the![Image](<lib/NewItem4.png>)button to run the selected script.

&nbsp;

&#50;. **Set up the circuit options**, such as the solution mode (snapshot, daily, harmonic, etc…)

a. This is accomplished through the commands in the Set menu. The most basic form of analysis is the “snapshot” which is analogous to a traditional power flow. For additional information on circuit options, see the [Circuit Model Concept](<CircuitModelConcept.md>).

&nbsp;

&#51;. **Solve** the powerflow problem

a. First, ensure that the bus list is created and the base voltages found by running Do \> Calc Voltage Bases.

b. Then use the ![Image](<lib/NewItem5.png>)button in the toolbar to solve the circuit.

&nbsp;

&#52;. **Perform analysis** on the solved circuit – The specifics of how to accomplish this vary from analysis to analysis, but some general tasks include:

a. Looking at a branch, transformer, load, or other element in the system – To do this, first select the element type and then the element from the element toolbar. Then select the C, V, or P buttons to see a current, voltage, or power visualization. Select the ![Image](<lib/NewItem6.png>)button to edit the element. An example of a voltage visualization for a line is provided in Figure 1.

&nbsp;

![Image](<lib/NewItem7.png>)

Figure 1. Voltage Visualization for a Line Element

&nbsp;

b. Visualize the voltage profile of the system – Type plot profile into the main script window, and press Ctrl‐D to Do that command. A voltage profile will come up showing how the voltage progresses as one progresses down the feeder; an example is provided in Figure 2. Additional parameter can be specified via the plot command; see the [plot ](<Plot.md>)section of this manual.

&nbsp;

![Image](<lib/NewItem8.png>)

Figure 2. Voltage Profile for a Feeder

&nbsp;

c. Visualize data onto a one‐line of the feeder – If you provide bus location data via the buscoords command (see the [plot menu commands](<Plot.md>) section for more information), you can superimpose power flow data onto a map/one‐line of the system. To do this, go Plot \> Circuit Plots \> Circuit Plot. An example is provided in Figure 3. Additional parameter cans be specified via the plot command.

&nbsp;

![Image](<lib/NewItem9.png>)

Figure 3. Lines Losses for a Feeder

&nbsp;

d. Export data for analysis in 3rd party program – All results obtained through OpenDSS can be exported through the various commands in the “Export” menu. Results are .csv files (see the [export](<Export.md>) section for more information)

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly create a professional-quality documentation website with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
