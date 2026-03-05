dwarf_data = {}

while True:
    info = input().split(" <:> ")
    if "Once upon a time" in info:
        break
    dwarf_name, dwarf_hat_color, dwarf_physics = info
    dwarf_physics = int(dwarf_physics)
    if dwarf_name not in dwarf_data:
        dwarf_data[dwarf_name] = {}

    if dwarf_hat_color not in dwarf_data[dwarf_name]:
        dwarf_data[dwarf_name][dwarf_hat_color] = dwarf_physics
    else:
        if dwarf_physics > dwarf_data[dwarf_name][dwarf_hat_color]:
            dwarf_data[dwarf_name][dwarf_hat_color] = dwarf_physics

        # # If the dwarf exists, compare the current physics with the new physics
        # current_physics = dwarf_data[dwarf_name].get(dwarf_hat_color, 0)
        # dwarf_data[dwarf_name][dwarf_hat_color] = max(current_physics, dwarf_physics)

# Initialize a dictionary to store the counts
color_counts = {}

# Iterate through your stored dwarfs to count the colors
for name, colors in dwarf_data.items():
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

final_dwarfs = []

for name, colors in dwarf_data.items():
    for color, physics in colors.items():
        # Store all info needed for sorting and printing
        final_dwarfs.append({
            'name': name,
            'color': color,
            'physics': physics,
            'count': color_counts[color]
        })

# 1st criteria: physics (descending)
# 2nd criteria: count of hat color (descending)
sorted_dwarfs = sorted(final_dwarfs, key=lambda d: (d['physics'], d['count']), reverse=True)


for dwarf in sorted_dwarfs:
    print(f"({dwarf['color']}) {dwarf['name']} <-> {dwarf['physics']}")