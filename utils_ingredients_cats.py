# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:37:52 2022

@author: siddh
"""
import re
def ingredients_initial_cleaning_cat_wet(ingredients_column):
    '''This function will do the initial cleaning of noises for ingredients column before the ingredients panel
    is split out for different flavors.
    Parameters: ingredients_column - The unprocessed ingredients column from the data
    Returns: A list of lists of cleaned and flavour wise split out ingredients'''
    
    # Get ingredients into a list of strings
    # ingredients_column = ingredients_column
    
    # ingredients_column = []
    # ingredients_column.append(ingredients_str)
    ingredients_list=list(ingredients_column)
    ingredients_list=[str(i) for i in ingredients_list]
    
    # Removing the caloric content from ingredients string
#     ingredients_only=[i.split('caloric content')[0] for i in ingredients_list]
    
    # Some products have ingredients listed in two categories - Original and New
    # The below code will remove the original list and keep only the new list of ingredients
    #ingredients_only=[i for i in ingredients_only if str(i)!='nan']
    ingredients_only=[i.split('original:')[0] for i in ingredients_list]
    ingredients_only=[i.replace('new:', '') for i in ingredients_only]
    ingredients_only=[i.replace('animal fat, (source of omega 6 fatty acids [preserved with bha/citric acid])',
                                'animal fat (preserved with citric acid)') for i in ingredients_only]
    
    ingredients_only=[i.replace('essential nutrients and other ingredients:', ',') for i in ingredients_only]
    ingredients_only=[i.replace('(filtered) water', 'water') for i in ingredients_only]
    ingredients_only=[i.replace('beef meat', 'beef') for i in ingredients_only]
    ingredients_only=[i.replace('chicken (boneless, skinless breast)',
                                'boneless skinless chicken breast') for i in ingredients_only]
    ingredients_only=[i.replace('duck (boneless, skinless, breast)',
                                'boneless skinless duck breast') for i in ingredients_only]
    ingredients_only=[i.replace('calcium iodate and sodium selenite',
                                'calcium iodate, sodium selenite') for i in ingredients_only]
    ingredients_only=[i.replace('carrots tomato concentrate',
                                'carrots, tomato concentrate') for i in ingredients_only]
    ingredients_only=[i.replace('chicken 76%',
                                'chicken') for i in ingredients_only]
    ingredients_only=[i.replace('potassium, chloride',
                                'potassium chloride') for i in ingredients_only]
    ingredients_only=[i.replace('choline chloride parsley.',
                                'choline chloride, parsley') for i in ingredients_only]
    ingredients_only=[i.replace('copper glycine, complex',
                                'copper glycine complex') for i in ingredients_only]
    ingredients_only=[i.replace('menadione sodium bisulfite, complex',
                                'menadione sodium bisulfite complex') for i in ingredients_only]
    ingredients_only=[i.replace('cranberries coconut.',
                                'cranberries, coconut') for i in ingredients_only]
    ingredients_only=[i.replace('fish oil (preserved with mixed tocopherols) dl-methionine',
                                'fish oil (preserved with mixed tocopherols), dl-methionine') for i in ingredients_only]
    ingredients_only=[i.replace('folic acid) inulin',
                                'folic acid), inulin') for i in ingredients_only]
    ingredients_only=[i.replace('folic acid. water added for processing',
                                'folic acid, water added for processing') for i in ingredients_only]
    ingredients_only=[i.replace('guar gum     sweet potatoes',
                                'guar gum, sweet potatoes') for i in ingredients_only]
    ingredients_only=[i.replace('icelandic fish (cod, haddock, pollock, monkfish, lumpfish, plaice)',
                                'icelandic fish') for i in ingredients_only]
    ingredients_only=[i.replace('manganese proteinate ethylenediamine dihydriodide',
                                'manganese proteinate, ethylenediamine dihydroiodide') for i in ingredients_only]
    ingredients_only=[i.replace('menadione, sodium',
                                'menadione sodium') for i in ingredients_only]
    ingredients_only=[i.replace('menhaden fish oil (preserved with mixed tocopherols) magnesium sulfate',
                                'menhaden fish oil (preserved with mixed tocopherols), magnesium sulfate') for i in ingredients_only]
    ingredients_only=[i.replace(', no carrageenan, no guar gum and no xanthan gum.',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace("pea starch\xa0 brewer's dried yeast",
                                "pea starch, brewer's dried yeast") for i in ingredients_only]
    ingredients_only=[i.replace("potassium iodide) calcium carbonate",
                                "potassium iodide, calcium carbonate") for i in ingredients_only]
    ingredients_only=[i.replace("potassium iodide) sodium carbonate",
                                "potassium iodide, sodium carbonate") for i in ingredients_only]
    ingredients_only=[i.replace("potassium iodide) sodium carbonate",
                                "potassium iodide, sodium carbonate") for i in ingredients_only]
    ingredients_only=[i.replace("potassium iodide] xanthan gum",
                                "potassium iodide, xanthan gum") for i in ingredients_only]
    ingredients_only=[i.replace("potassium iodide)] xanthan gum",
                                "potassium iodide, xanthan gum") for i in ingredients_only]
    ingredients_only=[i.replace("preserved with mixed tocopherols. vitamin b5",
                                "vitamin b5") for i in ingredients_only]
    ingredients_only=[i.replace("pyfidoxine hydrochloride (vitamin b6)",
                                "pyridoxine hydrochloride (source of vitamin b6)") for i in ingredients_only]
    ingredients_only=[i.replace("rosemary extract. sodium selenite",
                                "sodium selenite") for i in ingredients_only]
    ingredients_only=[i.replace("salmon oil (preserved with mixed tocopherols) choline chloride",
                                "salmon oil (preserved with mixed tocopherols), choline chloride") for i in ingredients_only]
    ingredients_only=[i.replace("salmon oil (preserved with mixed tocopherols) potassium chloride",
                                "salmon oil (preserved with mixed tocopherols), potassium chloride") for i in ingredients_only]
    ingredients_only=[i.replace("sodium selenite) choline chloride",
                                "sodium selenite), choline chloride") for i in ingredients_only]
    ingredients_only=[i.replace("sodium selenite manganese proteinate",
                                "sodium selenite, manganese proteinate") for i in ingredients_only]
    ingredients_only=[i.replace("sodium selenite riboflavin supplement",
                                "sodium selenite, riboflavin supplement") for i in ingredients_only]
    ingredients_only=[i.replace("vitamin  d3, supplement",
                                "vitamin  d3 supplement") for i in ingredients_only]
    ingredients_only=[i.replace("vitamin a supplement biotin vitamin d3 supplement",
                                "vitamin a supplement, biotin, vitamin d3 supplement") for i in ingredients_only]
    ingredients_only=[i.replace("vitamin b12 supplement manganese proteinate",
                                "vitamin b12 supplement, manganese proteinate") for i in ingredients_only]
    ingredients_only=[i.replace("vitamin b12 supplement. menadione sodium bisulfite",
                                "vitamin b12 supplement, menadione sodium bisulfite") for i in ingredients_only]
    ingredients_only=[i.replace("vitamin b12. calcium iodate",
                                "vitamin b12, calcium iodate") for i in ingredients_only]
    
    ingredients_only=[i.replace("vitamin d3 supplement) inulin",
                                "vitamin d3 supplement), inulin") for i in ingredients_only]
    ingredients_only=[i.replace("vitamin d3 supplement) blueberries",
                                "vitamin d3 supplement), blueberries") for i in ingredients_only]
    ingredients_only=[i.replace("water sufficient for processing 24%",
                                "water sufficient for processing") for i in ingredients_only]
    
    ingredients_only=[i.replace("water sufficient forprocessing",
                                "water sufficient for processing") for i in ingredients_only]
    ingredients_only=[i.replace("postassium",
                                "potassium") for i in ingredients_only]
    ingredients_only=[i.replace("sunflower oi,",
                                "sunflower oil,") for i in ingredients_only]
    
    
   
    # Cleaning other noises in ingredients list specific to the  data
    # These specific noises can vary from dataset to dataset and 
    # needs to be looked into before executing them 
    #ingredients_only=[i.replace('Ingredients\n                        \n                                ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('\n                        ', '') for i in ingredients_only]
    ingredients_only=[i.replace('         meal', '') for i in ingredients_only]
    #ingredients_only=[i.replace('   A-2569', ' A-2569') for i in ingredients_only]
    #ingredients_only=[i.replace('\n', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\xa0', ' ') for i in ingredients_only]
    #ingredients_only=[i.replace('ESSENTIAL NUTRIENTS AND OTHER INGREDIENTS: ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('        Inactive Ingredients: Disodium Edta', ' Inactive Ingredients: Disodium Edta') for i in ingredients_only]
    ingredients_only=[each.replace(', (', ' (').strip() for each in ingredients_only]
#     ingredients_only=[i.replace(';', '\n') for i in ingredients_only]
    ingredients_only=[i.replace(' ,', ',') for i in ingredients_only]
    ingredients_only=[i.replace('*(official name is marine microalgae)', '') for i in ingredients_only]
    ingredients_only=[i.replace('\u200btrout', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('?', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\u202f', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\t', ',') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    ingredients_only=[i.replace('. b470920-5', '') for i in ingredients_only]
    
    #ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
    # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
    # We remove such key terms to get the actual name of ingredients
    ingredients_only=[i.replace(' minerals', ',') for i in ingredients_only]
    ingredients_only=[i.replace(' vitamins', ',') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace(':', '') for i in ingredients_only]
    ingredients_only=[i.replace('"', '') for i in ingredients_only]
    ingredients_only=[i.replace('processing.', 'processing,') for i in ingredients_only]
    #ingredients_only=[i.replace('MINERALS', ' ') for i in ingredients_only]
    
    # Some other specific scenarios based on the data. 
    # This was identified while making the dictionary to standardize the name of ingredients
    #ingredients_only=[i for i in ingredients_only if i!='']
    #ingredients_only=[i.replace('Preserved With Mixed Tocopherols And Citric Acid', 'Preserved With Mixed Tocopherols, And Citric Acid') for i in ingredients_only]
    #ingredients_only=[i.replace('Mixed Tocopherols and Citric Acid (Preservatives)', 'Mixed Tocopherols (preservative), and Citric Acid (Preservative)') for i in ingredients_only]
    
    # Removing multiple whitespaces and new lines
    ingredients_only=[re.sub(' +', ' ', each) for each in ingredients_only]
    ingredients_only=[re.sub(r'\n+', '\n', each) for each in ingredients_only]
    ingredients_only=[i.strip() for i in ingredients_only]
    ingredients_only=[each.replace('riboflavin supplement vitamin,', 'riboflavin supplement, vitamin') for each in ingredients_only]
    
    ingredients_only=[each.replace('vitamin e, a, d3, b12 supplements,', 'vitamin e, vitamin a, vitamin d3, vitamin b12,') for each in ingredients_only]
    ingredients_only=[each.replace('folic acid inulin', 'folic acid, inulin') for each in ingredients_only]
    ingredients_only=[each.replace('(boneless, skinless breast)', '') for each in ingredients_only]
    ingredients_only=[each.replace('�', '') for each in ingredients_only]
    ingredients_only=[each.replace('ingredients', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('\n', ' ').strip() for each in ingredients_only]
    ingredients_only=[each.replace(',,', ',').strip() for each in ingredients_only]
    ingredients_only=[each.replace('[', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace(']', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('))', ')').strip() for each in ingredients_only]
    ingredients_only=[each.replace(') water sufficient for processing',
                                   '), water sufficient for processing').strip() for each in ingredients_only]
    ingredients_only=[each.replace('}', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('{', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('minerals', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('vitamins', '').strip() for each in ingredients_only]
#     ingredients_only=[each.replace(', (vitamin', ' (vitamin').strip() for each in ingredients_only]
    
    
    
    ingredients_only=[re.sub(' +', ' ', each) for each in ingredients_only]
#     ingredients_only=[re.sub('', 'nan', each) for each in ingredients_only]
#     ingredients_only=[i.replace(" and ", ", ") for i in ingredients_only]
    # Tokenized ingredients in a list of list format
    tokenized_ingredients_nested=[[ingredient.strip() for ingredient in each.split(',')] for each in ingredients_only]
    
    # Inconsistent use of the parantheses in the data is to be removed.
    new_tokenized_ingredients_nested=[]
    
    for ingredients in tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if '(' in each and ')' not in each:
                s=each.replace('(', '')
                ingredients_tokenized.append(s)
            elif ')' in each and '(' not in each:
                s=each.replace(')', '')
                ingredients_tokenized.append(s)
            else:
                ingredients_tokenized.append(each)
        new_tokenized_ingredients_nested.append(ingredients_tokenized)
        
    # Removing the unnecessary trailing fullstops and leading colons
    new_ingredients=[]

    for ingredients in new_tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)!=0 and each[-1]=='.':
                item=each[:-1].strip()
                ingredients_tokenized.append(item)
            elif len(each)!=0 and each[0]==':':
                item=each[2:].strip()
                ingredients_tokenized.append(item)
            else:
                ingredients_tokenized.append(each)
        new_ingredients.append(ingredients_tokenized)
        
    # Removing the 'ID' like text in the end of ingredients
    # In some places, the ingredients contained text that was unidentifiable.
    # For example, *Blue 2. N450118*. The *Blue 2* is a color here but the text after it is meaningless
    # Hence the below code removes such texts in the data.
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]
    new_ingredients_split      
    
    new_ingredients_2=[]
    for ingredients in new_ingredients_split:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)==2:
                if len(each[1])==8 or len(each[1])==7:
                    ingredients_tokenized.append(each[0].strip())
                else:
                    ingredients_tokenized.append(each)
            else:
                ingredients_tokenized.append(each)
        new_ingredients_2.append(ingredients_tokenized)
        
    # Joining again with fullstops as that was the separator for splitting for previous step
    new_product_wise_ingredients=[]
    for ingredient in new_ingredients_2:
        ingredients=[]
        for each in ingredient:
            if type(each)==list:
                ingredients.append(('.').join(each).lower().strip())
            else:
                ingredients.append(each.lower().strip())
        new_product_wise_ingredients.append(ingredients)
    return new_product_wise_ingredients
    
    #ingredients_only=[re.sub(r") [a-z]", r"), [a-z]", each) for each in ingredients_only]
    
    #ingredients_only=[each.replace(', (', '(') for each in ingredients_only]
    
    # This step is to take care of random newline characters between any ingredients
    
#     ingredients_only_final_2=[]
#     for i, each in enumerate(ingredients_only_final):
#         if ':' not in each and '\n' in each:
#             ingredients_only_final_2.append(each.replace('\n', ''))
#         else:
#             ingredients_only_final_2.append(each)
            
    # Splitting the ingredients column by \n to get the ingredients panel for different products in combos or variety packs
#     ingredients_only_split_for_combo_products_raw=[each.split('\n') for each in ingredients_only_final_2]
    
#     # Removing the 'Ingredients' word from ingredients panel
#     ingredients_only_split_for_combo_products=[]
#     for each in ingredients_only_split_for_combo_products_raw:
#         temp_list=[]
#         for s in each:
#             new_s=s.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}')
#             temp_list.append(new_s)
#         ingredients_only_split_for_combo_products.append(temp_list)
    
#     # removing empty nested lists
#     ingredients_only_split_for_combo_products_final=[[a for a in each if len(a)>0] for each in ingredients_only_split_for_combo_products]
#     return ingredients_only_split_for_combo_products_final


def ingredients_initial_cleaning_cat_vet(ingredients_column):
    '''This function will do the initial cleaning of noises for ingredients column before the ingredients panel
    is split out for different flavors.
    Parameters: ingredients_column - The unprocessed ingredients column from the data
    Returns: A list of lists of cleaned and flavour wise split out ingredients'''

    # Get ingredients into a list of strings
    ingredients_list=list(ingredients_column)
    ingredients_list=[str(i) for i in ingredients_list]
    
    # Removing the caloric content from ingredients string
    ingredients_only=[i.split('caloric content')[0] for i in ingredients_list]
    
    # Some products have ingredients listed in two categories - Original and New
    # The below code will remove the original list and keep only the new list of ingredients
    #ingredients_only=[i for i in ingredients_only if str(i)!='nan']
    ingredients_only=[i.split('original:')[0] for i in ingredients_only]
    ingredients_only=[i.replace('new:', '') for i in ingredients_only]
    
    # Cleaning other noises in ingredients list specific to the  data
    # These specific noises can vary from dataset to dataset and 
    # needs to be looked into before executing them 
    #ingredients_only=[i.replace('Ingredients\n                        \n                                ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('\n                        ', '') for i in ingredients_only]
    ingredients_only=[i.replace('         meal', '') for i in ingredients_only]
    #ingredients_only=[i.replace('   A-2569', ' A-2569') for i in ingredients_only]
    #ingredients_only=[i.replace('\n', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\xa0', ' ') for i in ingredients_only]
    #ingredients_only=[i.replace('ESSENTIAL NUTRIENTS AND OTHER INGREDIENTS: ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('        Inactive Ingredients: Disodium Edta', ' Inactive Ingredients: Disodium Edta') for i in ingredients_only]
    ingredients_only=[i.replace(';', '\n') for i in ingredients_only]
    ingredients_only=[i.replace(' ,', ',') for i in ingredients_only]
    ingredients_only=[i.replace('*(official name is marine microalgae)', '') for i in ingredients_only]
    ingredients_only=[i.replace('\u200btrout', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('?', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\u202f', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\t', ',') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    ingredients_only=[i.replace(', preserved with mixed tocopherols and citric acid', ', preserved with mixed tocopherols, and citric acid') for i in ingredients_only]
    ingredients_only=[i.replace('>', '') for i in ingredients_only]
    ingredients_only=[i.replace('<', '') for i in ingredients_only]
    ingredients_only=[i.replace('trace', '') for i in ingredients_only]
    #ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
    # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
    # We remove such key terms to get the actual name of ingredients
    ingredients_only=[i.replace(' minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace(' vitamins', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    #ingredients_only=[i.replace('MINERALS', ' ') for i in ingredients_only]
    
    # Some other specific scenarios based on the data. 
    # This was identified while making the dictionary to standardize the name of ingredients
    #ingredients_only=[i for i in ingredients_only if i!='']
    #ingredients_only=[i.replace('Preserved With Mixed Tocopherols And Citric Acid', 'Preserved With Mixed Tocopherols, And Citric Acid') for i in ingredients_only]
    #ingredients_only=[i.replace('Mixed Tocopherols and Citric Acid (Preservatives)', 'Mixed Tocopherols (preservative), and Citric Acid (Preservative)') for i in ingredients_only]
    
    # Removing multiple whitespaces and new lines
    ingredients_only=[re.sub(' +', ' ', each) for each in ingredients_only]
    ingredients_only=[re.sub(r'\n+', '\n', each) for each in ingredients_only]
    ingredients_only=[i.strip() for i in ingredients_only]
    
    # Splitting the ingredients column by \n to get the ingredients panel for different products in combos or variety packs
    # ingredients_only_split_for_combo_products_raw=[each.split('\n') for each in ingredients_only]
    
    # # Removing the 'Ingredients' word from ingredients panel
    # ingredients_only_split_for_combo_products=[]
    # for each in ingredients_only_split_for_combo_products_raw:
    #     temp_list=[]
    #     for s in each:
    #         new_s=s.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}')
    #         temp_list.append(new_s)
    #     ingredients_only_split_for_combo_ products.append(temp_list)
    
    # # removing empty nested lists
    # ingredients_only_split_for_combo_products_final=[[a for a in each if len(a)>0] for each in ingredients_only_split_for_combo_products]
    # return ingredients_only_split_for_combo_products_final

    tokenized_ingredients_nested=[[ingredient.strip() for ingredient in each.split(',')] for each in ingredients_only]
    
    # Inconsistent use of the parantheses in the data is to be removed.
    new_tokenized_ingredients_nested=[]
    
    for ingredients in tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if '(' in each and ')' not in each:
                s=each.replace('(', '')
                ingredients_tokenized.append(s)
            elif ')' in each and '(' not in each:
                s=each.replace(')', '')
                ingredients_tokenized.append(s)
            else:
                ingredients_tokenized.append(each)
        new_tokenized_ingredients_nested.append(ingredients_tokenized)
        
    # Removing the unnecessary trailing fullstops and leading colons
    new_ingredients=[]

    for ingredients in new_tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if each[-1]=='.':
                item=each[:-1]
                ingredients_tokenized.append(item)
            elif each[0]==':':
                item=each[2:]
                ingredients_tokenized.append(item)
            else:
                ingredients_tokenized.append(each)
        new_ingredients.append(ingredients_tokenized)
        
    # Removing the 'ID' like text in the end of ingredients
    # In some places, the ingredients contained text that was unidentifiable.
    # For example, *Blue 2. N450118*. The *Blue 2* is a color here but the text after it is meaningless
    # Hence the below code removes such texts in the data.
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]
    new_ingredients_split      
    
    new_ingredients_2=[]
    for ingredients in new_ingredients_split:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)==2:
                if len(each[1])==8 or len(each[1])==7:
                    ingredients_tokenized.append(each[0])
                else:
                    ingredients_tokenized.append(each)
            else:
                ingredients_tokenized.append(each)
        new_ingredients_2.append(ingredients_tokenized)
        
    # Joining again with fullstops as that was the separator for splitting for previous step
    new_product_wise_ingredients=[]
    for ingredient in new_ingredients_2:
        ingredients=[]
        for each in ingredient:
            if type(each)==list:
                ingredients.append(('.').join(each).lower())
            else:
                ingredients.append(each.lower())
        new_product_wise_ingredients.append(ingredients)
    return new_product_wise_ingredients

def ingredients_initial_cleaning_cat_raw(ingredients_column):
    '''This function will do the initial cleaning of noises for ingredients column before the ingredients panel
    is split out for different flavors.
    Parameters: ingredients_column - The unprocessed ingredients column from the data
    Returns: A list of lists of cleaned and flavour wise split out ingredients'''
    
    # Get ingredients into a list of strings
    ingredients_list=list(ingredients_column)
    ingredients_list=[str(i) for i in ingredients_list]
    
    # Removing the caloric content from ingredients string
    ingredients_only=[i.split('caloric content')[0] for i in ingredients_list]
    
    # Some products have ingredients listed in two categories - Original and New
    # The below code will remove the original list and keep only the new list of ingredients
    #ingredients_only=[i for i in ingredients_only if str(i)!='nan']
    ingredients_only=[i.split('original:')[0] for i in ingredients_only]
    ingredients_only=[i.replace('new:', '') for i in ingredients_only]
    
    # Cleaning other noises in ingredients list specific to the  data
    # These specific noises can vary from dataset to dataset and 
    # needs to be looked into before executing them 
    #ingredients_only=[i.replace('Ingredients\n                        \n                                ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('\n                        ', '') for i in ingredients_only]
    ingredients_only=[i.replace('         meal', '') for i in ingredients_only]
    #ingredients_only=[i.replace('   A-2569', ' A-2569') for i in ingredients_only]
    #ingredients_only=[i.replace('\n', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\xa0', ' ') for i in ingredients_only]
    #ingredients_only=[i.replace('ESSENTIAL NUTRIENTS AND OTHER INGREDIENTS: ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('        Inactive Ingredients: Disodium Edta', ' Inactive Ingredients: Disodium Edta') for i in ingredients_only]
    ingredients_only=[i.replace(';', '\n') for i in ingredients_only]
    ingredients_only=[i.replace(' ,', ',') for i in ingredients_only]
    ingredients_only=[i.replace('*(official name is marine microalgae)', '') for i in ingredients_only]
    ingredients_only=[i.replace('\u200btrout', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('?', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\u202f', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\t', ',') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    #ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
    # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
    # We remove such key terms to get the actual name of ingredients
    ingredients_only=[i.replace(' minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace(' vitamins', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace('sa�ower oil', 'safflower oil') for i in ingredients_only]
    ingredients_only=[i.replace('boneless, skinless', 'boneless skinless') for i in ingredients_only]
    ingredients_only=[i.replace('sa\x1dower oil', 'safflower oil') for i in ingredients_only]
    
    
    #ingredients_only=[i.replace('MINERALS', ' ') for i in ingredients_only]
    
    # Some other specific scenarios based on the data. 
    # This was identified while making the dictionary to standardize the name of ingredients
    #ingredients_only=[i for i in ingredients_only if i!='']
    #ingredients_only=[i.replace('Preserved With Mixed Tocopherols And Citric Acid', 'Preserved With Mixed Tocopherols, And Citric Acid') for i in ingredients_only]
    #ingredients_only=[i.replace('Mixed Tocopherols and Citric Acid (Preservatives)', 'Mixed Tocopherols (preservative), and Citric Acid (Preservative)') for i in ingredients_only]
    
    # Removing multiple whitespaces and new lines
    ingredients_only=[re.sub(' +', ' ', each) for each in ingredients_only]
    ingredients_only=[re.sub(r'\n+', '\n', each) for each in ingredients_only]
    ingredients_only=[re.sub('\n', '', each) for each in ingredients_only]
    ingredients_only=[i.strip() for i in ingredients_only]
    
    # Tokenized ingredients in a list of list format
    tokenized_ingredients_nested=[[ingredient.strip() for ingredient in each.split(',')] for each in ingredients_only]
    
    # Inconsistent use of the parantheses in the data is to be removed.
    new_tokenized_ingredients_nested=[]
    
    for ingredients in tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if '(' in each and ')' not in each:
                s=each.replace('(', '')
                ingredients_tokenized.append(s)
            elif ')' in each and '(' not in each:
                s=each.replace(')', '')
                ingredients_tokenized.append(s)
            else:
                ingredients_tokenized.append(each)
        new_tokenized_ingredients_nested.append(ingredients_tokenized)
        
    # Removing the unnecessary trailing fullstops and leading colons
    new_ingredients=[]

    for ingredients in new_tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if each[-1]=='.':
                item=each[:-1]
                ingredients_tokenized.append(item)
            elif each[0]==':':
                item=each[2:]
                ingredients_tokenized.append(item)
            else:
                ingredients_tokenized.append(each)
        new_ingredients.append(ingredients_tokenized)
        
    # Removing the 'ID' like text in the end of ingredients
    # In some places, the ingredients contained text that was unidentifiable.
    # For example, *Blue 2. N450118*. The *Blue 2* is a color here but the text after it is meaningless
    # Hence the below code removes such texts in the data.
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]
    new_ingredients_split      
    
    new_ingredients_2=[]
    for ingredients in new_ingredients_split:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)==2:
                if len(each[1])==8 or len(each[1])==7:
                    ingredients_tokenized.append(each[0])
                else:
                    ingredients_tokenized.append(each)
            else:
                ingredients_tokenized.append(each)
        new_ingredients_2.append(ingredients_tokenized)
        
    # Joining again with fullstops as that was the separator for splitting for previous step
    new_product_wise_ingredients=[]
    for ingredient in new_ingredients_2:
        ingredients=[]
        for each in ingredient:
            if type(each)==list:
                ingredients.append(('.').join(each).lower())
            else:
                ingredients.append(each.lower())
        new_product_wise_ingredients.append(ingredients)
    return new_product_wise_ingredients
    
#     # Splitting the ingredients column by \n to get the ingredients panel for different products in combos or variety packs
#     ingredients_only_split_for_combo_products_raw=[each.split('\n') for each in ingredients_only]
    
#     # Removing the 'Ingredients' word from ingredients panel
#     ingredients_only_split_for_combo_products=[]
#     for each in ingredients_only_split_for_combo_products_raw:
#         temp_list=[]
#         for s in each:
#             new_s=s.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}')
#             temp_list.append(new_s)
#         ingredients_only_split_for_combo_products.append(temp_list)
    
#     # removing empty nested lists
#     ingredients_only_split_for_combo_products_final=[[a for a in each if len(a)>0] for each in ingredients_only_split_for_combo_products]
#     return ingredients_only_split_for_combo_products_final

def ingredients_initial_cleaning_cat_dry(ingredients_column):
    '''This function will do the initial cleaning of noises for ingredients column before the actual standardization.
    Parameters: ingredients_column - The unprocessed ingredients column from the data
    Returns: A list of lists of cleaned splitted out ingredients'''
    
    # Get ingredients into a list of strings
    ingredients_list=list(ingredients_column)
    ingredients_list=[str(i) for i in ingredients_list]
    
    # Removing the caloric content from ingredients string
#     ingredients_only=[i.split('Caloric Content')[0] for i in ingredients_list]
    
#     # Some products have ingredients listed in two categories - Original and New
#     # The below code will remove the original list and keep only the new list of ingredients
#     #ingredients_only=[i for i in ingredients_only if str(i)!='nan']
#     ingredients_only=[i.split('Original:')[0] for i in ingredients_only]
#     ingredients_only=[i.replace('New:', '') for i in ingredients_only]
    
#     # Cleaning other noises in ingredients list specific to the  data
#     # These specific noises can vary from dataset to dataset and 
#     # needs to be looked into before executing them 
    
    ingredients_only=[i.replace('ingredients\n                        \n                                ', '') for i in ingredients_list]
    ingredients_only=[i.replace('] vitamins [', ', ') for i in ingredients_list]
    ingredients_only=[i.replace(". contains a source of live naturally occurring microorganisms.",
                                ", natural microorganisms") for i in ingredients_only]
    ingredients_only=[i.replace(". contains a source of live (viable), naturally occurring microorganisms.",
                                ", natural microorganisms") for i in ingredients_only]
    ingredients_only=[i.replace("docosahexaenoic acid (dha)", r"docosahexaenoic acid") for i in ingredients_only]
    ingredients_only=[i.replace("mixed tocopherols (vitamin e) used as a preservative", "mixed tocopherols (preservative)") for i in ingredients_only]
    ingredients_only=[i.replace("animal fat preserved with mixed-tocopherols (form of vitamin e)",
                                "animal fat (preserved with mixed-tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("mixed tocopherols (preservative, form of vitamin e;",
                                "mixed tocopherols (preservative and a form of vitamin e)") for i in ingredients_only]
    ingredients_only=[i.replace("\n",
                                " ") for i in ingredients_only]
    ingredients_only=[i.replace("menadione, sodium bisulfite complex",
                                "menadione sodium bisulfite complex") for i in ingredients_only]
    ingredients_only=[i.replace("thiamine, mononitrate",
                                "thiamine mononitrate") for i in ingredients_only]
    
    
#     ingredients_only=[i.replace('. contains a source of live (viable), naturally occurring microorganisms.',
#                                 ', naturally occurring microorganisms') for i in ingredients_only]
    ingredients_only=[i.replace(")", r"),") for i in ingredients_only]
    ingredients_only=[i.replace(r",,", r",") for i in ingredients_only]
    
    
    
#     ingredients_only=[i.replace('. contains a source of live (viable), naturally occurring microorganisms.',
#                                 ', naturally occurring microorganisms') for i in ingredients_only]
#     ingredients_only=[i.replace('. contains a source of live (viable), naturally occurring microorganisms.',
#                                 ', naturally occurring microorganisms') for i in ingredients_only]
    ingredients_only=[i.replace("vitamin e supplement  niacin  thiamine mononitrate  d-pantothenic acid  vitamin a supplement  riboflavin  pyridoxine hydrochloride  biotin  vitamin b12 supplement  vitamin d3 supplement  folic acid",
                                "vitamin e supplement, niacin, thiamine mononitrate, d-pantothenic acid, vitamin a supplement, riboflavin, pyridoxine hydrochloride, biotin, vitamin b12 supplement, vitamin d3 supplement, folic acid") for i in ingredients_only]
    ingredients_only=[i.replace("zinc proteinate  iron proteinate  calcium carbonate  manganese proteinate  copper proteinate  sodium selenite  calcium iodate",
                                "zinc proteinate, iron proteinate, calcium carbonate, manganese proteinate, copper proteinate, sodium selenite, calcium iodate") for i in ingredients_only]
    ingredients_only=[i.replace('contains a source of live, naturally occurring microorganisms',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('*',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace(', preserved with natural mixed tocopherols and citric acid',
                                ', mixed tocopherols (preservative), citric acid') for i in ingredients_only]
    ingredients_only=[i.replace('\n                        ', '') for i in ingredients_only]
    ingredients_only=[i.replace('biotin) minerals (', 'biotin), (') for i in ingredients_only]
    ingredients_only=[i.replace('chicken & rice:', '') for i in ingredients_only]
    
    ingredients_only=[i.replace('         meal', '') for i in ingredients_only]
    ingredients_only=[i.replace('   a-2569', ' a-2569') for i in ingredients_only]
    ingredients_only=[i.replace('\n', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\xa0', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('essential nutrients and other ingredients: ', '') for i in ingredients_only]
    ingredients_only=[i.replace('        inactive ingredients: disodium edta', ' disodium edta') for i in ingredients_only]
    ingredients_only=[i.replace(';', ',') for i in ingredients_only]
    ingredients_only=[i.replace('[', '') for i in ingredients_only]
    ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
#     # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
#     # We remove such key terms to get the actual name of ingredients
#     ingredients_only=[i.replace(' Minerals', '') for i in ingredients_only]
#     ingredients_only=[i.replace(' Vitamins', '') for i in ingredients_only]
#     ingredients_only=[i.replace('VITAMINS', ' ') for i in ingredients_only]
#     ingredients_only=[i.replace('MINERALS', ' ') for i in ingredients_only]
#     ingredients_only=[i.split('original:')[0] for i in ingredients_only]
    ingredients_only=[i.replace('new:', '') for i in ingredients_only]
    
    # Cleaning other noises in ingredients list specific to the  data
    # These specific noises can vary from dataset to dataset and 
    # needs to be looked into before executing them 
    #ingredients_only=[i.replace('Ingredients\n                        \n                                ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('\n                        ', '') for i in ingredients_only]
    ingredients_only=[i.replace('         meal', '') for i in ingredients_only]
    #ingredients_only=[i.replace('   A-2569', ' A-2569') for i in ingredients_only]
    #ingredients_only=[i.replace('\n', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\xa0', ' ') for i in ingredients_only]
    #ingredients_only=[i.replace('ESSENTIAL NUTRIENTS AND OTHER INGREDIENTS: ', '') for i in ingredients_only]
    #ingredients_only=[i.replace('        Inactive Ingredients: Disodium Edta', ' Inactive Ingredients: Disodium Edta') for i in ingredients_only]
    ingredients_only=[i.replace(';', '\n') for i in ingredients_only]
    ingredients_only=[i.replace(' ,', ',') for i in ingredients_only]
    ingredients_only=[i.replace('*(official name is marine microalgae)', '') for i in ingredients_only]
    ingredients_only=[i.replace('\u200btrout', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('?', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\u202f', ' ') for i in ingredients_only]
    ingredients_only=[i.replace('\t', ',') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    ingredients_only=[i.replace('a639120', '') for i in ingredients_only]
    ingredients_only=[i.replace('bisul\x1ete', 'bisulfite') for i in ingredients_only]
    ingredients_only=[i.replace('disulfite', 'bisulfite') for i in ingredients_only]
    #ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
    # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
    # We remove such key terms to get the actual name of ingredients
    ingredients_only=[i.replace('minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace('vitamins', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace('sa�ower oil', 'safflower oil') for i in ingredients_only]
    ingredients_only=[i.replace('boneless, skinless', 'boneless skinless') for i in ingredients_only]
    ingredients_only=[i.replace('sa\x1dower oil', 'safflower oil') for i in ingredients_only]
    ingredients_only=[i.replace('(l-ascorbyl-2-polyphosphate (source of vitamin c)', 'l-ascorbyl-2-polyphosphate') for i in ingredients_only]
    ingredients_only=[i.replace('alltech™ probiotics: ', '') for i in ingredients_only]
    ingredients_only=[i.replace('biotin) (copper sulfate', 'biotin, copper sulfate') for i in ingredients_only]
    ingredients_only=[i.replace('dehydrated sweet orange dehydrated apple',
                                'dehydrated sweet orange, dehydrated apple') for i in ingredients_only]
    ingredients_only=[i.replace('and dried',
                                ', dried') for i in ingredients_only]
    ingredients_only=[i.replace('contains a source of live (viable)',
                                '').strip() for i in ingredients_only]
    ingredients_only=[i.replace("poultry fat from 100% chicken mixed tocopherols (preservative)",
                                "poultry fat from 100% chicken (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("animal fat (preserved with mixed-tocopherols)",
                                "animal fat (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("beef fat preserved with mixed tocopherols",
                                "beef fat (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("canola oil (preserved with mixed tocopherols source of vitamin e)",
                                "canola oil (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("catfish oil preserved with mixed tocopherols",
                                "catfish oil (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("chicken fat (preserved with mixed natural tocopherols source of vitamin e)",
                                "chicken fat (preserved with natural mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("docosahexaenoic acid (source of omega-3 fatty acids)",
                                "dha (source of omega-3 fatty acids)") for i in ingredients_only]
    ingredients_only=[i.replace("feed grade fat product (algae source of fatty acids)",
                                "feed grade fat product algae") for i in ingredients_only]
    ingredients_only=[i.replace("fish oil from 100% menhaden oil mixed tocopherols (preservative)",
                                "menhaden fish oil (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("a- ",
                                "a") for i in ingredients_only]
    ingredients_only=[i.replace("ground miscanthus gra ss",
                                "ground miscanthus grass") for i in ingredients_only]
    ingredients_only=[i.replace("herring oil (preserved with mixed tocopherols source of vitamin e)",
                                "herring oil (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("menhaden fish oil (preserved with mixed natural tocopherols source of vitamin e)",
                                "menhaden fish oil (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("poultry fat from 100% chicken (preserved with mixed tocopherols)",
                                "chicken fat (preserved with mixed tocopherols)") for i in ingredients_only]
    ingredients_only=[i.replace("taurin,",
                                "taurine,") for i in ingredients_only]
    ingredients_only=[i.replace("vegetable juice (color)",
                                "vegetable juice") for i in ingredients_only]
    
    
    
    
    
#     ingredients_only=[i.replace('contains a source of live, naturally occurring microorganisms',
#                                 '') for i in ingredients_only]
    
    
    # Some other specific scenarios based on the data. 
    # This was identified while making the dictionary to standardize the name of ingredients
    #ingredients_only=[i for i in ingredients_only if i!='']
    ingredients_only=[i.replace('preserved with mixed tocopherols and citric acid', 'preserved with mixed tocopherols, and citric acid') for i in ingredients_only]
    ingredients_only=[i.replace(', source', ' source') for i in ingredients_only]
    ingredients_only=[i.replace(', a source', ' source') for i in ingredients_only]
    ingredients_only=[i.replace(' ,', ',') for i in ingredients_only]
    ingredients_only=[i.replace('potassium iodide beta-carotene', 'potassium iodide, beta-carotene') for i in ingredients_only]
    ingredients_only=[i.replace('rosemary extract and spearmint', 'rosemary extract, spearmint') for i in ingredients_only]
    ingredients_only=[i.replace('pyridoxine, calcium iodate', 'pyridoxine hydrochloride, calcium iodate') for i in ingredients_only]
    ingredients_only=[i.replace('vitamin d3 supplement. folic acid', 'vitamin d3 supplement, folic acid') for i in ingredients_only]
    ingredients_only=[i.replace('white fish meal (pacific whiting', 'pacific whiting') for i in ingredients_only]
    
    
    
#     ingredients_only=[i.replace('rosemary extract and spearmint', 'rosemary extract, spearmint') for i in ingredients_only]
#     ingredients_only=[i.replace(' and ', ', ') for i in ingredients_only]
    
    ingredients_only=[re.sub(' +', ' ', each) for each in ingredients_only]
#     ingredients_only=[re.sub('', 'nan', each) for each in ingredients_only]
#     ingredients_only=[i.replace(" and ", ", ") for i in ingredients_only]
    # Tokenized ingredients in a list of list format
    tokenized_ingredients_nested=[[ingredient.strip() for ingredient in each.split(',')] for each in ingredients_only]
    
    # Inconsistent use of the parantheses in the data is to be removed.
    new_tokenized_ingredients_nested=[]
    
    for ingredients in tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if '(' in each and ')' not in each:
                s=each.replace('(', '')
                ingredients_tokenized.append(s)
            elif ')' in each and '(' not in each:
                s=each.replace(')', '')
                ingredients_tokenized.append(s)
            else:
                ingredients_tokenized.append(each)
        new_tokenized_ingredients_nested.append(ingredients_tokenized)
        
    # Removing the unnecessary trailing fullstops and leading colons
    new_ingredients=[]

    for ingredients in new_tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)!=0 and each[-1]=='.':
                item=each[:-1].strip()
                ingredients_tokenized.append(item)
            elif len(each)!=0 and each[0]==':':
                item=each[2:].strip()
                ingredients_tokenized.append(item)
            else:
                ingredients_tokenized.append(each)
        new_ingredients.append(ingredients_tokenized)
        
    # Removing the 'ID' like text in the end of ingredients
    # In some places, the ingredients contained text that was unidentifiable.
    # For example, *Blue 2. N450118*. The *Blue 2* is a color here but the text after it is meaningless
    # Hence the below code removes such texts in the data.
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]
    new_ingredients_split      
    
    new_ingredients_2=[]
    for ingredients in new_ingredients_split:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)==2:
                if len(each[1])==8 or len(each[1])==7:
                    ingredients_tokenized.append(each[0].strip())
                else:
                    ingredients_tokenized.append(each)
            else:
                ingredients_tokenized.append(each)
        new_ingredients_2.append(ingredients_tokenized)
        
    # Joining again with fullstops as that was the separator for splitting for previous step
    new_product_wise_ingredients=[]
    for ingredient in new_ingredients_2:
        ingredients=[]
        for each in ingredient:
            if type(each)==list:
                ingredients.append(('.').join(each).lower())
            else:
                ingredients.append(each.lower())
        new_product_wise_ingredients.append(ingredients)
    return new_product_wise_ingredients
    
def splitting_ingredient_panel_to_individual_ingredients(flavour_wise_split_ingredients_column):
    '''This function will split the ingredients by commas from the full ingredients panela and 
    will also do further cleaning of noises.
    Parameters: flavour_wise_split_ingredients_column - The ingredients column generated based on the flavour 
    wise split ingredients
    Returns: A list of lists of cleaned and splitted individual ingredients'''
    
    ingredients_only_new=list(flavour_wise_split_ingredients_column)
    # Tokenized ingredients in a list of list format
    tokenized_ingredients_nested=[[ingredient.strip() for ingredient in each.split(',')] for each in ingredients_only_new]
    
    
    # Removing the '()' and '{}' where they may cause problems in the list. 
    #This is to keep the brackets which are necessary with the ingredient names intact and remove other brackets.
    
    # Inconsistent use of the parantheses in the data is to be removed.
    new_tokenized_ingredients_nested=[]
    for ingredients in tokenized_ingredients_nested:
        ingredients_tokenized=[]
        for each in ingredients:
            if '(' in each and ')' not in each:
                s=each.replace('(', '')
                ingredients_tokenized.append(s)
            elif ')' in each and '(' not in each:
                s=each.replace(')', '')
                ingredients_tokenized.append(s)
            else:
                ingredients_tokenized.append(each)
        new_tokenized_ingredients_nested.append(ingredients_tokenized)
        
    # Same with curly brackets
    new_tokenized_ingredients_nested_2=[]
    for each in new_tokenized_ingredients_nested:
        temp_ingredient_list=[]
        for ingredient in each:
            if '{' in ingredient and '}' not in ingredient:
                st=ingredient.replace('{', '')
                temp_ingredient_list.append(st)
            elif '}' in ingredient and '{' not in ingredient:
                st=ingredient.replace('}', '')
                temp_ingredient_list.append(st)
            else:
                temp_ingredient_list.append(ingredient)
        new_tokenized_ingredients_nested_2.append(temp_ingredient_list)
    new_tokenized_ingredients_nested_2
    
    new_tokenized_ingredients_nested_2=[[i.replace('{', '(').replace('}', ')') for i in each] for each in new_tokenized_ingredients_nested_2]

    # Removing the unnecessary trailing fullstops
    new_ingredients=[]

    for ingredients in new_tokenized_ingredients_nested_2:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)>0 and each[-1]=='.':
                item=each[:-1]
                ingredients_tokenized.append(item)
            # elif each[0]==':':
            #     item=each[2:]
            #     ingredients_tokenized.append(item)
            else:
                ingredients_tokenized.append(each)
        new_ingredients.append(ingredients_tokenized)
        
    # Removing the 'ID' like text in the end of ingredients
    # In some places, the ingredients contained text that was unidentifiable. For example, *Blue 2. N450118*. The *Blue 2* is a color here but the text after it is meaningless. Hence the below code removes such texts in the data.
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]     

    new_ingredients_2=[]
    for ingredients in new_ingredients_split:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)==2:
                if len(each[1])==8 or len(each[1])==7 or len(each[1])==10 or len(each[1])==11:
                    ingredients_tokenized.append(each[0])
                else:
                    ingredients_tokenized.append(each)
            else:
                ingredients_tokenized.append(each)
        new_ingredients_2.append(ingredients_tokenized)
        
    # Joining again with fullstops as that was the separator for splitting for previous step
    new_product_wise_ingredients=[]
    for ingredient in new_ingredients_2:
        ingredients=[]
        for each in ingredient:
            if type(each)==list:
                ingredients.append(('.').join(each).strip())
            else:
                ingredients.append(each)
        new_product_wise_ingredients.append(ingredients)
    
    return new_product_wise_ingredients

def final_ingredients_correction(product_wise_ingredients_panel,
                                 standardized_dictionary_of_ingredients):
    '''This function do the final correction based on the standardized dictionary of ingredients
    which follows AAFCO standards
    Parameters: product_wise_ingredients_panel - A list of ingredients which are clean yet not
    standardized, standardized_dictionary_of_ingredients - The dictionary of standardized ingredients
    Returns: Final list of product wise ingredients panel separated by comma. '''
    
    # Replacing where the key from the dictionary exists in the product wise ingredients list with the value of that corresponding key in the data.
    
    new_standardized_ingredient_names=[]
    for ingredients in product_wise_ingredients_panel:
        ingreds=[]
        for each in ingredients:
            #print(each)
            for key in standardized_dictionary_of_ingredients.keys():
                if str(each)==key:
                    ing=each.lower().replace(key, standardized_dictionary_of_ingredients[key]).strip()
                elif str(each)=='nan':
                    ing=each.strip()
            ingreds.append(ing)
        new_standardized_ingredient_names.append(ingreds)
    return new_standardized_ingredient_names