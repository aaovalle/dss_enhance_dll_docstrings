# Transformer model has been modified

&nbsp;

**TechNote Transformer model has been modified**

&nbsp;

***Transformer model***

&nbsp;

The Transformer model has been modified. A Property named "%Rs" has been added that will allow you to enter the %R for each winding as an array. This is to make it more consistent with other properties like kva/kvas, kv/kvs, conn/conns, etc.

&nbsp;

Note you can also specify the %R for the first 2 windings by using the %loadloss property. This is quite convenient for 2winding transformers commonly encountered.

&nbsp;

Equivalent definitions:

&nbsp;

Edit Transformer.T1

\~ Wdg=1 %R=.1

\~ Wdg=2 %R=.1

&nbsp;

Edit Transformer.T1 %Rs=\[0.1 0.1\]

&nbsp;

Edit Transformer.T1 %loadloss=0.2

&nbsp;

Other related issues:

&nbsp;

\-When you specify the kVA rating of Winding 1, all other winding kVAs are set to the same value by default.

\-When you specify the kVA rating either winding of a 2winding transformer, the other winding is set to the same value.

***
_Created with the Standard Edition of HelpNDoc: [Quickly and Easily Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
