#  Kirsty Russell
#  CS 4720
#  Assignment 2
#  Professor Setzer
#  January 31, 2019


import db_access
import db_utility


def main():
    pass

# Chart formatting
space = 18
line_format = ' {:>4}   {:<25}   {:<10}  {:^12}  {:' + str(space + 1) + '} '
divider_line1 = '-' * (84)
divider_line3 = '-' * 82
line_format2 = ' {:^' + str(60 + space) + '} '

# Print Chart
# Print header
print("\n" + divider_line1)
print(divider_line1)
print(line_format.format("ID", "Name", "Num Loc", "Avg Value", "Categories"))
print(divider_line3)


# Print information
for i in db_access.get_all_areas():
    avg = db_utility.get_average_measurements_for_area(i[0])  # Calculate average
    print(line_format.format(str(i[0]), i[1], str(db_utility.number_of_locations_by_area(i[0])),  # areaId, name, num of locations
                             "-----" if avg is None else str(round(avg, 2)),  # avg measurement, round 2 decimals
                             str(", ".join(str(j[1]) for j in db_access.get_categories_for_area(i[0])))))  # categories

