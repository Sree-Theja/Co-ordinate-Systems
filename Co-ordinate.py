#co-ordinate system conversions
import math as mp
print("Select co-ordinate system to convert from:")
print("1-Cartesian")
print("2-Cylindrical")
print("3-Spherical")
a=int(input("Enter the choice:"))
print("Select co-ordinate system to convert to:")
if a==1:
    print("5-Cylindrical")
    print("6-Spherical")
if a==2:
    print("4-Cartesian")
    print("6-Spherical")
if a==3:
    print("5-Cylindrical")
    print("4-Cartesian")    
b=int(input("Enter the choice:"))
if a==1 and b==5:
    def cylin(x,y,z):
        r=mp.sqrt((x**2)+(y**2))
        tantheetha=(y/x)
        theetha=mp.atan(tantheetha)
        z=z
        return r,theetha,z
    
    x=float(input("Enter x value:"))
    y=float(input("Enter y value:"))
    z=float(input("Enter z value:"))
    output=cylin(x,y,z)
    print("The cylindrical values are",output)
if a==1 and b==6:
    def spherical(x,y,z):
        theetha=theetha*mp.pi/180.0
        r=mp.sqrt((x**2)+(y**2)+(z**2))
        tantheetha=(y/x)
        theetha=(mp.atan(tantheetha))
        cosphi=(z/r)
        phi=mp.degrees(mp.acos(cosphi))
        return r,theetha,phi
    
    x=float(input("Enter x value:"))
    y=float(input("Enter y value:"))
    z=float(input("Enter z value:"))
    output=spherical(x,y,z)
    print("The spherical values are",output)
if a==2 and b==4:
     def cart(r,theetha,z):
        theetha = theetha * mp.pi/180.0
        x=r*(mp.cos(theetha))
        y=r*(mp.sin(theetha))
        z=z
        return x,y,z
 
     r=float(input("Enter r value:"))
     theetha=float(input("Enter theeta value in degrees:"))
     z=int(input("Enter z value:"))
     output=cart(r,theetha,z)
     print("The cartesian values are",output)
if a==2 and b==6:
    def spherical(r,theetha,z):
        p=mp.sqrt((r**2)+(z**2))
        theetha=theetha
        cosphi=z/p
        phi=mp.degrees(mp.acos(cosphi))
        return p,theetha,phi

    r=float(input("Enter value of r:"))
    theetha=float(input("Enter value of theetha in degrees:"))
    z=float(input("Enter value of z:"))
    output=spherical(r,theetha,z)
    print("The sperical values are:",output)
if a==3 and b==5:
    def cylin(p,theetha,phi):
        phi=phi*mp.pi/180.0
        r=p*(mp.sin(phi))
        theetha=theetha
        z=p*(mp.cos(phi))
        return r,theetha,z

    p=float(input("Enter value of p:"))
    theetha=float(input("Enter value of theetha in degrees:"))
    phi=float(input("Enter value of phi in degrees:"))
    output=cylin(p,theetha,phi)
    print("The cylindrical values are:",output)
if a==3 and b==4:
    def cart(p,theetha,phi):
        theetha = theetha * mp.pi/180.0
        phi=phi*mp.pi/180.0
        x=p*(mp.sin(phi))*(mp.cos(theetha))
        y=p*(mp.sin(phi))*(mp.sin(theetha))
        z=p*(mp.cos(phi))
        return x,y,z
 
    p=float(input("Enter p value:"))
    theetha=float(input("Enter theeta value in degrees:"))
    phi=float(input("Enter phi value in degrees:"))
    output=cart(p,theetha,phi)
    print("The cartesian values are",output)