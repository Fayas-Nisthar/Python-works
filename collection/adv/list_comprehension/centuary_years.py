years=[y for y in range(1800,2025)]
centuary=[c for c in years if c%100==0]
print(centuary)


leap_years=[l for l in years if (l%100==0 and l%400==0) or (l%100!=0 and l%4==0)]
print(leap_years)