'''
The pandas.Series.str accessor provides vectorized string operations 
for Series and Index objects containing string data. 

It's one of pandas' most powerful features for text processing, 
offering over 50 methods that mirror Python's built-in string methods 
while handling missing values automatically and operating efficiently on entire Series at once.


Flow of contents:

0. pandas.Series.str accessor: transform to string type (like .astype(str))

1. Slicing and Indexing:
   - .slice(start, stop, step)
   - .slice_replace(start, stop, repl)
   - .get(index)

2. Basic Transformations:
   - Case transformations: .lower(), .upper(), .title(), .capitalize(), .swapcase()
   - Information retrieval: .len(), .count(pattern)
   - Stripping: .strip(), .lstrip(), .rstrip()

3. Checking methods (Boolean returns):
   - Character type checks: .isalpha(), .isdigit(), .isalnum(), .isnumeric(), .isspace()
   - Case checks: .isupper(), .islower(), .istitle()
   - Pattern checks: .startswith(prefix), .endswith(suffix), .contains(pattern)

4. Splitting:
   - .split(delimiter)
   - .rsplit(delimiter)
   - .partition(separator)
   - .rpartition(separator)
   
5. Joinning: .join(delimiter)

6. Replacement, Removal, Repeat, Wrap:
   - .replace(old, new)
   - .removeprefix(prefix)
   - .removesuffix(suffix)
   - .repeat(n)
   - .wrap(width)

7. RegEx, Matching, Finding, Extracting:
   - Matching: .match(pattern), .fullmatch(pattern), .contains(pattern, regex=True)
   - Finding: .find(pattern), .rfind(pattern), .findall(pattern), .index(pattern), .rindex(pattern)
   - Extracting: .extract(pattern), .extractall(pattern)

8. Concatenation: .cat(others=None, sep='', na_rep=None)

9. Padding and Alignment:
   - Padding: .pad(width, side='left', fillchar=' ')
   - Alignment: .ljust(), .rjust(), .center()
   - Zero-fill: .zfill(width)

10. Categorical Encoding: .get_dummies()

11. Unicode and Encoding:
    - .normalize(form='NFC')
    - .encode(encoding='utf-8', errors='strict')
    - .decode(encoding='utf-8', errors='strict')

12. Real applications:
    - Data cleaning
    - Email processing
'''

import pandas as pd


#---------------------------------------------------------------------------------------------------------#
#--------------------------------------- 12. Real applications -------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

###################
## Data cleaning ##
###################

# Clean messy name data
messy_names = pd.Series(['  john doe  ', 'JANE SMITH', 'bob-johnson'])
clean_names = (messy_names
               .str.strip()
               .str.replace('-', ' ')
               .str.title()
               .str.replace(r'\s+', ' ', regex=True))


######################
## Email processing ##
######################

emails = pd.Series(['user@example.com', 'ADMIN@SITE.ORG', 'invalid.email'])
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validate and extract components
is_valid = emails.str.match(email_pattern)
domains = emails.str.extract(r'@([^.]+\..*)')
usernames = emails.str.extract(r'^([^@]+)@')
