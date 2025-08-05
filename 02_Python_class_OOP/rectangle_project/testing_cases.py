# --length and --width: not_given, one_valid, both_valid, both_invalid
# --input:            : not_given, dir_many_json, dir_one_json, dir_no_json, json_file, other_file, not_existed
# --output:           : not_given, existed_dir, non_existed_dir, json_file, not_json_file

from itertools import product
import polars as pl

length_width = ['not_given', 'one_valid', 'both_valid', 'both_invalid']
input = ['not_given', 'dir_many_json', 'dir_one_json', 'dir_no_json', 'json_file', 'other_file', 'not_existed']
output = ['not_given', 'non_existed_dir', 'existed_dir', 'json_file', 'not_json_file']

df_testing_cases = pl.DataFrame(
    list(product(length_width, input, output)),
    schema=["Length_Width", "Input_path", "Output_path"]
)

# Show every row and every column in any subsequent print()
pl.Config.set_tbl_rows(-1)   # -1  ➜ unlimited rows
pl.Config.set_tbl_cols(-1)   # -1  ➜ unlimited columns


print(df_testing_cases)
# shape: (140, 3)
# ┌──────────────┬───────────────┬─────────────────┐
# │ Length_Width ┆ Input_path    ┆ Output_path     │   Testing command
# │ ---          ┆ ---           ┆ ---             │   (must be in 02_Python_class_OOP/rectangle_project first,
# │ str          ┆ str           ┆ str             │    use "cd 02_Python_class_OOP/rectangle_project")
# ╞══════════════╪═══════════════╪═════════════════╡
# │ not_given    ┆ not_given     ┆ not_given       │   python3 rectangle_module.py
# │ not_given    ┆ not_given     ┆ non_existed_dir │   python rectangle_module.py -o result
# │ not_given    ┆ not_given     ┆ existed_dir     │   python rectangle_module.py -o result
# │ not_given    ┆ not_given     ┆ json_file       │   python rectangle_module.py -o result.json
# │ not_given    ┆ not_given     ┆ not_json_file   │   python rectangle_module.py -o result.txt
# │ not_given    ┆ dir_many_json ┆ not_given       │
# │ not_given    ┆ dir_many_json ┆ non_existed_dir │
# │ not_given    ┆ dir_many_json ┆ existed_dir     │
# │ not_given    ┆ dir_many_json ┆ json_file       │
# │ not_given    ┆ dir_many_json ┆ not_json_file   │
# │ not_given    ┆ dir_one_json  ┆ not_given       │
# │ not_given    ┆ dir_one_json  ┆ non_existed_dir │
# │ not_given    ┆ dir_one_json  ┆ existed_dir     │
# │ not_given    ┆ dir_one_json  ┆ json_file       │
# │ not_given    ┆ dir_one_json  ┆ not_json_file   │
# │ not_given    ┆ dir_no_json   ┆ not_given       │
# │ not_given    ┆ dir_no_json   ┆ non_existed_dir │
# │ not_given    ┆ dir_no_json   ┆ existed_dir     │
# │ not_given    ┆ dir_no_json   ┆ json_file       │
# │ not_given    ┆ dir_no_json   ┆ not_json_file   │
# │ not_given    ┆ json_file     ┆ not_given       │
# │ not_given    ┆ json_file     ┆ non_existed_dir │
# │ not_given    ┆ json_file     ┆ existed_dir     │
# │ not_given    ┆ json_file     ┆ json_file       │
# │ not_given    ┆ json_file     ┆ not_json_file   │
# │ not_given    ┆ other_file    ┆ not_given       │
# │ not_given    ┆ other_file    ┆ non_existed_dir │
# │ not_given    ┆ other_file    ┆ existed_dir     │
# │ not_given    ┆ other_file    ┆ json_file       │
# │ not_given    ┆ other_file    ┆ not_json_file   │
# │ not_given    ┆ not_existed   ┆ not_given       │
# │ not_given    ┆ not_existed   ┆ non_existed_dir │
# │ not_given    ┆ not_existed   ┆ existed_dir     │
# │ not_given    ┆ not_existed   ┆ json_file       │
# │ not_given    ┆ not_existed   ┆ not_json_file   │
# │ one_valid    ┆ not_given     ┆ not_given       │
# │ one_valid    ┆ not_given     ┆ non_existed_dir │
# │ one_valid    ┆ not_given     ┆ existed_dir     │
# │ one_valid    ┆ not_given     ┆ json_file       │
# │ one_valid    ┆ not_given     ┆ not_json_file   │
# │ one_valid    ┆ dir_many_json ┆ not_given       │
# │ one_valid    ┆ dir_many_json ┆ non_existed_dir │
# │ one_valid    ┆ dir_many_json ┆ existed_dir     │
# │ one_valid    ┆ dir_many_json ┆ json_file       │
# │ one_valid    ┆ dir_many_json ┆ not_json_file   │
# │ one_valid    ┆ dir_one_json  ┆ not_given       │
# │ one_valid    ┆ dir_one_json  ┆ non_existed_dir │
# │ one_valid    ┆ dir_one_json  ┆ existed_dir     │
# │ one_valid    ┆ dir_one_json  ┆ json_file       │
# │ one_valid    ┆ dir_one_json  ┆ not_json_file   │
# │ one_valid    ┆ dir_no_json   ┆ not_given       │
# │ one_valid    ┆ dir_no_json   ┆ non_existed_dir │
# │ one_valid    ┆ dir_no_json   ┆ existed_dir     │
# │ one_valid    ┆ dir_no_json   ┆ json_file       │
# │ one_valid    ┆ dir_no_json   ┆ not_json_file   │
# │ one_valid    ┆ json_file     ┆ not_given       │
# │ one_valid    ┆ json_file     ┆ non_existed_dir │
# │ one_valid    ┆ json_file     ┆ existed_dir     │
# │ one_valid    ┆ json_file     ┆ json_file       │
# │ one_valid    ┆ json_file     ┆ not_json_file   │
# │ one_valid    ┆ other_file    ┆ not_given       │
# │ one_valid    ┆ other_file    ┆ non_existed_dir │
# │ one_valid    ┆ other_file    ┆ existed_dir     │
# │ one_valid    ┆ other_file    ┆ json_file       │
# │ one_valid    ┆ other_file    ┆ not_json_file   │
# │ one_valid    ┆ not_existed   ┆ not_given       │
# │ one_valid    ┆ not_existed   ┆ non_existed_dir │
# │ one_valid    ┆ not_existed   ┆ existed_dir     │
# │ one_valid    ┆ not_existed   ┆ json_file       │
# │ one_valid    ┆ not_existed   ┆ not_json_file   │
# │ both_valid   ┆ not_given     ┆ not_given       │
# │ both_valid   ┆ not_given     ┆ non_existed_dir │
# │ both_valid   ┆ not_given     ┆ existed_dir     │
# │ both_valid   ┆ not_given     ┆ json_file       │
# │ both_valid   ┆ not_given     ┆ not_json_file   │
# │ both_valid   ┆ dir_many_json ┆ not_given       │
# │ both_valid   ┆ dir_many_json ┆ non_existed_dir │
# │ both_valid   ┆ dir_many_json ┆ existed_dir     │
# │ both_valid   ┆ dir_many_json ┆ json_file       │
# │ both_valid   ┆ dir_many_json ┆ not_json_file   │
# │ both_valid   ┆ dir_one_json  ┆ not_given       │
# │ both_valid   ┆ dir_one_json  ┆ non_existed_dir │
# │ both_valid   ┆ dir_one_json  ┆ existed_dir     │
# │ both_valid   ┆ dir_one_json  ┆ json_file       │
# │ both_valid   ┆ dir_one_json  ┆ not_json_file   │
# │ both_valid   ┆ dir_no_json   ┆ not_given       │
# │ both_valid   ┆ dir_no_json   ┆ non_existed_dir │
# │ both_valid   ┆ dir_no_json   ┆ existed_dir     │
# │ both_valid   ┆ dir_no_json   ┆ json_file       │
# │ both_valid   ┆ dir_no_json   ┆ not_json_file   │
# │ both_valid   ┆ json_file     ┆ not_given       │
# │ both_valid   ┆ json_file     ┆ non_existed_dir │
# │ both_valid   ┆ json_file     ┆ existed_dir     │
# │ both_valid   ┆ json_file     ┆ json_file       │
# │ both_valid   ┆ json_file     ┆ not_json_file   │
# │ both_valid   ┆ other_file    ┆ not_given       │
# │ both_valid   ┆ other_file    ┆ non_existed_dir │
# │ both_valid   ┆ other_file    ┆ existed_dir     │
# │ both_valid   ┆ other_file    ┆ json_file       │
# │ both_valid   ┆ other_file    ┆ not_json_file   │
# │ both_valid   ┆ not_existed   ┆ not_given       │
# │ both_valid   ┆ not_existed   ┆ non_existed_dir │
# │ both_valid   ┆ not_existed   ┆ existed_dir     │
# │ both_valid   ┆ not_existed   ┆ json_file       │
# │ both_valid   ┆ not_existed   ┆ not_json_file   │
# │ both_invalid ┆ not_given     ┆ not_given       │
# │ both_invalid ┆ not_given     ┆ non_existed_dir │
# │ both_invalid ┆ not_given     ┆ existed_dir     │
# │ both_invalid ┆ not_given     ┆ json_file       │
# │ both_invalid ┆ not_given     ┆ not_json_file   │
# │ both_invalid ┆ dir_many_json ┆ not_given       │
# │ both_invalid ┆ dir_many_json ┆ non_existed_dir │
# │ both_invalid ┆ dir_many_json ┆ existed_dir     │
# │ both_invalid ┆ dir_many_json ┆ json_file       │
# │ both_invalid ┆ dir_many_json ┆ not_json_file   │
# │ both_invalid ┆ dir_one_json  ┆ not_given       │
# │ both_invalid ┆ dir_one_json  ┆ non_existed_dir │
# │ both_invalid ┆ dir_one_json  ┆ existed_dir     │
# │ both_invalid ┆ dir_one_json  ┆ json_file       │
# │ both_invalid ┆ dir_one_json  ┆ not_json_file   │
# │ both_invalid ┆ dir_no_json   ┆ not_given       │
# │ both_invalid ┆ dir_no_json   ┆ non_existed_dir │
# │ both_invalid ┆ dir_no_json   ┆ existed_dir     │
# │ both_invalid ┆ dir_no_json   ┆ json_file       │
# │ both_invalid ┆ dir_no_json   ┆ not_json_file   │
# │ both_invalid ┆ json_file     ┆ not_given       │
# │ both_invalid ┆ json_file     ┆ non_existed_dir │
# │ both_invalid ┆ json_file     ┆ existed_dir     │
# │ both_invalid ┆ json_file     ┆ json_file       │
# │ both_invalid ┆ json_file     ┆ not_json_file   │
# │ both_invalid ┆ other_file    ┆ not_given       │
# │ both_invalid ┆ other_file    ┆ non_existed_dir │
# │ both_invalid ┆ other_file    ┆ existed_dir     │
# │ both_invalid ┆ other_file    ┆ json_file       │
# │ both_invalid ┆ other_file    ┆ not_json_file   │
# │ both_invalid ┆ not_existed   ┆ not_given       │
# │ both_invalid ┆ not_existed   ┆ non_existed_dir │
# │ both_invalid ┆ not_existed   ┆ existed_dir     │
# │ both_invalid ┆ not_existed   ┆ json_file       │
# │ both_invalid ┆ not_existed   ┆ not_json_file   │
# └──────────────┴───────────────┴─────────────────┘