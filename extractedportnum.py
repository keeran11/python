import re

# Input string containing the text with port numbers
input_text = """
During my junior year in college, I decided to learn Django development on my own, which later sparked my interest in information security
 (infosec) and cybersecurity.

"""

# Use a regular expression to find all numbers in the text
port_numbers = re.findall(r'\b\d{2,5}\b', input_text)

# Join the port numbers with a comma and print the result
output = ",".join(port_numbers)
print(output)
