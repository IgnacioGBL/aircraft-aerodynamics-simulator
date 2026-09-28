from calculations import calculate_lift, calculate_weight, calculate_drag, calculate_vstall, calculate_ld_ratio
from aerodynamics import plot_ld_vs_aoa

air_dens = float(input("Enter air density: "))
velocity = float(input("Enter velocity: "))
surface = float(input("Enter surface area: "))
cl = float(input("Enter lift coefficient: "))
cd = float(input("Enter drag coefficient: "))
mass = float(input("Enter mass: "))
cl_max = float(input("Enter maximum lift coefficient: "))
cl_alpha = float(input("Enter lift curve slope (CLα): "))
cd0 = float(input("Enter zero-lift drag coefficient (CD0): "))
k = float(input("Enter induced drag factor (k): "))

lift = calculate_lift(air_dens, velocity, surface, cl)
print("The lift force is:", round(lift, 2), "N")

drag = calculate_drag(air_dens, velocity, surface, cd)
print("The drag force is:", round(drag, 2), "N")

weight = calculate_weight(mass)
print("The weight force is:", round(weight, 2), "N")

vstall = calculate_vstall(air_dens, surface, weight, cl_max)
print("The stall velocity is:", round(vstall, 2), "m/s")

ld_ratio = calculate_ld_ratio(lift, drag)
print("The lift to drag ratio is", round(ld_ratio, 2 ))


if lift > weight:
    print("The aircraft is climbing.")

elif lift < weight:
    print("The aircraft is descending.")

else:
    print ("The aircraft is on a stable flight.")

plot_ld_vs_aoa(cl_alpha, cd0, k)