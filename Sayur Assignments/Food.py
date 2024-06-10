# Displaying Bill Amount for vada,soda & Sandwich .

Vadai=30
Soda=20
Sandwich=100
print("Cost of 1 Vadai is:",Vadai)
print("Cost of 1 Soda is:",Soda)
print("Cost of 1 Sandwich is:",Sandwich)
Quantity_Vadai=float(input("How much vadai bought:"))
Quantity_Soda=float(input("How much Soda bought:"))
Quantity_Sandwich=float(input("How much Sandwich bought:"))
Total=(Vadai*Quantity_Vadai)+(Soda*Quantity_Soda)+(Sandwich*Quantity_Sandwich)
print("The Total Amount is:",Total)
Amount_received=float(input("Amount that Has been received is:"))
Change_amount=Amount_received-Total
print("Collect The Change Amount:",Change_amount)