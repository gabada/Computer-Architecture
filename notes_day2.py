#       Boolean Bitwise
# OR         or    |
# AND        and   &
# XOR        N/A   ^
# NOT        not   ~


# and masking
  101010101
& 111100000 <- AND mask
------------
  101000000


  101000000 AND
& 110000000
------------
  100000000
  ^^
   10000000
    1000000
     100000
      10000
       1000
        100
  000000010
         ^^

LEFT SHIFT <<
RIGHT SHIFT >>

ir = 0b10100000 ADD
num_operands = (ir & 0b11000000) >> 6
dist_to_move_pc = num_operands + 1


setting a but to 1:

  00001100
| 01010100
-----------
  

x = x | ( 0b1111 << 3 )

def set_nth_bit(x, n):
    return x | (1 << n)

255.255.255.0 subnet mask
11111111.11111111.11111111.00000000 <- in binary

ip_add AND subnet_mask == network_number
192.168.2.4
255.255.255.0
192.168.2.0