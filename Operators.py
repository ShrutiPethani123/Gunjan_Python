"""
1. Arithmetic Operators

+
-
*
/
%
//  -> floor division
** -> Exponant

2. Relational Operator

<
>
<=
>=
==
!=

-> It will return value in boolean

3. Logical Operator

and -> to login when both userid and password must be right

a   b   a and b

F   F   F
F   T   F
T   F   F
T   T   T


or -> signup using google, facbook etc.

a   b   a or b

F   F   F
F   T   T
T   F   T
T   T   T

not -> 

A   not a

T   F
F   T

4. Assignment Operators (shorthand notation)

=
+=
-=
*=
/=
//=
%=
**=

5. Bitwise operator

&
|
^
~
<<
>>

^

a   b   a^b

F   F   F
F   T   T
T   F   T
T   T   F

128    64    32    16    8    4    2    1

12 -> 1100
14 -> 1110
34 -> 0010 0010


1100 -> 12
1111 -> 15
0111 -> 7

12 -> 1 1 0 0
     & & & &
8  -> 1 0 0 0
----------------
      1 0 0 0 (8)


12 -> 1 1 0 0
      | | | |
8  -> 1 0 0 0
----------------
      1 1 0 0 (12)


12 -> 1 1 0 0
      ^ ^ ^ ^
8  -> 1 0 0 0
----------------
      0 1 0 0 (4)

13 ->  01101 
~13 -> 10010 (18) (1's complement)

14 -> 01110
~14 -> 10001 (1's complement)

          1
~14 -> 10001
        +  1
    _________
       10010 (-14)

<< -> left shift operator


15   ->  0000 1111 (15)
15<<1 -> 0001 1110 (30 -> 15 *2^1)
15<<2 -> 0011 1100 (60 -> 15*2^2)


>> -> right shift operator

15    -> 0000 1111
15>>1 -> 0000 0111 ( 7 -> 15//2^1)
15>>2 -> 0000 0011 ( 3 -> 15// 2^2)


6. Membership Operator

    in
    not in

7. Identity operator

    is
    not is
    
"""

a=45
b=6
print("Add: ",a+b)
print("sub: ",a-b)
print("Mul: ",a*b)
print("div: ",a/b)
print("Modulus: ",a%b)
print("floor div: ",a//b)
print("Exponant: ",2**3)

print(a<b)
print(a>=b)
c=45
print(a!=b)


print(a>b and b<c) #T and T
print(a<c or b>a) #F or F
print(not(a<c or b>a))

a=a+2
a+=2


print(12&8)
print(12|8)
print(12^8)
print(~13)
print(13<<2)
print(15>>45)