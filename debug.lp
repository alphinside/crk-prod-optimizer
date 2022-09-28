\* smithy_allocation *\
Maximize
Objective_Function: nrof_axe_pack1 + 10 nrof_axe_pack2 + nrof_hammer_pack1
 + nrof_pickaxe_pack1 + 10 nrof_pickaxe_pack2 + nrof_saw_pack1
 + 10 nrof_saw_pack2 + nrof_shovel_pack1 + 10 nrof_shovel_pack2
 + nrof_stake_pack1 + nrof_tongs_pack1
Subject To
Slot_Limit_Constraints: nrof_axe_pack1 + nrof_axe_pack2 + nrof_hammer_pack1
 + nrof_pickaxe_pack1 + nrof_pickaxe_pack2 + nrof_saw_pack1 + nrof_saw_pack2
 + nrof_shovel_pack1 + nrof_shovel_pack2 + nrof_stake_pack1 + nrof_tongs_pack1
 <= 8
Time_Limit_Constraints: 20 nrof_axe_pack1 + 1200 nrof_axe_pack2
 + 14400 nrof_hammer_pack1 + 120 nrof_pickaxe_pack1 + 3000 nrof_pickaxe_pack2
 + 280 nrof_saw_pack1 + 4200 nrof_saw_pack2 + 600 nrof_shovel_pack1
 + 6600 nrof_shovel_pack2 + 2400 nrof_stake_pack1 + 7200 nrof_tongs_pack1
 <= 21600
axe_Sum_More_Than_Max_Constraint_: nrof_axe_pack1 + 10 nrof_axe_pack2 <= 60
hammer_Sum_More_Than_Max_Constraint_: nrof_hammer_pack1 <= 27
pickaxe_Sum_More_Than_Max_Constraint_: nrof_pickaxe_pack1
 + 10 nrof_pickaxe_pack2 <= 15
saw_Sum_More_Than_Max_Constraint_: nrof_saw_pack1 + 10 nrof_saw_pack2 <= 25
shovel_Sum_More_Than_Max_Constraint_: nrof_shovel_pack1 + 10 nrof_shovel_pack2
 <= 20
stake_Current_More_Than_Max_Constraint: nrof_stake_pack1 = 0
tongs_Sum_More_Than_Max_Constraint_: nrof_tongs_pack1 <= 50
Bounds
 0 <= nrof_axe_pack1
 0 <= nrof_axe_pack2
 0 <= nrof_hammer_pack1
 0 <= nrof_pickaxe_pack1
 0 <= nrof_pickaxe_pack2
 0 <= nrof_saw_pack1
 0 <= nrof_saw_pack2
 0 <= nrof_shovel_pack1
 0 <= nrof_shovel_pack2
 0 <= nrof_stake_pack1
 0 <= nrof_tongs_pack1
Generals
nrof_axe_pack1
nrof_axe_pack2
nrof_hammer_pack1
nrof_pickaxe_pack1
nrof_pickaxe_pack2
nrof_saw_pack1
nrof_saw_pack2
nrof_shovel_pack1
nrof_shovel_pack2
nrof_stake_pack1
nrof_tongs_pack1
End
