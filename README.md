# BFPack
A brainfuck compressor slightly better than [CompressedFuck](https://esolangs.org/wiki/CompressedFuck) or [BFZip](https://esolangs.org/wiki/CompressedFuck).

It encodes `>` as 2 bits, at the cost of making `,` and `.` 4 bits. The encoding is as follows:
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
