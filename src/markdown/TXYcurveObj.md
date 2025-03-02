# TXYcurveObj

| ***TXYcurveObj*** |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Type-access*** |  | *Command* | *Description* |  |
| **Implements the following properties/methods as in TLoadShapeObj and TLineObj:** **InitPropertyValues**&nbsp; **DumpProperties** **GetPropertyValue** **Set\_NumPoints** **SaveWrite** **NumPoints** |  |  |  |  |
| **Property-private** | InterpolatePoints |  |  | Returns a point after interpolating the given coordinates. |
| **Property-private** | Get\_YValue |  |  | Get Y Value by index. |
| **Property-private** | Get\_XValue |  |  | Get X Value corresponding to point index. |
| **Method-private** | Set\_XValue |  |  | Sets X Value corresponding to point index. |
| **Method-private** | Set\_YValue |  |  | Sets Y Value corresponding to point index. |
| **Property-private** | Get\_X |  |  | Get X present value. |
| **Property-private** | Get\_Y |  |  | Get Y present value. |
| **Method-private** | Set\_X |  |  | Sets present X value. |
| **Method-private** | Set\_Y |  |  | Sets present Y value. |
| **Property-public** | GetYValue |  |  | Get Y value at specified X Value. |
| **Property-public** | GetXValue |  |  | Get X value at specified Y Value. |
| **Property-public** | GetCoefficients |  |  | This function returns the coefficients of the line interpolated line for the given X (a\*X + b). If no points exist in the curve (or just a single point), the result is (a = 0, b = 0). If Xvalue is outside the range of defined X values, the curve is extrapolated from the Ends (a = 0, b = extrapolated value). |
| **Property-public** | XValue\_pt |  |  | PA Get\_XValue and Set\_XValue. |
| **Property-public** | YValue\_pt |  |  | PA Get\_YValue and Set\_YValue. |
| **Property-public** | X |  |  | PA Get\_X and Set\_X. |
| **Property-public** | Y |  |  | PA Get\_Y and Set\_Y. |



***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
