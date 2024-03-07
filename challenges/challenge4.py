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


# Helper method that returns total tax based on a given minimum threshold and rate
# <param name="THRESHOLD">The minimum threshold that tax applies</param>
# <param name="value">The current property value</param>
# <param name="rate">Rate that the tax should be applied at</param>
# <returns>Tax amount of value, based on a given minimum threshold and rate</returns>
def TaxAtThreshold(THRESHOLD, value, rate):
    return (value - THRESHOLD) * rate

def StampDuty(propertyPrice):
    
    # The below can be improved by using enums instead of hard-coding
    # However, I was not too sure if I could import enums for the test or not
    # so I refrained from using them, but used local vars instead
    # In this case, if any tax rates  or thresholds change, it will be easy to 
    # update them here
    
    FIRST_THRESHOLD = 300001
    SECOND_THRESHOLD = 925001
    THIRD_THRESHOLD = 1500001

    # This dictionairy maps minimum thresholds to tax rates
    rates = {
        FIRST_THRESHOLD : 0.05,
        SECOND_THRESHOLD : 0.1,
        THIRD_THRESHOLD : 0.12,
    }
    
    # Array which contains all our thresholds
    thresholds = [FIRST_THRESHOLD, SECOND_THRESHOLD, THIRD_THRESHOLD]
    # Sort array to descending order
    thresholds.sort(reverse=True)
    
    # Property price below any threshold (lower than lowest threshold) (0%)
    if propertyPrice <= thresholds[-1]:
        return 0
    
    startingValueForTax = propertyPrice
    tax = 0

    # Iterating through our thresholds in descending order

    for THRESHOLD in thresholds:
        # If current value exceeds current threshold
        if startingValueForTax >= THRESHOLD:
            # Add tax at threshold
            tax += TaxAtThreshold(THRESHOLD, startingValueForTax, rates[THRESHOLD])
            # Set value at maximum for next calculation
            startingValueForTax = THRESHOLD -1
            
    # Return final tax rounded nearest integer
    return round(tax, 0)
