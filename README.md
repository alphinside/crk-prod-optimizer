# CRK Optimal Production Allocator

This repo contain script to help you optimize production plan of materials and items in Cookie Run Kingdom given a specific time budget

## Installation

- Install python3.8 - [Reference](https://realpython.com/installing-python/)
- Install poetry - [Reference](https://python-poetry.org/docs/)
- Set working directory to this repo

## Configuration

`config.yaml` contains configuration need to be set for each materials and items you want to search.

### Base Materials

This section explain the configuration of base materials like wood, jellybean, sugar, etc

```yaml
materials:
  wood:
    slots: 8
    entities:
      pack1:
        count: 3
        time_cost: 21 #in seconds
      pack2:
        count: 9
        time_cost: 246 #in seconds
      pack3:
        count: 20
        time_cost: 3682 #in seconds
```

Base material configuration should look like the above example.

- `wood` specify the item name you want to produce, feel free to change this as you like
- The section under `wood` however need to follow the standards
  - `slots` is the number of production slot you have for one building (max should be `8`)
  - `entities` is the material packs that you can choose to produce (wood shoulde be pack of `3`, `9` and `20` )
    - `pack1` is the identifier of each pack, feel free to modify it
    - The section under each pack is strict
      - `count` is the number of resource produced in each pack
      - `time_cost` is the duration needed for the entity to be fully produced (in seconds)

### Crafted Items

TODO

## Usage

- Ensure the working directory is the repo root directory (file `config.yaml` should be exist)
- Run the following command, `--time-budget` is the argument needed to set to point how long the production time you want to optimize

```shell
poetry run task optimize_alloc --time-budget 7200
```

- Example result which will be dumped to `results.txt` will look like this

```
Optimal allocation for duration: 7200

Allocation for wood :
nrof_pack1 = 0.0
nrof_pack2 = 7.0
nrof_pack3 = 1.0
Will obtain wood = 83.0
============================================================
Allocation for jellybean :
nrof_pack1 = 1.0
nrof_pack2 = 6.0
nrof_pack3 = 1.0
Will obtain jellybean = 77.0
============================================================
Allocation for sugar :
nrof_pack1 = 0.0
nrof_pack2 = 8.0
nrof_pack3 = 0.0
Will obtain sugar = 72.0
============================================================
Allocation for flour :
nrof_pack1 = 0.0
nrof_pack2 = 7.0
nrof_pack3 = 0.0
Will obtain flour = 63.0
============================================================
Allocation for berry :
nrof_pack1 = 0.0
nrof_pack2 = 4.0
nrof_pack3 = 0.0
Will obtain berry = 24.0
============================================================
Allocation for milk :
nrof_pack1 = 6.0
nrof_pack2 = 0.0
nrof_pack3 = 0.0
Will obtain milk = 12.0
============================================================
Allocation for cotton :
nrof_pack1 = 2.0
nrof_pack2 = 0.0
nrof_pack3 = 0.0
Will obtain cotton = 2.0
============================================================
```
