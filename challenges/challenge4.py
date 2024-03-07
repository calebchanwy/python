import math
# <summary>
# For this task you will have to calculate and return the stamp duty of a property you have purchased.
# Stamp duty is a type of tax applied by the UK goverment when you purchase a property, this tax works in price brackets.
# i.e the same way income tax does.
# Less than £300,000 there is 0% tax.
# £300,001 - £925,000 there is 5% tax.
# £925,001 - £1,500,000 there is 10% tax.
# £1,500,001+ there is 12% tax
# All amounts as each tax bracket is calculated is rounded to the nearest pound
#
# For example if you buy a house worth £1,595,000:
# 0% on the first £300,000 = £0
# 5% on £624,999 (£300,001 -> £925,000) = £31,250
# 10% on £574,999 (£1,500,000 - £925,001) = £57,500
# 12% on the remaining £94,999 (£1,595,000 - £1,500,001) = £11,400
# Total tax = £100,150
# </summary>
# <param name="propertyPrice">The price of the property purchased</param>
# <returns>Total stamp duty</returns>


def StampDuty(propertyPrice):
    
    # The below can be improved by using enums instead of hard-coding
    # However, I was not too sure if I could import enums for the test or not
    # so I refrained from using them, but used local vars instead
    
    FIRST_THRESHOLD = 300001
    SECOND_THRESHOLD = 925001
    THIRD_THRESHOLD = 1500001
    
    # This dictionairy maps minimum thresholds to tax rates
    rates = {
        FIRST_THRESHOLD : 0.05,
        SECOND_THRESHOLD : 0.1,
        THIRD_THRESHOLD : 0.12,
    }
    
    # Property price below any threshold, (0%)
    if propertyPrice <= FIRST_THRESHOLD:
        return 0
    
    startingValueForTax = propertyPrice
    tax = 0

    # Property price at £1,500,000 threshold (12%)
    if startingValueForTax >= THIRD_THRESHOLD:
        tax += (startingValueForTax - THIRD_THRESHOLD)*rates[THIRD_THRESHOLD]
        # Set value at maximum for next calculation
        startingValueForTax = THIRD_THRESHOLD -1

    # Property price at £925,000 threshold (10%)
    if startingValueForTax >= SECOND_THRESHOLD:
        tax += (startingValueForTax - SECOND_THRESHOLD)*rates[SECOND_THRESHOLD]
        # Set value at maximum for next calculation
        startingValueForTax = SECOND_THRESHOLD -1
        
    # Property price at £300,000 threshold (5%)
    if startingValueForTax >= FIRST_THRESHOLD:
        tax += (startingValueForTax - FIRST_THRESHOLD)*rates[FIRST_THRESHOLD]

    # Return final tax rounded nearest integer
    return round(tax, 0)
