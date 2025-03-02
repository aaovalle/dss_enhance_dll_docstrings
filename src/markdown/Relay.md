# Relay

&nbsp;

This relay mode of operation is intended for applications where not only current magnitudes determine operation and trip times but also the angle determines the region of operation or whether the relay operates at all.

&nbsp;

It has been originally implemented to mimic features of microprocessor network protector relays for reverse power flow. It includes network protector functionalities as described in the IEEE standard C57.12.44-2014 \[1\]. These applications should allow for reverse power flow under certain operating scenarios and trip for reverse fault conditions while forward current flow operation is restrained. Nevertheless, this relay mode can also be used to model DOC protection applications where, for instance, the backward current flow direction is restrained and the relay is supposed to trip and protect a faulted line only in the forward direction.

&nbsp;

The modes of operation include a sensitive reverse flow mode intended to trip for any reverse flow condition where reverse resistive currents exceed a given pickup threshold, regardless of reactive current components. The sensitive region of operation can also be defined by a threshold line tilted around user-defined resistive current values by user-defined angles. The relay model also includes regions of operation defined by current magnitudes. The combination of regions of operation can be used to allow reverse flow for defined time intervals or indefinitely as long as the current stays in defined regions. Trip times can also be defined by inverse Time-Current Curve (TCC) curves. Operation region options can be combined depending on the application.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily create iPhone documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
