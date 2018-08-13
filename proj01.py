##################################
# Computer project #1
#
# Arithmetic
#    prompt user for integer
#    input an integer
#    define input as floating integer
#    reprint floating integer
#    print floating integer converted to meters, feet, miles, furlongs, and\
#    minutes per floating integer
##################################

# Prompts user to input integer and specifies input as a floating integer.
num_str1 = input("Input rods: ")
rod_float = float(num_str1)

# Reprints floating integer and prints a blank line.
print("You input",rod_float,"rods.\n")

# Prints "Conversions" and converts floating integer to meters, feet, miles,\
# furlongs, and minutes to walk the input. Rounds conversions to 3 places.
print("Conversions")
meters = rod_float*5.0292
print("Meters:",round(meters,3))
feet = rod_float*5.0292/0.3048
print("Feet:",round(feet,3))
miles = rod_float*5.0292/1609.34
print("Miles:",round(miles,3))
furlongs = rod_float/40
print("Furlongs:",round(furlongs,3))
walk_time = 301.752*rod_float/4988.954
print("Minutes to walk",rod_float,"rods:",round(walk_time,3))