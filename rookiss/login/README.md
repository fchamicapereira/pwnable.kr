- "wrong length" with len(input) > 17
- ignore whitespace and enter

- only accepts input with max 16 bytes (or 12 bytes encoded to base64)
```
n=1 input=A input_len=1 base64=QQ== base64_len=4
n=2 input=AA input_len=2 base64=QUE= base64_len=4
n=3 input=AAA input_len=3 base64=QUFB base64_len=4
n=4 input=AAAA input_len=4 base64=QUFBQQ== base64_len=8
n=5 input=AAAAA input_len=5 base64=QUFBQUE= base64_len=8
n=6 input=AAAAAA input_len=6 base64=QUFBQUFB base64_len=8
n=7 input=AAAAAAA input_len=7 base64=QUFBQUFBQQ== base64_len=12
n=8 input=AAAAAAAA input_len=8 base64=QUFBQUFBQUE= base64_len=12
n=9 input=AAAAAAAAA input_len=9 base64=QUFBQUFBQUFB base64_len=12
n=10 input=AAAAAAAAAA input_len=10 base64=QUFBQUFBQUFBQQ== base64_len=16
n=11 input=AAAAAAAAAAA input_len=11 base64=QUFBQUFBQUFBQUE= base64_len=16
n=12 input=AAAAAAAAAAAA input_len=12 base64=QUFBQUFBQUFBQUFB base64_len=16
```