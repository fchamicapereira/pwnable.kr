- passcode of 20bytes
- sum of these bytes must be == 0x21DD09EC

```
python -c "print '\xc8\xce\xc5\x06'*4+'\xcc\xce\xc5\x06'" | ./col
```