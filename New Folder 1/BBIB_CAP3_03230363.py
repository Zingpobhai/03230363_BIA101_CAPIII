################################
# Github Repo link:https://github.com/Zingpobhai/03230363_BIA101_CAPIII
# Your Name: Tshechi Norbu
# Your Section : B
# Your Student ID Number: 03230363
################################
# REFERENCES
# https://www.youtube.com/watch?v=OehCy8mnWX4
# SOLUTION
# Your Solution Score: 124323
################################
# Read input file
with open("363.txt", "r") as file:
    lines = file.readlines()

# Initialize total sum
total_sum = 0

# Iterate through each line to calculate the sum
for line in lines:
    # Strip whitespace and newline characters, then extract first two characters
    two_digits = line.strip()[:2]
    
    # Check if the extracted characters are numeric
    if two_digits.isdigit():
        # Convert the two digits to an integer and add to total_sum
        two_digit_number = int(two_digits)
        total_sum += two_digit_number

# Print the total sum
print(total_sum)
