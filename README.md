# Porter-Duff-Operators
implementation of the concepts employed by the porter duff operators for use on images within green screen areas

## Usage:
<pre>
porter-duff.py -t imagefile -s imagefile -tm mask -sm mask -m mode
    -t : Target Image (I1)
    -s : Secondary Image (I2)
    -z : Target Mask
    -x : Secondary Mask
    -m : mode (1 = clear | 2 = copy | 3 = over | 4 = in | 5 = out | 6 = atop | 7 = xor | 8 = display images | 9 = all)
    -b : apply operator in both directions (0/1)
            </pre>
