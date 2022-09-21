# Diet optimization -
 # https://docs.ocean.dwavesys.com/en/stable/examples/hybrid_cqm_diet.html#example-cqm-diet-reals ††
# imports
import dimod as dimod       # thx red lightbulb
from dwave.system import LeapHybridCQMSampler         #o
 # solver is an option. [See the solve-by sampling section toward the end ††]
  # For charges - $$$
    # Select a solver
    # sampler = LeapHybridSampler()

    # Submit for solution
    # answer = sampler.sample_qubo(Q)

# Python 3.9.2
# Python 3.9.2
print('\nHello quantum world.')
print('\nThis is the diet optimization prob w taste v cost goal, gvn several ')
print('constraints.')

# food dict
foods = {'rice': {'Calories': 100, 'Protein': 3, 'Fat': 1, 'Carbs': 22,
                    'Fiber': 2, 'Taste': 7, 'Cost': 2.5, 'Units': 'continuous'},
        'tofu': {'Calories': 140, 'Protein': 17, 'Fat': 9, 'Carbs': 3,
                    'Fiber': 2, 'Taste': 2, 'Cost': 4.0, 'Units': 'continuous'},
        'banana': {'Calories': 90, 'Protein': 1, 'Fat': 0, 'Carbs': 23, 'Fiber': 3,
                    'Taste': 10, 'Cost': 1.0, 'Units': 'discrete'},
        'lentils': {'Calories': 150, 'Protein': 9, 'Fat': 0, 'Carbs': 25, 'Fiber': 4,
                    'Taste': 3, 'Cost': 1.3, 'Units': 'continuous'},
        'bread': {'Calories': 270, 'Protein': 9, 'Fat': 3, 'Carbs': 50, 'Fiber': 3,
                    'Taste': 5, 'Cost': 0.25, 'Units': 'continuous'},
        'avocado': {'Calories': 300, 'Protein': 4, 'Fat': 30, 'Carbs': 20, 'Fiber': 14,
                    'Taste': 5, 'Cost': 2.0, 'Units': 'discrete'}}

min_nutrients = {"Protein": 50, "Fat": 30, "Carbs": 130, "Fiber": 30}
max_calories = 2000                 # for setting up bounds

# quantities list
quantities = [dimod.Real(f"{food}") if foods[food]["Units"] == "continuous"
    else dimod.Integer(f"{food}")
    for food in foods.keys()]		# dimod error?

print(quantities[0])                # simple linear bias
print(2*quantities[0])              # Now dbl lin bias
#print(quantities[0] * quantities[1]) #Now a quadratic bias. # ValueError: REAL variables
                                                            # (e.g. 'rice') cannot have interactions
for ind, food in enumerate(foods.keys()):
    ub = max_calories / foods[food]["Calories"]  # upper bnd is 20 portions, (2000/100)
    quantities[ind].set_upper_bound(food, ub)

qub = quantities[0].upper_bound("rice")			# check
print('\nquantities[0].ub is: ', qub)                                      # -> 20.0

# setup the OBJective Fn w a UTILity Fn
cqm = dimod.ConstrainedQuadraticModel()			# NOT arbitrarily set alpha=2 beta=1;

# UTILity Fn
# You can define a utility function, TOTAL_MIX, to calculate the summations for any given CATEGORY
  # such as calories;
def total_mix(quantity, category):
    return sum(q * c for q, c in zip(quantity, (foods[food][category] for food in foods.keys())))
    ## ZIP https://www.w3schools.com/python/ref_func_zip.asp

# Set the objective2. Because Ocean solvers MINIMIZE OBJECTIVES, to maximize taste, Taste
   # is multiplied by -1 and minimized.
cqm.set_objective(-total_mix(quantities, "Taste") + 6*total_mix(quantities, "Cost"))

# TUNING/Constraints
# Constrain the diet’s calorie intake to the required daily MAXIMUM.
cqm.add_constraint(total_mix(quantities, "Calories") <= max_calories, label="Calories") # rtn 'Calories'

# Require that the daily MINIMUM of each nutrient is met or exceeded.
for nutrient, amount in min_nutrients.items():
    cqm.add_constraint(total_mix(quantities, nutrient) >= amount, label=nutrient)
'Protein'
'Carbs'
'Fat'
'Fiber'

# You can access these constraints as a dict with the labels as keys:
constraintsDictLabelsAsKeys = list(cqm.constraints.keys())
# list(cqm.constraints.keys())        #o # ['Calories', 'Protein', 'Fat', 'Carbs', 'Fiber']
print('\nConstraints Dict w labels as keys: ', constraintsDictLabelsAsKeys)
print('\nCal constraints (as polystr):', cqm.constraints['Calories'].to_polystring())
    # 100*rice + 140*tofu + 90*banana + 150*lentils + 270*bread + 300*avocado <= 200
print('\nPt constraints (as polystr):', cqm.constraints['Protein'].to_polystring())
    # 3*rice + 17*tofu + banana + 9*lentils + 9*bread + 4*avocado >= 50

'''
Solve the Problem by Sampling
Solve the Problem by Sampling
D-Wave’s quantum cloud service provides cloud-based hybrid solvers you can submit arbitrary QMs to.
These solvers, which implement state-of-the-art classical algorithms together with intelligent allocation
of the quantum processing unit (QPU) to parts of the problem where it benefits most, are designed to
accommodate even very large problems.
Ocean software’s dwave-system LeapHybridCQMSampler class enables you to easily incorporate Leap’s hybrid
CQM solvers into your application:
'''
# Make certain ur in (ocean) venv
sampler = LeapHybridCQMSampler()

'''
Submit the CQM to the selected solver. For one particular execution, the CQM hybrid sampler returned 
49 samples, out of which 25 were solutions that met all the constraints.
CQM) solver on a simple mixed-integer linear-programming (MILP) type of optimization problem.
'''
sampleset = sampler.sample_cqm(cqm)
feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)

print("\nThere are {} feasible solutions OUT of {}.\n".format(len(feasible_sampleset), len(sampleset)))
def print_diet(sample):
    diet = {food: round(quantity, 1) for food, quantity in sample.items()}
    print(f"\nDiet: {diet}")
    taste_total = sum(foods[food]["Taste"] * amount for food, amount in sample.items())
    cost_total = sum(foods[food]["Cost"] * amount for food, amount in sample.items())
    print(f"Total taste of {round(taste_total, 2)} at cost {round(cost_total, 2)}")
    for constraint in cqm.iter_constraint_data(sample):
        print(f"{constraint.label} (nominal: {constraint.rhs_energy}): {round(constraint.lhs_energy)}")

# The best solution found in this current execution was a diet of bread and bananas, with
# avocado completing the required fiber and fat portions
best = feasible_sampleset.first.sample
print_diet(best)
''' >>>  a la:
Diet: {'avocado': 1.0, 'banana': 6.0, 'bread': 4.1, 'lentils': 0.3, 'rice': 0.0, 'tofu': 0.0}
Total taste of 86.56 at cost 9.46
Calories (nominal: 2000): 2000
Protein (nominal: 50): 50
Fat (nominal: 30): 42
Carbs (nominal: 130): 372
Fiber (nominal: 30): 46
'''




