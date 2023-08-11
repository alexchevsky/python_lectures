# Calculate the ROAS for five different marketing campaigns
print()
print()

exchange_rate = 100

# Campaign 1
clicks1 = 100
cpc1 = 0.50  # Cost Per Click in dollars
revenue1 = 120
cost1 = clicks1 * cpc1
roas1 = revenue1 / cost1
print(f"ROAS for campaign 1: {round(roas1,2)}")

# Campaign 2
clicks2 = 150
cpc2 = 0.60
revenue2 = 200
revenue1_conv = revenue2 * exchange_rate
cost2 = clicks2 * cpc2
roas2 = revenue2 / cost2
print(f"ROAS for campaign 2: {round(roas2,2)}")

# Campaign 3
clicks3 = 90
cpc3 = 0.55
revenue3 = 100
cost3 = clicks3 * cpc3
roas3 = revenue3 / cost3
print(f"ROAS for campaign 3: {round(roas3,2)}")

# Campaign 4
clicks4 = 200
cpc4 = 0.65
revenue4 = 280
cost4 = clicks4 * cpc4
roas4 = revenue4 / cost4
print(f"ROAS for campaign 4: {round(roas4,2)}")

# Campaign 5
clicks5 = 80
cpc5 = 0.52
revenue5 = 95
cost5 = clicks5 * cpc5
roas5 = revenue5 / cost5
print(f"ROAS for campaign 5: {round(roas5,2)}")

print()
print()
