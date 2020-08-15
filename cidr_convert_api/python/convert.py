# These functions need to be implemented
from iptools.ipv4 import netmask2prefix, validate_ip


class CidrMaskConvert:

    def cidr_to_mask(self, val):

        if int(val) <= 0 or int(val) > 32:
            return 'Invalid'
        else:
            mask = [0, 0, 0, 0]
            for i in range(int(val)):
                mask[i//8] = mask[i//8] + (1 << (7 - i % 8))

            return ".".join(map(str, mask))

    def mask_to_cidr(self, val):

        cidr = str(netmask2prefix(val))
        if int(cidr) == 0 or len(val.split('.')) < 4:
            return 'Invalid'
        else:
            return cidr
        #return sum([bin(int(x)).count('1') for x in val.split('.')])

class IpValidate:

    def ipv4_validation(self, val):

        return validate_ip(val)
