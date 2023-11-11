print("yusuf & sons")
p = float(input("Enter principal:"))
T = float(input("Enter time:"))
R = float(input("Enter rate:"))
Simple_interest = (p * R * T) / 100
Compound_interest = (p * (1 + R / 100) ** (T - 1))
print('Simple_interest is %f' %(Simple_interest))
print('Compound_interest is %f' %(Compound_interest))
print("simple_interest has been calculated")
print("compound interest has been calculated")








