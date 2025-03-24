import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of the email report file
with open(email_file, 'r') as file:
    email = file.read()

# regular expression pattern to match amounts in various formats (e.g., $45.99, €30, etc.)
# This pattern matches a currency symbol followed by an amount, which may have decimals.
pattern = r'[\$€£]\s?\d+\.\d{2}|\d+'

# extract numbers from email using the regex pattern
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
    # Remove any currency symbols and convert the string to a float
    if amount.startswith('$') or amount.startswith('€') or amount.startswith('£'):
        value = float(amount[1:].strip())  # Remove the currency symbol and convert to float
    else:
        value = float(amount.strip())  # Handle plain numbers without symbols

    total += value