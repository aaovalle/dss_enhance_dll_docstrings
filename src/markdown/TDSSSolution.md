# TDSSSolution

| ***TDSSSolution*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Method-protected** | DefineProperties | See 3.3.2. |
| **Property-protected** | Edit | See 3.2.2. |
| **Method-protected** | Init | See 3.2.2. |
| **Method-public** | NewObject | See 3.1.4. |


&nbsp;

The TDSSSolution class implements an additional class derived from TThread for allowing OpenDSS-X to use parallel processing. This is called TSolver, which implements the calls to the solution algorithms on a separate thread. TSolver is implemented as an actor, allowing the TDSSSolution and TDSSSolutionObj to send messages to TSolver commanding actions. The messages received are enqueued, guaranteeing that if several callers send commands to the actor “concurrently”, these will be executed by TSolver.&nbsp;

The messages of TSolver are handled through events. TSolver keeps waiting indefinitely until a new message arrives. Every time a new circuit is created, OpenDSS-X will create an actor (instance) of TSolver, this actor will have affinity to all the processor’s threads and real-time priority (MS Windows). TSolver gets destroyed after a “Clear” (for the active actor) or “ClearAll” (for all actors). OpenDSS-X is executed in a separate thread than all the other TSolver instances, facilitating communication between them and avoiding unnecessary queues. The job progress and status of the actors can be verified by TDSSSolutionObj using the global variables for such purpose (DSSGlobals.dss).

![Chart, box and whisker chart

Description automatically generated](<lib/NewItem597.png>)

**Figure 1. Containers object inheritance tree**

***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
