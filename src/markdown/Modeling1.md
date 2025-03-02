# Modeling

&nbsp;

The Storage element is a [Power Conversion Element](<OpenDSSDocumentation.md#\_bookmark0>) ([PCE](<OpenDSSDocumentation.md#\_bookmark0>)), which, at a high level, is modeled as a constant power load during charging and as a generator that can inject power into the grid during discharging, always subjected to its power rating and it stored energy capacity. The general model is illustrated in [Figure 1](<OpenDSSDocumentation.md#\_bookmark1>).

![Image](<lib/NewItem348.png>)

**Figure 1. General model of the Storage Element**

&nbsp;

The different components of the model are as follows:

* Ideal Storage: represents an ideal, lossless energy storage. Its [State of Charge](<OpenDSSDocumentation.md#\_bookmark0>) ([SOC](<OpenDSSDocumentation.md#\_bookmark0>)) varies according to the evolution of the element state among charging, discharging and idling along with the associated charging and discharging rates and losses.
* Charging and Discharging Losses: represent the charging and discharging losses associated with the conversion from the storage medium (e.g., battery) to electric energy and vice versa. The model allows to specify separate efficiencies for charging and discharging.
* Inverter: is a key new feature of the new Storage model, which works similarly to the inverter within PVSystem element as a built-in equipment in the model. It allows dispatching reactive power based on several functions, modeling the inverter losses, and limiting the rate of charge and discharge based on its ratings. Note that it is different than the InvControl control element which is responsible for providing smart inverter functionality (see \[[3](<OpenDSSDocumentation.md#\_bookmark36>)\]);
* State: represents the state in which Storage element operates. The three possible states are: charging, discharging, and idling.

&nbsp;

* Idling Losses: represent storage self-depletion losses and auxiliary loads (e.g., A/C, control, and communication equipment, etc.), which are supplied by the same inverter as the energy storage medium/battery. When in a discharging state, the self-depletion losses and auxiliary loads are supplied by the ideal storage, increasing the power that discharges the element. When in charging state, they are supplied by the inverter and act to slow the charging of the ideal storage. In idling state, they are supplied by the grid through the inverter. Note that AC auxiliary loads, which are not supplied by the same inverter as the storage medium/battery, can be modeled by a load object connected in parallel to the Storage element.


***
_Created with the Standard Edition of HelpNDoc: [Add an Extra Layer of Security to Your PDFs with Encryption](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
