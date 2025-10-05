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

5. Using .query() for short-syntax condition
   + df.query("condition_expression")
   + df.query("colname.str.method()") => string methods (same for .dt and .cat methods)
   + df.query("~condition_expression") => negation of condition
   + df.query()[["col_1", "col_2", ...]]
   + Using `column name` if the column name has special characters
   + Using @ to reference variables outside the DataFrame
'''

import pandas as pd

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
## == (equal)
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

##############################
##      String Boolean      ##
##############################

print(df_pokemon[df_pokemon['Name'].str.contains('Mega')]) # Name contains 'Mega'
#                           Name    Type_1    Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                           
# 3        VenusaurMega Venusaur     Grass    Poison    625   80     100      123     122     120     80          1      False
# 6    CharizardMega Charizard X      Fire    Dragon    634   78     130      111     130      85    100          1      False
# 6    CharizardMega Charizard Y      Fire    Flying    634   78     104       78     159     115    100          1      False
# 9      BlastoiseMega Blastoise     Water       NaN    630   79     103      120     135     115     78          1      False
# 15       BeedrillMega Beedrill       Bug    Poison    495   65     150       40      15      80    145          1      False

print(df_pokemon[df_pokemon['Name'].str.startswith('Tor')]) # Name starts with 'Tor'
#                         Name  Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                    
# 255                  Torchic    Fire     NaN    310  45      60       40      70      50     45          3      False
# 324                  Torkoal    Fire     NaN    470  70      85      140      85      70     20          3      False
# 389                 Torterra   Grass  Ground    525  95     109      105      75      85     56          4      False
# 641  TornadusIncarnate Forme  Flying     NaN    580  79     115       70     125      80    111          5       True
# 641    TornadusTherian Forme  Flying     NaN    580  79     100       80     110      90    121          5       True

print(df_pokemon[df_pokemon['Name'].str.endswith('saur')]) # Name ends with 'saur'
#                     Name Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                               
# 1              Bulbasaur  Grass  Poison    318  45      49       49      65      65     45          1      False
# 2                Ivysaur  Grass  Poison    405  60      62       63      80      80     60          1      False
# 3               Venusaur  Grass  Poison    525  80      82       83     100     100     80          1      False
# 3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123     122     120     80          1      False

##############################
##     DateTime Boolean     ##
##############################

df_emp = pd.read_csv(
    filepath_or_buffer = "05_Pandas_DataR_dataframe/data/emp.csv",
    parse_dates = ["start_date"]
)

print(df_emp.dtypes)
# id                     int64
# name                  object
# salary               float64
# start_date    datetime64[ns]
# dept                  object
# dtype: object

print(df_emp[df_emp['start_date'].dt.is_month_start]) # start_date is month start
#    id  name  salary start_date dept
# 0   1  Rick   623.3 2012-01-01   IT

print(df_emp[df_emp['start_date'].dt.is_leap_year]) # start_date is in a leap year
#    id  name  salary start_date dept
# 0   1  Rick   623.3 2012-01-01   IT


#-------------------------------------------------------------------------------------------------------------#
#---------------------------- 2. Negation of Condition: ~ (tilde) operator -----------------------------------#
#-------------------------------------------------------------------------------------------------------------#

print(df_pokemon[~(df_pokemon['Type_1'] == 'Fire')]) # Type_1 not equal to 'Fire'
#                       Name   Type_1  Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                    
# 1                Bulbasaur    Grass  Poison    318   45      49       49      65      65     45          1      False
# 2                  Ivysaur    Grass  Poison    405   60      62       63      80      80     60          1      False
# 3                 Venusaur    Grass  Poison    525   80      82       83     100     100     80          1      False
# 3    VenusaurMega Venusaur    Grass  Poison    625   80     100      123     122     120     80          1      False
# 7                 Squirtle    Water     NaN    314   44      48       65      50      64     43          1      False
# ..                     ...      ...     ...    ...  ...     ...      ...     ...     ...    ...        ...        ...
# 718       Zygarde50% Forme   Dragon  Ground    600  108     100      121      81      95     95          6       True
# 719                Diancie     Rock   Fairy    600   50     100      150     100     150     50          6       True
# 719    DiancieMega Diancie     Rock   Fairy    700   50     160      110     160     110    110          6       True
# 720    HoopaHoopa Confined  Psychic   Ghost    600   80     110       60     150     130     70          6       True
# 720     HoopaHoopa Unbound  Psychic    Dark    680   80     160       60     170     130     80          6       True

# [748 rows x 12 columns]

print(df_pokemon[~df_pokemon['Type_2'].isin(["Ground", "Ghost"])]) # Type_2 not in the list ['Ground', 'Ghost']
#                       Name   Type_1  Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                    
# 1                Bulbasaur    Grass  Poison    318   45      49       49      65      65     45          1      False
# 2                  Ivysaur    Grass  Poison    405   60      62       63      80      80     60          1      False
# 3                 Venusaur    Grass  Poison    525   80      82       83     100     100     80          1      False
# 3    VenusaurMega Venusaur    Grass  Poison    625   80     100      123     122     120     80          1      False
# 4               Charmander     Fire     NaN    309   39      52       43      60      50     65          1      False
# ..                     ...      ...     ...    ...  ...     ...      ...     ...     ...    ...        ...        ...
# 717                Yveltal     Dark  Flying    680  126     131       95     131      98     99          6       True
# 719                Diancie     Rock   Fairy    600   50     100      150     100     150     50          6       True
# 719    DiancieMega Diancie     Rock   Fairy    700   50     160      110     160     110    110          6       True
# 720     HoopaHoopa Unbound  Psychic    Dark    680   80     160       60     170     130     80          6       True
# 721              Volcanion     Fire   Water    600   80     110      120     130      90     70          6       True

# [751 rows x 12 columns]


#-------------------------------------------------------------------------------------------------------------#
#---------------------------- 3. Combine Multiple Conditions: & (and), | (or) --------------------------------#
#-------------------------------------------------------------------------------------------------------------#

###########################
##       & (and)         ##
###########################
'''True if only all the conditions (clauses) are True.'''

# Type_1 equal to 'Fire' AND Generation equal to '1'
print(df_pokemon[(df_pokemon['Type_1'] == 'Fire') & (df_pokemon['Generation'] == '1')])
#                           Name Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                     
# 4                   Charmander   Fire     NaN    309  39      52       43      60      50     65          1      False
# 5                   Charmeleon   Fire     NaN    405  58      64       58      80      65     80          1      False
# 6                    Charizard   Fire  Flying    534  78      84       78     109      85    100          1      False
# 6    CharizardMega Charizard X   Fire  Dragon    634  78     130      111     130      85    100          1      False
# 6    CharizardMega Charizard Y   Fire  Flying    634  78     104       78     159     115    100          1      False
# 37                      Vulpix   Fire     NaN    299  38      41       40      50      65     65          1      False

# Type_2 equal to 'Flying' AND Speed greater than 100
print(df_pokemon[(df_pokemon['Type_2'] == 'Flying') & (df_pokemon['Speed'] > 100)])
#                           Name    Type_1  Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                         
# 18                     Pidgeot    Normal  Flying    479   83      80       75      70      70    101          1      False
# 18         PidgeotMega Pidgeot    Normal  Flying    579   83      80       80     135      80    121          1      False
# 123                    Scyther       Bug  Flying    500   70     110       80      55      80    105          1      False
# 127          PinsirMega Pinsir       Bug  Flying    600   65     155      120      65      90    105          1      False
# 142                 Aerodactyl      Rock  Flying    515   80     105       65      60      75    130          1      False
# 142  AerodactylMega Aerodactyl      Rock  Flying    615   80     135       85      70      95    150          1      False

###########################
##       | (or)          ##
###########################
'''False if only all the conditions (clauses) are False.'''

# HP less than 50 OR HP greater than 100
print(df_pokemon[(df_pokemon['HP'] < 30) | (df_pokemon['HP'] > 100)])
#                  Name    Type_1  Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                
# 39         Jigglypuff    Normal   Fairy    270  115      45       20      45      25     20          1      False
# 40         Wigglytuff    Normal   Fairy    435  140      70       45      85      50     45          1      False
# 50            Diglett    Ground     NaN    265   10      55       25      35      45     95          1      False
# 63               Abra   Psychic     NaN    310   25      20       15     105      55     90          1      False
# 81          Magnemite  Electric   Steel    325   25      35       70      95      55     45          1      False
# ..                ...       ...     ...    ...  ...     ...      ...     ...     ...    ...        ...        ...
# 683        Aromatisse     Fairy     NaN    462  101      72       72      99      89     29          6      False
# 699           Aurorus      Rock     Ice    521  123      77       72      99      92     58          6      False
# 716           Xerneas     Fairy     NaN    680  126     131       95     131      98     99          6       True
# 717           Yveltal      Dark  Flying    680  126     131       95     131      98     99          6       True
# 718  Zygarde50% Forme    Dragon  Ground    600  108     100      121      81      95     95          6       True

# Attack greater than Defense OR Sp_Atk less than or equal to Sp_Def
print(df_pokemon[(df_pokemon["Attack"] > df_pokemon["Defense"]) | (df_pokemon["Sp_Atk"] <= df_pokemon["Sp_Def"])])
#                    Name   Type_1  Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                  
# 1              Bulbasaur    Grass  Poison    318   45      49       49      65      65     45          1      False
# 2                Ivysaur    Grass  Poison    405   60      62       63      80      80     60          1      False
# 3               Venusaur    Grass  Poison    525   80      82       83     100     100     80          1      False
# 4             Charmander     Fire     NaN    309   39      52       43      60      50     65          1      False
# 5             Charmeleon     Fire     NaN    405   58      64       58      80      65     80          1      False

###############################
##      Combine & and |      ##
###############################

# (Type_1 equal to 'Fire' OR Type_1 equal to 'Water') AND Generation > to '4'
print(df_pokemon[((df_pokemon['Type_1'] == 'Fire') | (df_pokemon['Type_1'] == 'Water')) & (df_pokemon['Generation'] > '4')])
#                         Name Type_1    Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                      
# 498                    Tepig   Fire       NaN    308   65      63       45      45      45     45          5      False
# 499                  Pignite   Fire  Fighting    418   90      93       55      70      55     55          5      False
# 500                   Emboar   Fire  Fighting    528  110     123       65     100      65     65          5      False
# 501                 Oshawott  Water       NaN    308   55      55       45      63      45     45          5      False
# 502                   Dewott  Water       NaN    413   75      75       60      83      60     60          5      False
# 503                 Samurott  Water       NaN    528   95     100       85     108      70     70          5      False


#-------------------------------------------------------------------------------------------------------------#
#---------------------- 4. Using .loc[] for Boolean Filtering within specific columns ------------------------#
#-------------------------------------------------------------------------------------------------------------#

'''df.loc[filter_conditions, columns]'''

# HP less than 30 OR HP greater than 100, only Name, Type_1, Type_2 columns
print(df_pokemon.loc[(df_pokemon['HP'] < 30) | (df_pokemon['HP'] > 100), ["Name", "Type_1", "Type_2"]])
#                  Name    Type_1  Type_2
# #                                      
# 39         Jigglypuff    Normal   Fairy
# 40         Wigglytuff    Normal   Fairy
# 50            Diglett    Ground     NaN
# 63               Abra   Psychic     NaN
# 81          Magnemite  Electric   Steel

# Type_2 not in the list ['Ground', 'Ghost'], only Name, Type_2, Generation columns
print(df_pokemon.loc[~df_pokemon['Type_2'].isin(["Ground", "Ghost"]), ["Name", "Type_2", "Generation"]])
#                       Name  Type_2 Generation
# #                                            
# 1                Bulbasaur  Poison          1
# 2                  Ivysaur  Poison          1
# 3                 Venusaur  Poison          1
# 3    VenusaurMega Venusaur  Poison          1
# 4               Charmander     NaN          1


#-------------------------------------------------------------------------------------------------------------#
#-------------------------------- 5. Using .query() for Boolean Filtering ------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

'''
df.query(expr, inplace=False, **kwargs)
=> Allows filtering a DataFrame using a boolean expression.

Support operators: ==, !=, >, >=, <, <=, &, |, ~, +, -, *, /, //, %, ** and parentheses () for grouping.

If the column name has special characters => put in backticks ``: `variable name` (like SQL style)

Can use @ to reference variables outside the DataFrame like: @variable_name.
'''

######################################
## df.query("condition_expression") ##
######################################

print(df_pokemon.query('HP > 200'))
#         Name  Type_1 Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                    
# 113  Chansey  Normal    NaN    450  250       5        5      35     105     50          1      False
# 242  Blissey  Normal    NaN    540  255      10       10      75     135     55          2      False

print(df_pokemon.query('(Sp_Atk > Attack*2) & (Type_1 == "Psychic")'))
#                       Name   Type_1 Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                  
# 63                    Abra  Psychic    NaN    310  25      20       15     105      55     90          1      False
# 64                 Kadabra  Psychic    NaN    400  40      35       30     120      70    105          1      False
# 65                Alakazam  Psychic    NaN    500  55      50       45     135      95    120          1      False
# 65   AlakazamMega Alakazam  Psychic    NaN    590  55      50       65     175      95    150          1      False
# 122               Mr. Mime  Psychic  Fairy    460  40      45       65     100     120     90          1      False

print(df_pokemon.query('(Speed < 15) | (Speed > 150)'))
#                   Name   Type_1  Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                
# 213            Shuckle      Bug    Rock    505   20      10      230      10     230      5          2      False
# 291            Ninjask      Bug  Flying    456   61      90       45      50      50    160          3      False
# 328           Trapinch   Ground     NaN    290   45     100       45      45      45     10          3      False
# 386  DeoxysSpeed Forme  Psychic     NaN    600   50      95       90      95      90    180          3       True
# 438             Bonsly     Rock     NaN    290   50      80       95      10      45     10          4      False
# 446           Munchlax   Normal     NaN    390  135      85       40      40      85      5          4      False
# 597          Ferroseed    Grass   Steel    305   44      50       91      24      86     10          5      False

######################################
## df.query("colname.str.method()") ##
######################################
'''Same for .dt.method() and .cat.method()'''

print(df_pokemon.query('Name.str.contains("Mega")'))
#                           Name    Type_1    Type_2  Total   HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                           
# 3        VenusaurMega Venusaur     Grass    Poison    625   80     100      123     122     120     80          1      False
# 6    CharizardMega Charizard X      Fire    Dragon    634   78     130      111     130      85    100          1      False
# 6    CharizardMega Charizard Y      Fire    Flying    634   78     104       78     159     115    100          1      False
# 9      BlastoiseMega Blastoise     Water       NaN    630   79     103      120     135     115     78          1      False
# 15       BeedrillMega Beedrill       Bug    Poison    495   65     150       40      15      80    145          1      False

#######################################
## df.query("~condition_expression") ##
#######################################

print(df_pokemon.query('~(`Type_2` == "Flying")'))
#                       Name   Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                                   
# 1                Bulbasaur    Grass  Poison    318  45      49       49      65      65     45          1      False
# 2                  Ivysaur    Grass  Poison    405  60      62       63      80      80     60          1      False
# 3                 Venusaur    Grass  Poison    525  80      82       83     100     100     80          1      False
# 3    VenusaurMega Venusaur    Grass  Poison    625  80     100      123     122     120     80          1      False
# 4               Charmander     Fire     NaN    309  39      52       43      60      50     65          1      False

#########################################
## df.query()[["col_1", "col_2", ...]] ##
#########################################

print(df_pokemon.query('(Speed < 15) | (Speed > 150)')[["Name", "Speed"]])
#                   Name  Speed
# #                            
# 213            Shuckle      5
# 291            Ninjask    160
# 328           Trapinch     10
# 386  DeoxysSpeed Forme    180
# 438             Bonsly     10
# 446           Munchlax      5
# 597          Ferroseed     10

#########################
## Using `column name` ##
#########################

df_pkm_raw = pd.read_csv("05_Pandas_DataR_dataframe/data/pokemon.csv")
print(df_pkm_raw.columns)
# Index(['#', 'Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense',
#        'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary'],
#       dtype='object')

print(df_pkm_raw.query('(`Type 1` == "Fire") & (`Sp. Atk` < 60)')[['Name', 'Type 1', 'Sp. Atk']])
#                         Name Type 1  Sp. Atk
# 42                    Vulpix   Fire       50
# 435                 Chimchar   Fire       58
# 557                    Tepig   Fire       45
# 572                  Pansear   Fire       53
# 614                 Darumaka   Fire       15
# 615  DarmanitanStandard Mode   Fire       30
# 730              Fletchinder   Fire       56

#####################
## Using @variable ##
#####################

atk_threshold = 180

print(df_pokemon.query('Attack >= @atk_threshold')[['Name', 'Attack', "Legendary"]])
#                         Name  Attack  Legendary
# #                                              
# 150      MewtwoMega Mewtwo X     190       True
# 214  HeracrossMega Heracross     185      False
# 383    GroudonPrimal Groudon     180       True
# 384    RayquazaMega Rayquaza     180       True
# 386       DeoxysAttack Forme     180       True

