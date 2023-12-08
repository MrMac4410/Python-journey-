weight = 10.40
cost_ground = 0
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
  print("Cost to ship your package via ground:$",cost_ground)
elif (weight > 2) and (weight <= 6):
  cost_ground = weight * 3 + 20
  print("Cost to ship your package via ground:$",cost_ground)
elif (weight > 6) and (weight <= 10):
  cost_ground = weight * 4 + 20
  print("Cost to ship your package via ground:$",cost_ground)
else:
  cost_ground = weight * 14.25 + 20
  print("Cost to ship your package via ground:$",cost_ground)

cost_ground_premium = 125.00
print("Premium shipping cost:$", cost_ground_premium)

cost_drone_shipping = 0

if weight <= 2:
  cost_drone_shipping = weight * 4.50
  print("Cost to ship your package via drone shipping:$", cost_drone_shipping)
elif (weight > 2) and (weight <= 6):
  cost_drone_shipping = weight * 9
  print("Cost to ship your package via drone shipping:$", cost_drone_shipping)
elif (weight > 6) and (weight <= 10):
  cost_drone_shipping = weight * 12
  print("Cost to ship your package via drone shipping:$", cost_drone_shipping)
else: 
  cost_drone_shipping = weight * 14.25
  print("Cost to ship your package via drone shipping:$", cost_drone_shipping)
