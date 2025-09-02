'''
Boolean Filtering or Boolean Indexing is a powerful technique in Pandas 
that allows you to filter data based on specific conditions. 

###############################

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

4. Using .loc[] for Boolean Filtering within specific columns

5. Using .query() method for short-syntax condition filtering
'''

import pandas as pd
import re

df_pokemon = (
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

print(df_pokemon.head())
#                     Name Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                               
# 1              Bulbasaur  Grass  Poison    318  45      49       49      65      65     45          1      False
# 2                Ivysaur  Grass  Poison    405  60      62       63      80      80     60          1      False
# 3               Venusaur  Grass  Poison    525  80      82       83     100     100     80          1      False
# 3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123     122     120     80          1      False
# 4             Charmander   Fire     NaN    309  39      52       43      60      50     65          1      False

print(df_pokemon.dtypes)
# Index: 800 entries, 1 to 721
# Data columns (total 12 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   Name        800 non-null    object  
#  1   Type_1      800 non-null    category
#  2   Type_2      414 non-null    category
#  3   Total       800 non-null    int64   
#  4   HP          800 non-null    int64   
#  5   Attack      800 non-null    int64   
#  6   Defense     800 non-null    int64   
#  7   Sp_Atk      800 non-null    int64   
#  8   Sp_Def      800 non-null    int64   
#  9   Speed       800 non-null    int64   
#  10  Generation  800 non-null    category
#  11  Legendary   800 non-null    bool    
# dtypes: bool(1), category(3), int64(7), object(1)
# memory usage: 60.8+ KB

print(df_pokemon['Generation'].cat.categories)
# Name: Generation, Length: 800, dtype: category
# Categories (6, object): ['1' < '2' < '3' < '4' < '5' < '6']


#-------------------------------------------------------------------------------------------------------------#
#------------------------------------ 1. Single Condition Examples -------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

#######################################################
## Logic Operators: >, <, >=, <=, .between(), ==, != ##
#######################################################

#-------------
## > (greater than)
#-------------

print(df_pokemon[df_pokemon['HP'] > 200]) # HP greater than 200
#         Name  Type_1 Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                    
# 113  Chansey  Normal    NaN    450  250       5        5      35     105     50          1      False
# 242  Blissey  Normal    NaN    540  255      10       10      75     135     55          2      False

print(df_pokemon[df_pokemon["Sp_Atk"] > df_pokemon["Attack"]*2]) # Sp_Atk greater than double of Attkack
#                       Name    Type_1   Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                      
# 63                    Abra   Psychic      NaN    310   25      20       15     105      55     90          1      False
# 64                 Kadabra   Psychic      NaN    400   40      35       30     120      70    105          1      False
# 65                Alakazam   Psychic      NaN    500   55      50       45     135      95    120          1      False
# 65   AlakazamMega Alakazam   Psychic      NaN    590   55      50       65     175      95    150          1      False
# 81               Magnemite  Electric    Steel    325   25      35       70      95      55     45          1      False

#-------------
## < (less than)
#-------------

print(df_pokemon[df_pokemon['Speed'] < 15]) # Speed less than 20
#           Name  Type_1 Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                      
# 213    Shuckle     Bug   Rock    505   20      10      230      10     230      5          2      False
# 328   Trapinch  Ground    NaN    290   45     100       45      45      45     10          3      False
# 438     Bonsly    Rock    NaN    290   50      80       95      10      45     10          4      False
# 446   Munchlax  Normal    NaN    390  135      85       40      40      85      5          4      False
# 597  Ferroseed   Grass  Steel    305   44      50       91      24      86     10          5      False

print(df_pokemon[df_pokemon["Defense"] < df_pokemon["Attack"]*0.5]) # Defense less than half of Attkack
#                         Name    Type_1  Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                       
# 15                  Beedrill       Bug  Poison    395   65      90       40      45      80     75          1      False
# 15     BeedrillMega Beedrill       Bug  Poison    495   65     150       40      15      80    145          1      False
# 39                Jigglypuff    Normal   Fairy    270  115      45       20      45      25     20          1      False
# 50                   Diglett    Ground     NaN    265   10      55       25      35      45     95          1      False
# 56                    Mankey  Fighting     NaN    305   40      80       35      35      45     70          1      False


'''
THE SAME FOR ">=" (greater or equal) and "<=" (less or equal)
'''

#-------------
## .between()
#-------------
'''
inclusive = "both" (default): [left, right] or left <= x <= right
inclusive = "neither": (left, right) or left < x < right
inclusive = "left": [left, right) or left <= x < right
inclusive = "right": (left, right] or left < x <= right
'''

print(df_pokemon[df_pokemon['Speed'].between(5, 10)]) # Speed between 100 and 150 (inclusive)
#           Name  Type_1 Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                      
# 213    Shuckle     Bug   Rock    505   20      10      230      10     230      5          2      False
# 328   Trapinch  Ground    NaN    290   45     100       45      45      45     10          3      False
# 438     Bonsly    Rock    NaN    290   50      80       95      10      45     10          4      False
# 446   Munchlax  Normal    NaN    390  135      85       40      40      85      5          4      False
# 597  Ferroseed   Grass  Steel    305   44      50       91      24      86     10          5      False

#-------------
## == (equal) and != (not equal)
#-------------

print(df_pokemon[df_pokemon['Type_1'] == 'Fire']) # Type_1 equal to 'Fire'
#                           Name Type_1    Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                        
# 4                   Charmander   Fire       NaN    309   39      52       43      60      50     65          1      False
# 5                   Charmeleon   Fire       NaN    405   58      64       58      80      65     80          1      False
# 6                    Charizard   Fire    Flying    534   78      84       78     109      85    100          1      False
# 6    CharizardMega Charizard X   Fire    Dragon    634   78     130      111     130      85    100          1      False
# 6    CharizardMega Charizard Y   Fire    Flying    634   78     104       78     159     115    100          1      False

print(df_pokemon[df_pokemon["Legendary"] == True]) # Legendary equal to True
#                     Name    Type_1    Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                     
# 144             Articuno       Ice    Flying    580   90      85      100      95     125     85          1       True
# 145               Zapdos  Electric    Flying    580   90      90       85     125      90    100          1       True
# 146              Moltres      Fire    Flying    580   90     100       90     125      85     90          1       True
# 150               Mewtwo   Psychic       NaN    680  106     110       90     154      90    130          1       True
# 150  MewtwoMega Mewtwo X   Psychic  Fighting    780  106     190      100     154     100    130          1       True

#-------------
## != (not equal)
#-------------

print(df_pokemon[df_pokemon['Type_2'] != 'Flying']) # Type_2 not equal to 'Flying'
#                       Name   Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                   
# 1                Bulbasaur    Grass  Poison    318  45      49       49      65      65     45          1      False
# 2                  Ivysaur    Grass  Poison    405  60      62       63      80      80     60          1      False
# 3                 Venusaur    Grass  Poison    525  80      82       83     100     100     80          1      False
# 3    VenusaurMega Venusaur    Grass  Poison    625  80     100      123     122     120     80          1      False
# 4               Charmander     Fire     NaN    309  39      52       43      60      50     65          1      False

print(df_pokemon[df_pokemon["Generation"] != '1']) # Generation not equal to '1'
#                     Name   Type_1 Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                
# 152            Chikorita    Grass    NaN    318  45      49       65      49      65     45          2      False
# 153              Bayleef    Grass    NaN    405  60      62       80      63      80     60          2      False
# 154             Meganium    Grass    NaN    525  80      82      100      83     100     80          2      False
# 155            Cyndaquil     Fire    NaN    309  39      52       43      60      50     65          2      False
# 156              Quilava     Fire    NaN    405  58      64       58      80      65     80          2      False

##############################
##          .isin()         ##
##############################

print(df_pokemon[df_pokemon['Type_1'].isin(['Fire', 'Water'])]) # Type_1 in the list ['Fire', 'Water']
#                  Name Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #
# 667            Litleo   Fire  Normal    369  62      50       58      73      54     72          6      False
# 668            Pyroar   Fire  Normal    507  86      68       72     109      66    106          6      False
# 692         Clauncher  Water     NaN    330  50      53       62      58      63     44          6      False
# 693         Clawitzer  Water     NaN    500  71      73       88     120      89     59          6      False
# 721         Volcanion   Fire   Water    600  80     110      120     130      90     70          6       True

print(df_pokemon[df_pokemon["Generation"].isin(['4', '6'])]) # Generation in the list ['4', '6']
#                     Name   Type_1    Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                   
# 387              Turtwig    Grass       NaN    318  55      68       64      45      55     31          4      False
# 388               Grotle    Grass       NaN    405  75      89       85      55      65     36          4      False
# 389             Torterra    Grass    Ground    525  95     109      105      75      85     56          4      False
# 720   HoopaHoopa Unbound  Psychic      Dark    680  80     160       60     170     130     80          6       True
# 721            Volcanion     Fire     Water    600  80     110      120     130      90     70          6       True