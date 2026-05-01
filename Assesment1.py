
order_value = 50.00
distance = float(input("Please enter the delivery distance in miles: "))


if distance <= 10:
    delivery_fee = 0
elif distance <= 20:
    delivery_fee = 10
elif distance <= 30:
    delivery_fee = 15
else:
    delivery_fee = 20


print(f"\nOrder Value: £{order_value:.2f}")
print(f"Distance: {distance} miles")
print(f"Delivery Fee: £{delivery_fee:.2f}")
