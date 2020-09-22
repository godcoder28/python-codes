# Write A programme to print commission of a person depending on the sale?
# Date. 29/04/19
# MADE BY: Shivang Gupta

"""Sale              commisiion
    <10,000              5%
    >10,000;<20,000     10%
    >20,000;<50,000     20%
    >50,000             25%

"""
cmsn = int(0)
# Date. 29/04/2019
sale = int(input("Enter The Sales:"))
if sale < 10000:
    cmsn = 0.05 * sale

elif sale < 20000:
    cmsn = 0.1 * sale

elif sale < 50000:
    cmsn = 0.2 * sale

else:
    cmsn = 0.25 * sale

print("The commission is:", cmsn)
