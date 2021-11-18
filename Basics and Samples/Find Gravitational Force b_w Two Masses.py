m1=float(input("Enter the first mass: "))
m2=float(input("Enter the second mass: "))
r=float(input("Enter the distance between the centres of the masses: "))
##Distance Between Two Bodies
G=6.673*(10**-11)
##Gravitaion Constant
f=(G*m1*m2)/(r**2)
##F=Gm1m2/r^2
print("Hence, the Gravitational Force is: ",round(f,2),"N")
##N = Newton, SI UNIT OF Force.
