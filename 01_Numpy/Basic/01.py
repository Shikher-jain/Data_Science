import numpy as np

d1 = [1,2,3]

d2 = [
        [1,2,3],
        [4,5,6]
    ]

d3 = [
        [
            [11,21,31],[41,51,61],[71,81,91]
        ],
        [
            [12,22,32],[42,52,62],[72,82,92]
        ],
        [
            [13,23,33],[43,53,63],[73,83,93]
        ]
    ]

print(np.array(d1))
print(np.array(d2))
print(np.array(d3))

print(type(np.array(d1)))
print(type(np.array(d2)))
print(type(np.array(d3)))

print(np.array(d1, dtype=np.int32))
print(np.array(d2, dtype=np.float64))
print(np.array(d3, dtype=np.str_))