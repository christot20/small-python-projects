Name = ["Juan", "Rae", "Ivanna", "Lilly", "Robert"]
Wage = {"Juan":7.50, "Rae":11.00, "Ivanna":18.25, "Lilly":9.25, "Robert":11.10}
Hours = {"Juan":35, "Rae":41, "Ivanna":26, "Lilly":35, "Robert":45}
for y in Name:
    GrossPay = 0
    while Hours[y] > 40:
        GrossPay = (35 * Wage[y]) + ((Hours[y]-35)*Wage[y]*1.5)
        break
    while Hours[y] <= 40:
        GrossPay = (Hours[y] * Wage[y])
        break
    print ('{:<5s} {:<10s} {:<5s} {:<10f} {:<5s} {:<10d} {:<5s} {:<10f}'.format("Name:", y, "Wage:",  Wage[y],  "Hours:", Hours[y], "Gross pay:",  GrossPay))