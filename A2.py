'''To accept an object mass in kilograms and velocity in meters per second and display its
momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is
its velocity.'''

mass=float(input("Enter the mass of Object(kg):"))
velo=float(input("Enter the velocity of object(m/s):"))

mov=mass*velo*velo
print("Momentum of the object using e=mc2 is :",mov)