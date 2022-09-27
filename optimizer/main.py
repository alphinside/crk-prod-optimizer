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


def optimize_material(
    name: str, material_config: DictConfig, time_budget: int
):
    problem = LpProblem(f"{name}_allocation", LpMaximize)
    entities_list = list(material_config.entities.keys())

    # Define entities
    entities = {}
    for item in entities_list:
        entities[item] = LpVariable(f"nrof_{item}", lowBound=0, cat=LpInteger)

    # Create objective function
    problem += (
        lpSum(
            [
                var * getattr(material_config.entities, name)["count"]
                for name, var in entities.items()
            ]
        ),
        "Objective Function",
    )

    # Create constraints

    # Slot constraints
    problem += (
        lpSum(var for var in entities.values()) <= material_config.slots,
        "Slot Limit Constraints",
    )

    # Time constraints
    problem += (
        lpSum(
            var * getattr(material_config.entities, name)["time_cost"]
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
            f.write(f"{var.name} = {var.varValue}\n")

        f.write(f"Will obtain {name} = {value(problem.objective)}\n")
        f.write("=" * 60 + "\n")


def main(
    time_budget: int = typer.Option(3600), conf_file: str = "config.yaml"
):
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Optimal allocation for duration: {time_budget}\n\n")

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
