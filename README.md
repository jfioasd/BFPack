# BFpack
A brainfuck compressor slightly better than [CompressedFuck](https://esolangs.org/wiki/CompressedFuck) or [BFZip](https://github.com/robbie01/BFZip/).

It encodes `>` as 2 bits, at the cost of making `,` and `.` 4 bits. This yields better compression rates than the other BF encodings. The encoding is as follows:
|Instruction|Bits|
| :-------: | :-:|
| `>`       | `00` |
| `<`       | `100` |
| `+`       | `110` |
| `[`       | `111` |
| `]`       | `010` |
| `-`       | `011` |
| `.`       | `1010` |
| `,`       | `1011` |
