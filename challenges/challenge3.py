class SalesItem:
  def __init__(self, branch, totalSales, date):
    self.branch = branch
    self.totalSales = totalSales
    self.date = date

# <summary >
# It has been a busy year at mountain warehouse, having made lots of sales.
# Management would like to know which branch made the most in revenue.
# For this challenge you will be given an array of sales broken down by Branch and Date.
# You will need to sum all branch across multiple days and identify which branch had the highest sales overall
# Assume that there is only one branch with the highest total
# We have provided some starting code but if you know of a better method then go ahead with that
# </summary >
# <param name = "sales" > The array of sales items < /param >
# <returns > The branch with the best performing sales < /returns >


def CalculateBestBranch(sales):

  # Check if empty list
  if len(sales) == 0:
    return

  branchSales = {}
  
  # Iterate through each sale in sales
  for sale in sales:
    branch = sale.branch
    
    # If the branch name is not found within the keys of branchSales, add to dictionairy
    if branch not in branchSales:
      branchSales[branch] = sale.totalSales
      
    # If the branch is found within the keys of branchSales, add to sales
    else:
      branchSales[branch] += sale.totalSales
  
  # Using sorted in built method to sort dictionairy by the values in descending order
  sortedBranchSales = sorted(branchSales.items(), key=lambda x:x[1], reverse=True)
  
  # Return the first value in the sorted list
  return sortedBranchSales[0][0]
  
    


