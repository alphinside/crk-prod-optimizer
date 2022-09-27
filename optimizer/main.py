import typer
from omegaconf import DictConfig, OmegaConf
from pulp import (
    PULP_CBC_CMD,
    LpInteger,
    LpMaximize,
    LpProblem,
    LpVariable,
    value,
)


def optimize_material(
    name: str, material_config: DictConfig, time_budget: int
):
    problem = LpProblem(f"{name}_allocation", LpMaximize)
    entities_list = list(material_config.entities.keys())

    # Define entities
    entities = {}
    for item in entities_list:
        entities[item] = LpVariable(item, lowBound=0, cat=LpInteger)

    # Create objective function
    objective_str = ""
    for idx, entity in enumerate(entities_list):
        material_count = getattr(material_config.entities, entity)["count"]
        objective_str += f"entities['{entity}']*int({material_count})"

        if idx != len(entities.keys()) - 1:
            objective_str += " + "

    problem += (eval(objective_str), "Objective Function")

    # Create constraints

    # Slot constraints
    slot_constraints_str = ""

    for idx, entity in enumerate(entities_list):
        slot_constraints_str += f"entities['{entity}']"

        if idx != len(entities.keys()) - 1:
            slot_constraints_str += " + "

    slot_constraints_str += f" <= {material_config.slots}"

    problem += (eval(slot_constraints_str), "Slot Limit Constraints")

    # Time constraints

    time_constraints_str = ""

    for idx, entity in enumerate(entities_list):
        material_time_cost = getattr(material_config.entities, entity)[
            "time_cost"
        ]
        time_constraints_str += (
            f"entities['{entity}']*int({material_time_cost})"
        )

        if idx != len(entities.keys()) - 1:
            time_constraints_str += " + "

    time_constraints_str += f" <= {time_budget}"

    problem += (eval(time_constraints_str), "Time Limit Constraints")

    # Solver
    problem.solve(PULP_CBC_CMD(msg=0))

    # Results
    for var in problem.variables():
        print(var.name, "=", var.varValue)

    print(f"Obtained {name} = ", value(problem.objective))


def main(
    time_budget: int = typer.Option(3600), conf_file: str = "config.yaml"
):
    config = OmegaConf.load(conf_file)
    materials_config = config.materials

    for material in materials_config:
        optimize_material(
            name=material,
            material_config=getattr(materials_config, material),
            time_budget=time_budget,
        )


if __name__ == "__main__":
    typer.run(main)
