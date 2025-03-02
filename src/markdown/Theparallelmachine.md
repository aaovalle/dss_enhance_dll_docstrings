# The parallel machine

\
\
To create the parallel machine, OpenDSS uses the actor model. There are several actor frameworks for Delphi proposed by various authors; however, we already had a framework developed to evaluate Delphi’s tools for this purpose so we chose to use it. Each actor is created by OpenDSS, runs on a separate processor (if possible) using separate threads and has its own assigned core and priority (real-time priority for the process and time critical for the thread).

&nbsp;

The interface for sending and receiving messages from other actors will be the one selected by the user, this is, either the COM interface, the Direct DLL API, or a text script using the EXE version of the program. With this interface, the user will be able to create a new actor (instance), send/receive messages from these actors, and define the execution properties of the actors such as the execution core, simulation mode, and circuit to be solved, among others. This concept is shown in Figure 19.

&nbsp;

Using the existing interfaces, the user can:

&nbsp;

&#49;. Request the number of available cores and the number of physical processors available.

&#50;. Create/Destroy actors

&#51;. Execute the simulation of each circuit concurrently and in parallel (hardware dependent)

&#52;. Assign the core where the actor will be executed

&#53;. Modify the simulation settings for the active actor\
&#54;. Set the name of the circuit that will be simulated

&nbsp;

Basically, the user can do the same things he can do with the classic version plus the operations related with parallel processing.

&nbsp;

![Image](<lib/NewItem137.png>)\
Figure 19. Operational architecture used for OpenDSS

&nbsp;

As can be seen in Figure 19, the interface will work as the communication medium between the different actors on the parallel machine. This feature enables several simulation modes inspired in parallel computations such as temporal, Diakoptics, among others. These type of simulations will be driven by an external program that will handle the actors within the parallel machine, in keeping with the actor concept as a message driven state machine.\
\
To operate the parallel machine, the suggested procedure is as follows:

\
&#49;. The program will create a new default actor every time the start function is called in an OpenDSS COM or DLL interface or when the EXE version is started. OpenDSS will create Actor 1, designate a memory space, open an instance for KLUSolve, and define the execution thread. In return, OpenDSS will return to the user an ID (integer) to identify the created actor.

&nbsp;

&#50;. After the program has started the user issues the NewActor command to create a new actor.

&nbsp;

&#51;. After a new actor is created, the user will designate the core in which the actor is to be executed using the Set Core=nn command. This command will apply to the active actor using the selected interface. Core 0 will be the default core for the initial actor created at start up, but this can be changed.

&nbsp;

&#52;. To change the active actor, the user will issue the Set ActiveActor=nn command.

&nbsp;

&#53;. After the active actor is set, the user can execute OpenDSS commands as done for the classic version using the selected interface. The commands will apply to the process executed by the active actor.

&nbsp;

&#54;. There are two options for solving the systems with actors:

&nbsp;

a. Solve the active actor

&nbsp;

b. Solve all of the actors

&nbsp;

&#55;. If the user selects to solve only the active actor while there are other actors created, the user can continue to interact with the other actors while the solving actor is working. On the other hand, if the user selects to solve all the actors, the ability to exchange information with an actor will depend on the availability of its core. If there are not enough cores to handle the request the user program will have to wait until one of the actors finishes the solution routine.

&nbsp;

&#56;. Each actor can be asked for data and can store its own monitor and energy meter samples locally.

&nbsp;

To make this possible it is necessary to clone essential classes of OpenDSS. This cloning process must be done every time the user requests it. By default, there will be at least 1 actor active for performing simulations and the default core will be Core 0.

&nbsp;

The configuration of each instance (actor) can be made sequentially, however, the parallel processing of each actor circuit is done using multithreading, defining the process and thread affinity and its priority.

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
