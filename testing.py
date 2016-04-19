from saxpy import SAX

s = SAX(wordSize = 30, alphabetSize = 4, epsilon = 1e-6)
print(s.scalingFactor)

X1 = [1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]

X2 = [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]

(x1String, x1Indices) = s.to_letter_rep(X1)
print(s.scalingFactor)

(x2String, x2Indices) = s.to_letter_rep(X2)
print(s.scalingFactor)

print(x1String)
print(x2String)



print(s.compare_strings(x1String, x2String))

 
