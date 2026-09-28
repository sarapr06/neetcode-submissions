class Solution:
    def getSum(self, a: int, b: int) -> int:
        #python integers have arbitrary precision (never overflow naturally) so solving in python could just need a 32 bit mask 0xffffffff to force it to be 32 bit 
        mask = 0xFFFFFFFF
        
        while b!=0:
            #calculate carry and shift left by 1
            #mask to keep to 32b
            carry = ((a&b)<<1) & mask
            #get sum without carry
            #apply mask to keep in 32b
            a=(a^b)&mask
            b=carry
        #if a is negative in 32b, have to format it back to negative
        if a>0x7fffffff:
            return ~(a^mask)
        return a

