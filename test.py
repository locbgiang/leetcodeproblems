key = 'vpenu'

options = [
    'dtalswbpfm',
    'lcetnapori',
    'erilanutos',
    'aosknrteld',
    'nthydkerls',
]

alpha = 'abcdefghijklmnopqrstuvwxyz'
slide = 'nkuzmeayfjsiqxdtlrpvbotwcg'

def check_slide(mapping):
    for k, opt in zip(key, options):
        if mapping[k] not in opt:
            return False
    return True

for i in range(26):
    L = list(slide)
    for j in range(i):
        x = L.pop(0)
        L.append(x)
    s = "".join(L)
    mapping1 = dict(zip(alpha, s))
    mapping2 = dict(zip(s, alpha))
    res1 = check_slide(mapping1)
    res2 = check_slide(mapping2)
    if res1:
        print("".join(mapping1[k] for k in key))
    if res2:
        print("".join(mapping2[k] for k in key))