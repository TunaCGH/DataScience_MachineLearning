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
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Attack, f.Legendary)
    >> dr.slice_head(n=5)
)
#                         Name     Type_1     Type_2  Attack  Legendary
                                                                     
# #                   <object> <category> <category> <int64>     <bool>
# 127        PinsirMega Pinsir        Bug     Flying     155      False
# 130    GyaradosMega Gyarados      Water       Dark     155      False
# 150      MewtwoMega Mewtwo X    Psychic   Fighting     190       True
# 214  HeracrossMega Heracross        Bug   Fighting     185      False
# 248  TyranitarMega Tyranitar       Rock       Dark     164      False

print(
    tb_pokemon
    >> dr.filter_(f.Sp_Atk > f.Attack*2)
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Attack, f.Sp_Atk, f.Legendary)
    >> dr.slice_head(n=5)
)
#                      Name     Type_1     Type_2  Attack  Sp_Atk  Legendary
                                                                          
# #                <object> <category> <category> <int64> <int64>     <bool>
# 63                   Abra    Psychic        NaN      20     105      False
# 64                Kadabra    Psychic        NaN      35     120      False
# 65               Alakazam    Psychic        NaN      50     135      False
# 65  AlakazamMega Alakazam    Psychic        NaN      50     175      False
# 81              Magnemite   Electric      Steel      35      95      False

#-------------
## < (less than)
#-------------

print(
    tb_pokemon
    >> dr.filter_(f.Speed < 15)
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Speed, f.Legendary)
    >> dr.slice_head(n=5)
)
#           Name     Type_1     Type_2   Speed  Legendary
                                                       
# #     <object> <category> <category> <int64>     <bool>
# 213    Shuckle        Bug       Rock       5      False
# 328   Trapinch     Ground        NaN      10      False
# 438     Bonsly       Rock        NaN      10      False
# 446   Munchlax     Normal        NaN       5      False
# 597  Ferroseed      Grass      Steel      10      False

print(
    tb_pokemon
    >> dr.filter_(f.Defense < f.Attack*0.5)
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Attack, f.Defense, f.Legendary)
    >> dr.slice_head(n=5)
)
#                      Name     Type_1     Type_2  Attack  Defense  Legendary
                                                                           
# #                <object> <category> <category> <int64>  <int64>     <bool>
# 15               Beedrill        Bug     Poison      90       40      False
# 15  BeedrillMega Beedrill        Bug     Poison     150       40      False
# 39             Jigglypuff     Normal      Fairy      45       20      False
# 50                Diglett     Ground        NaN      55       25      False
# 56                 Mankey   Fighting        NaN      80       35      False

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
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Defense, f.Legendary)
    >> dr.slice_head(n=5)
)
#                          Name     Type_1     Type_2  Defense  Legendary
                                                                       
# #                    <object> <category> <category>  <int64>     <bool>
# 3       VenusaurMega Venusaur      Grass     Poison      123      False
# 6   CharizardMega Charizard X       Fire     Dragon      111      False
# 9                   Blastoise      Water        NaN      100      False
# 9     BlastoiseMega Blastoise      Water        NaN      120      False
# 28                  Sandslash     Ground        NaN      110      False

#-------------
## == (equal)
#-------------

print(
    tb_pokemon
    >> dr.filter_(f.Type_1 == 'Fire')
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_head(n=5)
)
#                         Name     Type_1     Type_2   Total  Legendary
                                                                     
# #                   <object> <category> <category> <int64>     <bool>
# 4                 Charmander       Fire        NaN     309      False
# 5                 Charmeleon       Fire        NaN     405      False
# 6                  Charizard       Fire     Flying     534      False
# 6  CharizardMega Charizard X       Fire     Dragon     634      False
# 6  CharizardMega Charizard Y       Fire     Flying     634      False

#-------------
## != (not equal)
#-------------

print(
    tb_pokemon
    >> dr.filter_(f.Type_1 != 'Fire')
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_head(n=5)
)
#                     Name     Type_1     Type_2   Total  Legendary
                                                                 
# #               <object> <category> <category> <int64>     <bool>
# 1              Bulbasaur      Grass     Poison     318      False
# 2                Ivysaur      Grass     Poison     405      False
# 3               Venusaur      Grass     Poison     525      False
# 3  VenusaurMega Venusaur      Grass     Poison     625      False
# 7               Squirtle      Water        NaN     314      False

##############################
##          .isin()         ##
##############################

print(
    tb_pokemon
    >> dr.filter_(f.Type_1.isin(['Fire', 'Water'])) # Type_1 in the list ['Fire', 'Water']
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_tail(n=5)
)
#           Name     Type_1     Type_2   Total  Legendary
                                                       
# #     <object> <category> <category> <int64>     <bool>
# 667     Litleo       Fire     Normal     369      False
# 668     Pyroar       Fire     Normal     507      False
# 692  Clauncher      Water        NaN     330      False
# 693  Clawitzer      Water        NaN     500      False
# 721  Volcanion       Fire      Water     600       True

print(
    tb_pokemon
    >> dr.filter_(f.Generation.isin(['4', '6'])) # Generation in the list ['4', '6']
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Generation, f.Legendary)
)
#                     Name     Type_1     Type_2   Total Generation  Legendary
                                                                            
# #               <object> <category> <category> <int64> <category>     <bool>
# 387              Turtwig      Grass        NaN     318          4      False
# 388               Grotle      Grass        NaN     405          4      False
# 389             Torterra      Grass     Ground     525          4      False
# 390             Chimchar       Fire        NaN     309          4      False
# ..                   ...        ...        ...     ...        ...        ...
# 391             Monferno       Fire   Fighting     405          4      False
# 719              Diancie       Rock      Fairy     600          6       True
# 719  DiancieMega Diancie       Rock      Fairy     700          6       True
# 720  HoopaHoopa Confined    Psychic      Ghost     600          6       True
# 720   HoopaHoopa Unbound    Psychic       Dark     680          6       True
# 721            Volcanion       Fire      Water     600          6       True

##############################
##      String Boolean      ##
##############################

print(
    tb_pokemon
    >> dr.filter_(f.Name.str.contains('Mega')) # Name contains the substring 'Mega'
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_head(n=5)
)
#                          Name     Type_1     Type_2   Total  Legendary
                                                                      
# #                    <object> <category> <category> <int64>     <bool>
# 3       VenusaurMega Venusaur      Grass     Poison     625      False
# 6   CharizardMega Charizard X       Fire     Dragon     634      False
# 6   CharizardMega Charizard Y       Fire     Flying     634      False
# 9     BlastoiseMega Blastoise      Water        NaN     630      False
# 15      BeedrillMega Beedrill        Bug     Poison     495      False

print(
    tb_pokemon
    >> dr.filter_(f.Name.str.startswith('Tor')) # Name starts with the substring 'Tor'
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_head(n=5)
)
#                         Name     Type_1     Type_2   Total  Legendary
                                                                     
# #                   <object> <category> <category> <int64>     <bool>
# 255                  Torchic       Fire        NaN     310      False
# 324                  Torkoal       Fire        NaN     470      False
# 389                 Torterra      Grass     Ground     525      False
# 641  TornadusIncarnate Forme     Flying        NaN     580       True
# 641    TornadusTherian Forme     Flying        NaN     580       True

print(
    tb_pokemon
    >> dr.filter_(f.Name.str.endswith('ite')) # Name ends with the substring 'ite'
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_head(n=5)
)
#           Name     Type_1     Type_2   Total  Legendary
                                                       
# #     <object> <category> <category> <int64>     <bool>
# 81   Magnemite   Electric      Steel     325      False
# 149  Dragonite     Dragon     Flying     600      False
# 307   Meditite   Fighting    Psychic     280      False
# 444     Gabite     Dragon     Ground     410      False
# 499    Pignite       Fire   Fighting     418      False

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
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_head(n=5)
)
#                     Name     Type_1     Type_2   Total  Legendary
                                                                 
# #               <object> <category> <category> <int64>     <bool>
# 1              Bulbasaur      Grass     Poison     318      False
# 2                Ivysaur      Grass     Poison     405      False
# 3               Venusaur      Grass     Poison     525      False
# 3  VenusaurMega Venusaur      Grass     Poison     625      False
# 7               Squirtle      Water        NaN     314      False

print(
    tb_pokemon
    >> dr.filter_(~f.Type_2.isin(['Flying', 'Dragon'])) # Type_2 not in the list ['Flying', 'Dragon']
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
    >> dr.slice_head(n=5)
)
#                     Name     Type_1     Type_2   Total  Legendary
                                                                 
# #               <object> <category> <category> <int64>     <bool>
# 1              Bulbasaur      Grass     Poison     318      False
# 2                Ivysaur      Grass     Poison     405      False
# 3               Venusaur      Grass     Poison     525      False
# 3  VenusaurMega Venusaur      Grass     Poison     625      False
# 4             Charmander       Fire        NaN     309      False


#-------------------------------------------------------------------------------------------------------------#
#---------------------------- 3. Combine Multiple Conditions: & (and), | (or) --------------------------------#
#-------------------------------------------------------------------------------------------------------------#

##########################
##       & (and)        ##
##########################
'''True if only all the conditions (clauses) are True.'''

print(
    tb_pokemon
    >> dr.filter_((f.Type_1 == 'Fire') & (f.Attack > 100)) # Type_1 equal to 'Fire' AND Attack greater than 100
    >> dr.select(f.Name, f.Type_1, f.Attack)
    >> dr.slice_head(n=5)
)
#                           Name     Type_1  Attack
                                                 
# #                     <object> <category> <int64>
# 6    CharizardMega Charizard X       Fire     130
# 6    CharizardMega Charizard Y       Fire     104
# 59                    Arcanine       Fire     110
# 136                    Flareon       Fire     130
# 244                      Entei       Fire     115

print(
    tb_pokemon
    >> dr.filter_((f.Type_1 == 'Fire') & (f.Attack > 100) & (f.Generation == "5"))
    >> dr.select(f.Name, f.Type_1, f.Attack, f.Generation, f.Legendary)
    >> dr.slice_head(n=5)
)
#                         Name     Type_1  Attack Generation  Legendary
                                                                     
# #                   <object> <category> <int64> <category>     <bool>
# 500                   Emboar       Fire     123          5      False
# 555  DarmanitanStandard Mode       Fire     140          5      False

###########################
##       | (or)          ##
###########################
'''False if only all the conditions (clauses) are False.'''

print(
    tb_pokemon
    >> dr.filter_((f.Type_1 == 'Fire') | (f.Type_1 == 'Water')) # Type_1 equal to 'Fire' OR Type_1 equal to 'Water'
    >> dr.select(f.Name, f.Type_1, f.Type_2, f.Total, f.Legendary)
)
#                           Name     Type_1     Type_2   Total  Legendary
                                                                       
# #                     <object> <category> <category> <int64>     <bool>
# 4                   Charmander       Fire        NaN     309      False
# 5                   Charmeleon       Fire        NaN     405      False
# 6                    Charizard       Fire     Flying     534      False
# 6    CharizardMega Charizard X       Fire     Dragon     634      False
# ..                         ...        ...        ...     ...        ...
# 6    CharizardMega Charizard Y       Fire     Flying     634      False
# 667                     Litleo       Fire     Normal     369      False
# 668                     Pyroar       Fire     Normal     507      False
# 692                  Clauncher      Water        NaN     330      False
# 693                  Clawitzer      Water        NaN     500      False
# 721                  Volcanion       Fire      Water     600       True

print(
    tb_pokemon
    >> dr.filter_((f.Attack > f.Defense) | (f.Sp_Atk <= f.Sp_Def))
    >> dr.select(f.Name, f.Attack, f.Defense, f.Sp_Atk, f.Sp_Def)
    >> dr.slice_head(n=5)
)
#          Name  Attack  Defense  Sp_Atk  Sp_Def
                                              
# #    <object> <int64>  <int64> <int64> <int64>
# 1   Bulbasaur      49       49      65      65
# 2     Ivysaur      62       63      80      80
# 3    Venusaur      82       83     100     100
# 4  Charmander      52       43      60      50
# 5  Charmeleon      64       58      80      65

###############################
##      Combine & and |      ##
###############################

print(
    tb_pokemon
    >> dr.filter_(
        ((f.Type_1 == 'Fire') | (f.Type_1 == 'Water')) & (f.Attack > 100)
    ) # (Type_1 equal to 'Fire' OR Type_1 equal to 'Water') AND Attack greater than 100
    >> dr.select(f.Name, f.Type_1, f.Attack, f.Legendary)
    >> dr.slice_head(n=5)
)
#                          Name     Type_1  Attack  Legendary
                                                           
# #                    <object> <category> <int64>     <bool>
# 6   CharizardMega Charizard X       Fire     130      False
# 6   CharizardMega Charizard Y       Fire     104      False
# 9     BlastoiseMega Blastoise      Water     103      False
# 59                   Arcanine       Fire     110      False
# 98                     Krabby      Water     105      False


#-------------------------------------------------------------------------------------------------------------#
#--------------------------- 4. Columns with "bad" names: using f["col name"] --------------------------------#
#-------------------------------------------------------------------------------------------------------------#

tb_lifexp = dr.tibble(
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/life_expectancy.csv"
    )
)

print(tb_lifexp.columns)
# Index(['Country', 'Year', 'Status', 'Life expectancy ', 'Adult Mortality',
#        'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
#        'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',
#        'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
#        ' thinness  1-19 years', ' thinness 5-9 years',
#        'Income composition of resources', 'Schooling'],
#       dtype='object')

#############################################
## Using f['col name'] for bad column name ##
#############################################

print(
    tb_lifexp
    >> dr.filter_((f['Life expectancy '] > 80) & (f[' thinness 5-9 years'] <= 2) & (f.Year == 2015))
    >> dr.select(f.Country, f.Year, f['Life expectancy '], f[' thinness 5-9 years'])
    >> dr.slice_head(n=5)
)
#        Country    Year  Life expectancy    thinness 5-9 years
#       <object> <int64>         <float64>            <float64>
# 112  Australia    2015              82.8                  0.6
# 240    Belgium    2015              81.1                  1.0
# 496     Canada    2015              82.2                  0.5
# 544      Chile    2015              85.0                  0.8
# 673     Cyprus    2015              85.0                  1.0