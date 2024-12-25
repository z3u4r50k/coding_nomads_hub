# Use the interpreter to calculate how many seconds are in a year.
# Then write the code in this script file below this line.
#print (60*60*24*365)

seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365

seconds_in_a_year = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year
print (seconds_in_a_year)

"""
# Start the calculation of seconds in a year

# Define time units
SET seconds_per_minute TO 60    # Store 60 and call it "seconds_per_minute" 
SET minutes_per_hour TO 60     # Store 60 and call it "minutes_per_hour"
SET hours_per_day TO 24       # Store 24 and call it "hours_per_day"
SET days_per_year TO 365      # Store 365 and call it "days_per_year"

# Calculate seconds in an hour
SET seconds_per_hour TO seconds_per_minute * minutes_per_hour  # Multiply seconds in a minute by minutes in an hour

# Calculate seconds in a day
SET seconds_per_day TO seconds_per_hour * hours_per_day       # Multiply seconds in an hour by hours in a day

# Calculate total seconds in a year
SET seconds_per_year TO seconds_per_day * days_per_year      # Multiply seconds in a day by days in a year

# Display the result
PRINT "There are" seconds_per_year "seconds in a year."  # Show the answer on the screen

# End the calculation

"""