import sys
INF = 1000000000

"""
I worked on this assignment with Anne Glickenhaus, Miguel H. No code was copied, but ideas were shared.
I also used Geeks for Geeks a lot on this assignment to understand the concepts more and be able 
to create the code.
"""

def main():
    input_file = sys.stdin

    num_of_items = int(input_file.readline())
    spend_exactly_amt = int(input_file.readline())
    sys.setrecursionlimit(spend_exactly_amt)

    items = []
    all_costs = []
    all_calories = []
    for line in input_file:
        cost, calories, food = line.strip().split(" ")
        amount = 0 
        items.append([int(cost), int(calories), str(food), int(amount)])
        all_costs.append(int(cost))
        all_calories.append(int(calories))

    min_cal, min_cal_list, can_spend_exact = chipotle(items, spend_exactly_amt, num_of_items)


    if can_spend_exact == True:
        curr_cost = 0
        num = mem_chipotle(spend_exactly_amt, all_costs, all_calories, num_of_items, curr_cost)

        reconstruction = reconstruction_fun(min_cal_list, items, spend_exactly_amt, num_of_items)

        print('Possibly to spend exactly: {0}'.format(spend_exactly_amt))
        print('Minimum calories (iteratively): {0}'.format(min_cal))
        print("Minimim calories (memoization): {}".format(num))

        dict_food = {}
        for cost, calories, food, amount in reconstruction:
            if food not in dict_food:
                dict_food[food] = 1
            else:
                dict_food[food] += 1
        # print (dict_food)
        for food, value in dict_food.items():
            print ("{} {}".format(food, value))

    else:
        print("Not possible to spend exactly: {0}".format(spend_exactly_amt))


def mem_chipotle(spend_exactly_amt, all_costs, all_calories, num_of_items, curr_cost):
    """
    This is the memoization version to find the min calories while spending that amount.
    """
    if num_of_items == 0 or spend_exactly_amt == 0:
        return 0

    if (all_costs[num_of_items-1] > spend_exactly_amt):
        # curr_cost = add_amount(curr_cost, all_costs[num_of_items-1])
        cal_amt = mem_chipotle(spend_exactly_amt , all_costs, all_calories[num_of_items-1] , num_of_items-1, curr_cost) 
  
    else:
        cal_amt =  max(all_calories[num_of_items-1] + mem_chipotle(spend_exactly_amt - all_costs[num_of_items-1] , all_costs, all_calories , num_of_items-1, curr_cost), 
                   mem_chipotle(spend_exactly_amt , all_costs, all_calories , num_of_items-1, curr_cost)) 

    return cal_amt


def chipotle(items, spend_exactly_amt, num_of_items):
    """
    This is the iterative method to find the minimum number of calories
    while spending that exact limit. To keep track of if this was done 
    correctly or not, I have a bool can_spend_exact which is return and
    used in main to see if it is possible or not. 

    It also returns the minimum calories, and returns the matrix.
    https://www.geeksforgeeks.org/minimum-cost-to-fill-given-weight-in-a-bag/
    """
    can_spend_exact = False # change this bool if can spend exactly money
    food_bought = []

    # This is the site that helped me initialize the matrix like this: https://www.geeksforgeeks.org/initialize-matrix-in-python/
    min_cal = [[0 for i in range(spend_exactly_amt + 1)] for j in range (num_of_items + 1)]

    for i in range(spend_exactly_amt + 1):
        min_cal[0][i] = INF

    for i in range(1, num_of_items+1):
        min_cal[i][0] = 0


    for i in range(1, num_of_items + 1):
        for j in range(1, spend_exactly_amt+1):
            cost = items[i-1][0]
            cal = items[i-1][1]

            if (cost > j):
                min_cal[i][j] = min_cal[i-1][j]
            else:
                min_cal[i][j] = min(min_cal[i-1][j], min_cal[i][j-cost] + cal)

    if(min_cal[num_of_items][spend_exactly_amt] == INF):
        can_spend_exact = False
    else:
        can_spend_exact = True
        min_cal_amt = min_cal[num_of_items][spend_exactly_amt]


    min_calories = min_cal[len(items)][spend_exactly_amt]

    return min_calories, min_cal, can_spend_exact


def reconstruction_fun(min_cal, items, spend_exactly_amt, num_of_items):
    """
    This is a function to go through the matrix and see what food items were purchases in order
    to spend that amount and get that calorie number. This returns a list of all the items used.
    """
    bought_food = []

    i = num_of_items
    j = spend_exactly_amt
    while i > 0 and j != 0:
  
        if min_cal[i][j] != min_cal[i-1][j]:
            bought_food.append(items[i - 1])
            j -= items[i - 1][ 0]
            items[i-1][3] += 1

        else:
            i -= 1
            
    return bought_food

if __name__ == '__main__':
    main()