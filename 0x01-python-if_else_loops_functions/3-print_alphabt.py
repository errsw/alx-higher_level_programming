#!/usr/bin/python3
print(''.join(['{:c}'.format(i) for i in range(ord('a'), ord('z') + 1) if chr(i) != 'e' and chr(i) != 'q']), end='')
