# LFSR

class LFSR:
    # create an LFSR with initial state ‘seed’ and tap ‘tap’ 
    def __init__(self, seed: str, tap: int): 
        self.seed = seed
        self.tap = tap
        self.xor_num = None
        self.new_num = None

    # return the bit at index ‘-tap’ , from right -> left
    def bit(self): 
        if not self.new_num:
            bit_str = str(self.seed)
        else:
            bit_str = str(self.new_num)
        return bit_str[-self.tap]

    # execute one LFSR iteration and return new (rightmost) bit as an int     
    # you will find the binary XOR operator useful here 
    def step(self):
        # create new number 
        if not self.new_num: # for first time
            front_num = self.seed[0]
            rest_num = self.seed[1:]
        else: # new number exists
            front_num = self.new_num[0]
            rest_num = self.new_num[1:]
        # XOR
        self.xor_num = int(LFSR.bit(self)) ^ int(front_num)
        self.new_num = rest_num + str(self.xor_num)
            
    # return string representation of the LFSR, ex: 01001010 1
    def __str__(self):
        return f'{self.new_num} {self.xor_num}'

def main(numbers: list):
    for pair in numbers:
        seed, tap = pair[0], pair[1]
        obj = LFSR(seed, tap)
        obj.step() # perform step once
        print(obj)

if __name__=='__main__':
    # do something
    numbers = [
        # ('10011010', 5), # sample
        ('0110100111', 2),
        ('0100110010', 8),
        ('1001011101', 5),
        ('0001001100', 1),
        ('1010011101', 7),
    ]
    
    main(numbers)


    # seed = 0110100111, tap = 2 
    # seed = 0100110010, tap = 8 
    # seed = 1001011101, tap = 5 
    # seed = 0001001100, tap = 1 
    # seed = 1010011101, tap = 7 