##Insert Solid Color 

**PyMel is required for this script to work.**

The selected material has to have a color attribute. 
If the color attribute is connected the script wont change the connection and wont create extra nodes.
Multiple material nodes can be selected. 

By default a gamma correct node will be inserted between the ramp and the material. The default gamma correct value is 0.455 0.455 0.455. These behavours can can be changed in the script on line 5 and 6.  
The default Naming convention is `{name of the selected node}_Color` and `{name of the selected node}_Color_GammaCorrect`. Also can be changed in the script.