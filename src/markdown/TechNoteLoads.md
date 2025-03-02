# TechNote Loads

&nbsp;

&nbsp;

In particular case, loads were initially defined in the traditional type 1 models (constant P, Q). As I increased the loading on the circuit in 1 % increments from 90%, the LTC controls in STATIC control mode started to oscillate at 96% of the peak load specified, which was 114% of what they have actually measured or predicted by some means. Each of the feeders would converge very quickly by themselves without any indication that there was any problem. However, together, they impacted each other to the point where I couldn't achieve control convergence in

the standard power flow mode. The options are:

&nbsp;

&#49;. widen the LTC bandwidth

&#50;. use a different control mode (slower)

&#51;. alter the DSS to only change one tap at a time (might work, might not),

&#52;. try a different load model.

&nbsp;

I started with model 4 just to see what would happen. With this model, P varies linearly with voltage and Q varies quadratically. This load model is patterned after a 1970vintage paper for feeder load characteristics in the Northeast. But this seems to be working much better as the control iterations are dramatically reduced.

&nbsp;

Note that Load Model 4 has since been modified to accommodate Conservation Voltage Reduction (CVR) models.

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
