#saxpy.py

An implementation of Symbolic Aggregate approXimation in python.

Based on the paper A Symbolic Representation of Time Series, with Implications for Streaming Algorithms

************
*General use:*
--------------
```
from saxpy import SAX

s = SAX(wordSize, alphabetSize, epsilon)
```
You can optionally specify word size, alphabet size and epsilon

If you want to compare x1 and x2 (lists of values):

```
(x1String, x1Indices) = s.to_letter_rep(x1)
(x2String, x2Indices) = s.to_letter_rep(x2)

x1x2ComparisonScore = s.compare_strings(x1String, x2String)
```

If you want to use the sliding window functionality:

(say you want to break x3 into a lot of subsequences)

can optionally specify the number of subsequences and how much each subsequence
overlaps with the previous subsequence
```
(x3Strings, x3Indices) = s.sliding_window(x3, numSubsequences, overlappingFraction)
```

Then if you wanted to compare each subsequence to another string (say x2):

```
x3x2ComparisonScores = s.batch_compare(x3,x2)
```

*****
*Note:*

If you haven't generated the strings through the same SAX object, the scaling
factor (square root of the length of the input vector over the word size) will be
incorrect, you can correct it using:

```
s.set_scaling_factor(scalingFactor)
```

*****
To run the tests, just do:

```
nosetests ./tests/
```