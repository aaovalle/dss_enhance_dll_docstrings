# Transformer 

&nbsp;

**Transformer Object**

&nbsp;

The Transfomer is implemented as a multi-terminal (two or more) power delivery element.

&nbsp;

A transfomer consists of two or more Windings, connected in somewhat arbitrary fashion (with a default Wye-Delta connection). You can specify the parameters one winding at a time or use arrays to set all the winding values at once. Use the "wdg=…" parameter to select a winding for editing.

&nbsp;

Note that you can define an XfmrCode object to define a Transformer object. This will same some coding in large circuits where many transformers are identical.

&nbsp;

Transformers have one or more phases. The number of conductors per terminal is always one more than the number of phases. For wye- or star-connected windings, the extra conductor is the neutral point. For delta-connected windings, the extra terminal is open internally (you normally leave this connected to node 0).

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Converting Word Documents to eBooks: A Step-by-Step Guide with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
