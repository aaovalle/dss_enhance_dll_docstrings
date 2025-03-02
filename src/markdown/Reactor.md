# Reactor

&nbsp;

**Reactor Object**

&nbsp;

The Reactor element is an extremely flexible and powerful circuit element. The Reactor element is implemented with basically the same philosophy as a Capacitor (and a Fault object). It is a constant impedance element that may be configured into a variety of connections. Like the Capacitor, the second terminal defaults to a Wye connection to ground if not specified. In that case, it is flagged as a Shunt element. It is a constant impedance element entirely represented by its primitive Y matrix.

&nbsp;

A Reactor object can have frequency-dependent R and L by supplying an appropriate per-unit XYCurve object. You can put a Reactor in series with another circuit element to give the element frequency dependence. This might be common for a Transformer for harmonics studies. If a Line object is defined by a LineGeometry object, frequency-dependence is often automatic. However, if defined by a LineCode object you can use a Reactor element, appropriately defined, to impart frequency dependence.

&nbsp;

The reactor may be conceived as a series R-L or a parallel R-L connection (see Parallel property). By default it is an inductance with series resistance. You may also specify a resistor, Rp, in parallel with the entire branch. These options allow the Reactor impedance characteristic to have different frequency response characteristics, which are often useful for some Harmonics-mode simulations, particularly for filters. In the case of a shunt reactor, the Rp value is used for no-load losses.

&nbsp;

Zero-impedance devices cannot exist in OpenDSS. However, either R or X can be zero in this model, but not both. A Reactor element can be used for source equivalent or other equivalent impedances where the capacitance of a Line element is unnecessary. Use a 1-phase reactor to model neutral reactors in transformers, generators, or loads.

&nbsp;

By default, the Reactor has no coupling between the phases. Shunt reactors would typically be defined by kV and kvar properties, similar to a capacitor. Series reactors without mutual coupling would be defined by the R and X properties. Of course, either could be used in all circumstances.

&nbsp;

You can use Reactor objects to represent lines and switches. However, keep in mind that you do not get any shunt capacitance as a Line element would naturally give. Thus, it is easier to accidentally create isolated islands with no conductive path to ground. This will result in Y matrices that will not invert and you will get floating-point errors.

&nbsp;

Note that if the connection is specified as “delta” only the first terminal matters; there is no second terminal. This applies only to shunt reactors. By leaving the Conn property as wye and specifying both terminal connections explicitly, nearly any reactor configuration can be achieved. Mutual coupling between phases can be achieved by specifying Rmatrix and Xmatrix properties. Note that the matrix specification is mutually exclusive with the other means of specifying the reactance values. Of course, the Rmatrix and Xmatrix properties may be defined with zero mutual coupling. The Parallel property applies to the Rmatrix and Xmatrix specification.

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
