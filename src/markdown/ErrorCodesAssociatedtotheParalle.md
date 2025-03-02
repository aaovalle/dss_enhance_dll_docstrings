# Error Codes Associated to the Parallel Machine (PM) Operation

&nbsp;

**Error Codes Associated to the Parallel Machine Operation**

&nbsp;

&nbsp;

&nbsp;

| **Code**&nbsp; | **Description**&nbsp; |
| --- | --- |
| &#55;000 | This error is generated when the user is trying to create a new circuit but the number of available CPUs is already assigned to other circuits. To avoid this message, before creating a new circuit check if there are available CPUs by requesting OpenDSS to deliver the number of CPUs and the number of existing Actors. |
| &#55;001 | This error is generated when the user tries to create a new actor but there are no more CPUs available. The number of actors cannot exceed the number of available CPUs on the computer. Check the number of actors (NumActors) and the number of CPUs (NumCPUs) before executing the NewActor Command. |
| &#55;002 | This message is displayed when the user is trying to activate an inexistent actor. To avoid this message, check the number of actors (NumActors) before activating one. The ID of the actor should be less than or equal to NumActors. |
| &#55;003 | This message is displayed when the user is trying to assign a non-existent CPU to the active actor. To avoid this message, check the number of CPUs (Get NumCPUs) before activating one. The CPU ID should be lower to the Number of existing CPUs (starts in CPU 0). |
| &#55;004 | The number of clones requested is not valid, this number cannot be 0 or a negative number. |



***
_Created with the Standard Edition of HelpNDoc: [Streamline Your CHM Help File Creation with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
