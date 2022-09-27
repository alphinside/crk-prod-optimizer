import typer
from enum import Enum
from pulp import LpProblem, LpMaximize,LpVariable,LpInteger, value,PULP_CBC_CMD
from omegaconf import OmegaConf

# def construct_problem()

# def optimize_wood(time_budget:int):
#     problem = LpProblem('wood_allocation', LpMaximize)
#     wood1 = LpVariable('wood1', lowBound=0 , cat=LpInteger)
#     wood2 = LpVariable('wood2', lowBound=0 , cat=LpInteger)
#     wood3 = LpVariable('wood3', lowBound=0 , cat=LpInteger)

#     #Objective Function
#     problem += wood1*3 + wood2*9 + wood3*20, 'Objective Function'

#     # The five constraints are entered
#     problem += wood1 + wood2 + wood3 == 8, "Slot Limit"
#     problem += wood1*21 + wood2*246 + wood3*3682 <= time_budget, "Time Limit",
#     problem.solve(PULP_CBC_CMD(msg=0))
#     print("Optimize prod allocation for wood:")
#     for v in problem.variables():
#         print(v.name, "=", v.varValue)

#     print("Obtained wood = ", value(problem.objective))

# def optimize_jelly(time_budget:int):
#     problem = LpProblem('jelly_allocation', LpMaximize)
#     jelly1 = LpVariable('jelly1', lowBound=0 , cat=LpInteger)
#     jelly2 = LpVariable('jelly2', lowBound=0 , cat=LpInteger)
#     jelly3 = LpVariable('jelly3', lowBound=0 , cat=LpInteger)

#     #Objective Function
#     problem += jelly1*3 + jelly2*9 + jelly3*20, 'Objective Function'

#     # The five constraints are entered
#     problem += jelly1 + jelly2 + jelly3 == 8, "Slot Limit"
#     problem += jelly1*40 + jelly2*480 + jelly3*4000 <= time_budget, "Time Limit",
#     problem.solve(PULP_CBC_CMD(msg=0))
#     print("Optimize prod allocation for jelly:")
#     for v in problem.variables():
#         print(v.name, "=", v.varValue)

#     print("Obtained jelly = ", value(problem.objective))

# def optimize_sugar(time_budget:int):
#     problem = LpProblem('sugar_allocation', LpMaximize)
#     sugar1 = LpVariable('sugar1', lowBound=0 , cat=LpInteger)
#     sugar2 = LpVariable('sugar2', lowBound=0 , cat=LpInteger)
#     sugar3 = LpVariable('sugar3', lowBound=0 , cat=LpInteger)

#     #Objective Function
#     problem += sugar1*3 + sugar2*9 + sugar3*20, 'Objective Function'

#     # The five constraints are entered
#     problem += sugar1 + sugar2 + sugar3 == 8, "Slot Limit"
#     problem += sugar1*62 + sugar2*573 + sugar3*4296 <= time_budget, "Time Limit",
#     problem.solve(PULP_CBC_CMD(msg=0))
#     print("Optimize prod allocation for sugar:")
#     for v in problem.variables():
#         print(v.name, "=", v.varValue)

#     print("Obtained sugar = ", value(problem.objective))

def main(time_budget: int = typer.Option(3600), conf_file: str = "config.yaml"):
    config = OmegaConf.load(conf_file)
    print(config)
    # optimize_wood(time_budget)
    # optimize_jelly(time_budget)
    # optimize_sugar(time_budget)

if __name__ == "__main__":
    typer.run(main)