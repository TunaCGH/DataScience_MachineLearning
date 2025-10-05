''' dr.filter_()

1. Single Condition Examples:
   + Logic Operators: >, <, >=, <=, .between(), ==, !=
   + .isin()
   + String Boolean: .str.contains(), .str.startswith(), .str.endswith(), ....
   + DateTime Boolean: .dt.is_month_start, .dt.is_month_end, ...

2. Negation of Condition: ~ (tilde) operator

3. Combine Multiple Conditions:
   + & (and),
   + | (or)
   + Combine & and |

4. Columns with "bad" names: using f["col name"]
'''
import datar.all as dr
from datar import f
import pandas as pd

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")

########################

tb_pokemon = dr.tibble(
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/pokemon.csv",
        index_col = "#",
        dtype = {
            "Type 1": "category",
            "Type 2": "category",
            "Generation": "category",
            "Legendary": "bool"
        }
    )
    .pipe(lambda df: df.set_axis(df.columns.str.strip().str.replace(r"\s+", "_", regex = True).str.replace(".", ""), axis=1))
    .assign(Generation = lambda df: df['Generation'].cat.as_ordered())
)

print(
    tb_pokemon
    >> dr.slice_head(n=5)
)
#                     Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                             
# #               <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 1              Bulbasaur      Grass     Poison     318      45      49       49      65      65      45          1      False
# 2                Ivysaur      Grass     Poison     405      60      62       63      80      80      60          1      False
# 3               Venusaur      Grass     Poison     525      80      82       83     100     100      80          1      False
# 3  VenusaurMega Venusaur      Grass     Poison     625      80     100      123     122     120      80          1      False
# 4             Charmander       Fire        NaN     309      39      52       43      60      50      65          1      False


#-------------------------------------------------------------------------------------------------------------#
#------------------------------------ 1. Single Condition Examples -------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

#######################################################
## Logic Operators: >, <, >=, <=, .between(), ==, != ##
#######################################################

#-------------
## > (greater than)
#-------------

print(
    tb_pokemon
    >> dr.filter_(f.Attack > 150)
    >> dr.slice_head(n=5)
)
#                         Name     Type_1     Type_2   Total      HP       Sp_Atk  Sp_Def   Speed  Generation  Legendary
#                                                                     ...                                               
# #                   <object> <category> <category> <int64> <int64>  ... <int64> <int64> <int64>  <category>     <bool>
# 127        PinsirMega Pinsir        Bug     Flying     600      65  ...      65      90     105           1      False
# 130    GyaradosMega Gyarados      Water       Dark     640      95  ...      70     130      81           1      False
# 150      MewtwoMega Mewtwo X    Psychic   Fighting     780     106  ...     154     100     130           1       True
# 214  HeracrossMega Heracross        Bug   Fighting     600      80  ...      40     105      75           2      False
# 248  TyranitarMega Tyranitar       Rock       Dark     700     100  ...      95     120      71           2      False

print(
    tb_pokemon
    >> dr.filter_(f.Sp_Atk > f.Attack*2)
    >> dr.slice_head(n=5)
)
#                      Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                              
# #                <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 63                   Abra    Psychic        NaN     310      25      20       15     105      55      90          1      False
# 64                Kadabra    Psychic        NaN     400      40      35       30     120      70     105          1      False
# 65               Alakazam    Psychic        NaN     500      55      50       45     135      95     120          1      False
# 65  AlakazamMega Alakazam    Psychic        NaN     590      55      50       65     175      95     150          1      False
# 81              Magnemite   Electric      Steel     325      25      35       70      95      55      45          1      False

#-------------
## < (less than)
#-------------

print(
    tb_pokemon
    >> dr.filter_(f.Speed < 15)
    >> dr.slice_head(n=5)
)
#           Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                   
# #     <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 213    Shuckle        Bug       Rock     505      20      10      230      10     230       5          2      False
# 328   Trapinch     Ground        NaN     290      45     100       45      45      45      10          3      False
# 438     Bonsly       Rock        NaN     290      50      80       95      10      45      10          4      False
# 446   Munchlax     Normal        NaN     390     135      85       40      40      85       5          4      False
# 597  Ferroseed      Grass      Steel     305      44      50       91      24      86      10          5      False

print(
    tb_pokemon
    >> dr.filter_(f.Defense < f.Attack*0.5)
    >> dr.slice_head(n=5)
)
#                      Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                              
# #                <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 15               Beedrill        Bug     Poison     395      65      90       40      45      80      75          1      False
# 15  BeedrillMega Beedrill        Bug     Poison     495      65     150       40      15      80     145          1      False
# 39             Jigglypuff     Normal      Fairy     270     115      45       20      45      25      20          1      False
# 50                Diglett     Ground        NaN     265      10      55       25      35      45      95          1      False
# 56                 Mankey   Fighting        NaN     305      40      80       35      35      45      70          1      False

'''
THE SAME FOR ">=" (greater or equal) and "<=" (less or equal)
'''

#-------------
## .between(left, right, inclusive = 'both')
#-------------
'''
inclusive = "both" (default): [left, right] or left <= x <= right
inclusive = "neither": (left, right) or left < x < right
inclusive = "left": [left, right) or left <= x < right
inclusive = "right": (left, right] or left < x <= right
'''

print(
    tb_pokemon
    >> dr.filter_(f.Defense.between(100, 150, inclusive = "both"))
    >> dr.slice_head(n=5)
)
#                          Name     Type_1     Type_2   Total      HP       Sp_Atk  Sp_Def   Speed  Generation  Legendary
#                                                                      ...                                               
# #                    <object> <category> <category> <int64> <int64>  ... <int64> <int64> <int64>  <category>     <bool>
# 3       VenusaurMega Venusaur      Grass     Poison     625      80  ...     122     120      80           1      False
# 6   CharizardMega Charizard X       Fire     Dragon     634      78  ...     130      85     100           1      False
# 9                   Blastoise      Water        NaN     530      79  ...      85     105      78           1      False
# 9     BlastoiseMega Blastoise      Water        NaN     630      79  ...     135     115      78           1      False
# 28                  Sandslash     Ground        NaN     450      75  ...      45      55      65           1      False

#-------------
## == (equal)
#-------------

print(
    tb_pokemon
    >> dr.filter_(f.Type_1 == 'Fire')
    >> dr.slice_head(n=5)
)
#                         Name     Type_1     Type_2   Total      HP       Sp_Atk  Sp_Def   Speed  Generation  Legendary
#                                                                     ...                                               
# #                   <object> <category> <category> <int64> <int64>  ... <int64> <int64> <int64>  <category>     <bool>
# 4                 Charmander       Fire        NaN     309      39  ...      60      50      65           1      False
# 5                 Charmeleon       Fire        NaN     405      58  ...      80      65      80           1      False
# 6                  Charizard       Fire     Flying     534      78  ...     109      85     100           1      False
# 6  CharizardMega Charizard X       Fire     Dragon     634      78  ...     130      85     100           1      False
# 6  CharizardMega Charizard Y       Fire     Flying     634      78  ...     159     115     100           1      False

#-------------
## != (not equal)
#-------------

print(
    tb_pokemon
    >> dr.filter_(f.Type_1 != 'Fire')
    >> dr.slice_head(n=5)
)
#                     Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                             
# #               <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 1              Bulbasaur      Grass     Poison     318      45      49       49      65      65      45          1      False
# 2                Ivysaur      Grass     Poison     405      60      62       63      80      80      60          1      False
# 3               Venusaur      Grass     Poison     525      80      82       83     100     100      80          1      False
# 3  VenusaurMega Venusaur      Grass     Poison     625      80     100      123     122     120      80          1      False
# 7               Squirtle      Water        NaN     314      44      48       65      50      64      43          1      False

##############################
##          .isin()         ##
##############################

print(
    tb_pokemon
    >> dr.filter_(f.Type_1.isin(['Fire', 'Water'])) # Type_1 in the list ['Fire', 'Water']
    >> dr.slice_head(n=5)
)
#                         Name     Type_1     Type_2   Total      HP       Sp_Atk  Sp_Def   Speed  Generation  Legendary
#                                                                     ...                                               
# #                   <object> <category> <category> <int64> <int64>  ... <int64> <int64> <int64>  <category>     <bool>
# 4                 Charmander       Fire        NaN     309      39  ...      60      50      65           1      False
# 5                 Charmeleon       Fire        NaN     405      58  ...      80      65      80           1      False
# 6                  Charizard       Fire     Flying     534      78  ...     109      85     100           1      False
# 6  CharizardMega Charizard X       Fire     Dragon     634      78  ...     130      85     100           1      False
# 6  CharizardMega Charizard Y       Fire     Flying     634      78  ...     159     115     100           1      False

print(
    tb_pokemon
    >> dr.filter_(f.Generation.isin(['4', '6'])) # Generation in the list ['4', '6']
    >> dr.slice_head(n=5)
)
#          Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                  
# #    <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 387   Turtwig      Grass        NaN     318      55      68       64      45      55      31          4      False
# 388    Grotle      Grass        NaN     405      75      89       85      55      65      36          4      False
# 389  Torterra      Grass     Ground     525      95     109      105      75      85      56          4      False
# 390  Chimchar       Fire        NaN     309      44      58       44      58      44      61          4      False
# 391  Monferno       Fire   Fighting     405      64      78       52      78      52      81          4      False

##############################
##      String Boolean      ##
##############################

print(
    tb_pokemon
    >> dr.filter_(f.Name.str.contains('Mega')) # Name contains the substring 'Mega'
    >> dr.slice_head(n=5)
)
#                          Name     Type_1     Type_2   Total      HP       Sp_Atk  Sp_Def   Speed  Generation  Legendary
#                                                                      ...                                               
# #                    <object> <category> <category> <int64> <int64>  ... <int64> <int64> <int64>  <category>     <bool>
# 3       VenusaurMega Venusaur      Grass     Poison     625      80  ...     122     120      80           1      False
# 6   CharizardMega Charizard X       Fire     Dragon     634      78  ...     130      85     100           1      False
# 6   CharizardMega Charizard Y       Fire     Flying     634      78  ...     159     115     100           1      False
# 9     BlastoiseMega Blastoise      Water        NaN     630      79  ...     135     115      78           1      False
# 15      BeedrillMega Beedrill        Bug     Poison     495      65  ...      15      80     145           1      False

print(
    tb_pokemon
    >> dr.filter_(f.Name.str.startswith('Tor')) # Name starts with the substring 'Tor'
    >> dr.slice_head(n=5)
)
#                         Name     Type_1     Type_2   Total      HP       Sp_Atk  Sp_Def   Speed  Generation  Legendary
#                                                                     ...                                               
# #                   <object> <category> <category> <int64> <int64>  ... <int64> <int64> <int64>  <category>     <bool>
# 255                  Torchic       Fire        NaN     310      45  ...      70      50      45           3      False
# 324                  Torkoal       Fire        NaN     470      70  ...      85      70      20           3      False
# 389                 Torterra      Grass     Ground     525      95  ...      75      85      56           4      False
# 641  TornadusIncarnate Forme     Flying        NaN     580      79  ...     125      80     111           5       True
# 641    TornadusTherian Forme     Flying        NaN     580      79  ...     110      90     121           5       True

print(
    tb_pokemon
    >> dr.filter_(f.Name.str.endswith('ite')) # Name ends with the substring 'ite'
    >> dr.slice_head(n=5)
)
#           Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                   
# #     <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 81   Magnemite   Electric      Steel     325      25      35       70      95      55      45          1      False
# 149  Dragonite     Dragon     Flying     600      91     134       95     100     100      80          1      False
# 307   Meditite   Fighting    Psychic     280      30      40       55      40      55      60          3      False
# 444     Gabite     Dragon     Ground     410      68      90       65      50      55      82          4      False
# 499    Pignite       Fire   Fighting     418      90      93       55      70      55      55          5      False

##############################
##     DateTime Boolean     ##
##############################

tb_emp = dr.tibble(
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/emp.csv",
        parse_dates = ["start_date"]
    )
)

print(
    tb_emp
    >> dr.filter_(f.start_date.dt.is_month_start)
)
#        id     name    salary       start_date     dept
#   <int64> <object> <float64> <datetime64[ns]> <object>
# 0       1     Rick     623.3       2012-01-01       IT

print(
    tb_emp
    >> dr.filter_(f.start_date.dt.is_leap_year)
)
#        id     name    salary       start_date     dept
#   <int64> <object> <float64> <datetime64[ns]> <object>
# 0       1     Rick     623.3       2012-01-01       IT


#-------------------------------------------------------------------------------------------------------------#
#---------------------------- 2. Negation of Condition: ~ (tilde) operator -----------------------------------#
#-------------------------------------------------------------------------------------------------------------#

print(
    tb_pokemon
    >> dr.filter_(~(f.Type_1 == 'Fire')) # Type_1 not equal to 'Fire'
    >> dr.slice_head(n=5)
)
#                     Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                             
# #               <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 1              Bulbasaur      Grass     Poison     318      45      49       49      65      65      45          1      False
# 2                Ivysaur      Grass     Poison     405      60      62       63      80      80      60          1      False
# 3               Venusaur      Grass     Poison     525      80      82       83     100     100      80          1      False
# 3  VenusaurMega Venusaur      Grass     Poison     625      80     100      123     122     120      80          1      False
# 7               Squirtle      Water        NaN     314      44      48       65      50      64      43          1      False

print(
    tb_pokemon
    >> dr.filter_(~f.Type_1.isin(['Fire', 'Water'])) # Type_1 not in the list ['Fire', 'Water']
    >> dr.slice_head(n=5)
)
#                      Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                              
# #                <object> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 1               Bulbasaur      Grass     Poison     318      45      49       49      65      65      45          1      False
# 2                 Ivysaur      Grass     Poison     405      60      62       63      80      80      60          1      False
# 3                Venusaur      Grass     Poison     525      80      82       83     100     100      80          1      False
# 3   VenusaurMega Venusaur      Grass     Poison     625      80     100      123     122     120      80          1      False
# 10               Caterpie        Bug        NaN     195      45      30       35      20      20      45          1      False