import os
from pathlib import Path

import typer
from omegaconf import DictConfig, OmegaConf
from pulp import (
    PULP_CBC_CMD,
    LpInteger,
    LpMaximize,
    LpProblem,
    LpVariable,
    lpSum,
    value,
)

OUTPUT_FILE = Path("results.txt")
if OUTPUT_FILE.exists():
    os.remove(OUTPUT_FILE)
f = open(OUTPUT_FILE, "w")
f.close()


def optimize_material(name: str, config: DictConfig, time_budget: int):
    problem = LpProblem(f"{name}_allocation", LpMaximize)

    # Define entities
    entities = {}
    for item in config.entities.keys():
        entities[item] = LpVariable(f"nrof_{item}", lowBound=0, cat=LpInteger)

    # Create objective function
    problem += (
        lpSum(
            [
                var * getattr(config.entities, name)["count"]
                for name, var in entities.items()
            ]
        ),
        "Objective Function",
    )

    # Create constraints

    # Slot constraints
    problem += (
        lpSum(var for var in entities.values()) <= config.slots,
        "Slot Limit Constraints",
    )

    # Time constraints
    problem += (
        lpSum(
            var * getattr(config.entities, name)["time_cost"]
            for name, var in entities.items()
        )
        <= time_budget,
        "Time Limit Constraints",
    )

    # Solver
    problem.solve(PULP_CBC_CMD(msg=0))

    # Results
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Allocation for {name} :\n")
        for var in problem.variables():
            if var.varValue != 0:
                f.write(f"{var.name} = {var.varValue}\n")

        f.write(f"Will obtain {name} = {value(problem.objective)}\n")
        f.write("=" * 60 + "\n")


def optimize_craft(name: str, config: DictConfig, time_budget: int):
    problem = LpProblem(f"{name}_allocation", LpMaximize)

    # Define entities
    entities = {}
    for item_name, item_config in config.item_name.items():
        for entity in item_config.entities.keys():
            entities[f"{item_name}_{entity}"] = LpVariable(
                f"nrof_{item_name}_{entity}", lowBound=0, cat=LpInteger
            )

    # Create objective function
    count_multiply_list = []

    for entity_name, entity in entities.items():
        parsed_item = entity_name.split("_")
        item_config = getattr(config.item_name, parsed_item[0])
        entity_config = getattr(item_config.entities, parsed_item[1])

        count_multiply = entity * entity_config.count
        count_multiply_list.append(count_multiply)

    problem += lpSum(count_multiply_list), "Objective Function"

    # Create constraints

    # Slot constraints

    problem += (
        lpSum(var for var in entities.values()) <= config.slots,
        "Slot Limit Constraints",
    )

    # Count constraints
    for item, item_config in config.item_name.items():

        if item_config.current >= item_config.max:
            for entity_name in item_config.entities.keys():
                problem += (
                    entities[f"{item}_{entity_name}"] == 0,
                    f"{item} Current More Than Max Constraint",
                )
        else:
            count_limit_list = []
            for entity_name, entity_config in item_config.entities.items():
                count_limit = (
                    entities[f"{item}_{entity_name}"] * entity_config.count
                )
                count_limit_list.append(count_limit)

            problem += (
                lpSum(count_limit_list) <= item_config.max,
                f"{item} Sum More Than Max Constraint ",
            )

    problem.writeLP("debug.lp")


def main(
    time_budget: int = typer.Option(3600), conf_file: str = "config.yaml"
):
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Optimal allocation for duration: {time_budget}\n\n")

    config = OmegaConf.load(conf_file)
    materials_config = config.materials
    crafts_config = config.crafts

    for material, config in materials_config.items():
        optimize_material(
            name=material,
            config=config,
            time_budget=time_budget,
        )

    for craft, config in crafts_config.items():
        optimize_craft(name=craft, config=config, time_budget=time_budget)


if __name__ == "__main__":
    typer.run(main)
