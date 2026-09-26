# Test Cases in test_validator.py

## Accepted
- GG-CS-25-ABC-R01-A
- GG-IS-29-0123C-R20-B
- GG-IT-26-9999-R10-C

## Rejects

### YR Below 25
- GG-CS-24-ABC-R01-A
### YR Above 29
- GG-CS-30-ABC-R01-A
### ID Too Short
- GG-CS-25-AB-R01-A
### ID Too Long
- GG-CS-25-ABC123-R01-A
### Invalid R Number
- GG-CS-25-ABC-R00-A
### Invalid Final Letter
- GG-CS-25-ABC-R01-D
### Missing Hyphen
- GGCS-25-ABC-R01-A
### Double Hyphen
- GG--CS-25-ABC-R01-A
### Spaces in Code
- GG- CS-25-ABC-R01-A

## Invalid Alphabet 

### Lower Case Symbols
- gg-CS-25-ABC-R01-A
### Punctuation Symbol
- GG-CS-25-ABC-R01-!

## Multiple Input
- GG-CS-25-ABC-R01-A , *Accept*
- GG-IS-29-0123C-R20-B , *Accept*
- GG-CS-24-ABC-R01-A , *Reject*
- GG-CS-25-AB-R01-A , *Reject*

#### Result: Ran 16 tests, all successful.
		