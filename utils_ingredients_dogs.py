# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:37:52 2022

@author: siddh
"""
import re

def ingredients_cleaning_dog_dry(ingredients_column):
    '''This function will do the initial cleaning of noises for ingredients column before the actual standardization.
    Parameters: ingredients_column - The unprocessed ingredients column from the data
    Returns: A list of lists of cleaned splitted out ingredients'''
    
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
    ingredients_only=[i.replace('iron amino acid chelate  vitamin e supplement',
                                'iron amino acid chelate, vitamin e supplement') for i in ingredients_only]
    ingredients_only=[i.replace('iron proteinate  copper proteinate',
                                'iron proteinate, copper proteinate') for i in ingredients_only]
    ingredients_only=[i.replace('magnesium sulfate. sodium selenite',
                                'magnesium sulfate, sodium selenite') for i in ingredients_only]
    ingredients_only=[i.replace("pea starch\xa0 brewer's dried yeast",
                                "pea starch, brewer's dried yeast") for i in ingredients_only]
    ingredients_only=[i.replace("potato calcium carbonate",
                                "potato, calcium carbonate") for i in ingredients_only]
    ingredients_only=[i.replace("pyridoxine hydrochloride vitamin d3 supplement",
                                "pyridoxine hydrochloride, vitamin d3 supplement") for i in ingredients_only]
    ingredients_only=[i.replace("riboavin",
                                "riboflavin") for i in ingredients_only]
    ingredients_only=[i.replace("riboflavin  biotin",
                                "riboflavin, biotin") for i in ingredients_only]
    ingredients_only=[i.replace("rice pasta (rice, water, ground tapioca)",
                                "rice pasta") for i in ingredients_only]
    ingredients_only=[i.replace("salmo,",
                                "salmon,") for i in ingredients_only]
    ingredients_only=[i.replace(", supplement",
                                " supplement") for i in ingredients_only]
    ingredients_only=[i.replace("thiamine mononitrate {vitamin b1} d-calcium pantothenate",
                                "thiamine mononitrate (vitamin b1), d-calcium pantothenate") for i in ingredients_only]
    ingredients_only=[i.replace("turkey & bacon\n",
                                "") for i in ingredients_only]
    ingredients_only=[i.replace("turkey & duck\n",
                                "") for i in ingredients_only]
    ingredients_only=[i.replace("vitamin b12 pyridoxine hydrochloride",
                                "vitamin b12, pyridoxine hydrochloride") for i in ingredients_only]
    ingredients_only=[i.replace("supplement.  water",
                                "supplement, water") for i in ingredients_only]
    ingredients_only=[i.replace(",vitamins",
                                ",") for i in ingredients_only]
    ingredients_only=[i.replace("water sufficient for\nprocessing",
                                "water sufficient for processing") for i in ingredients_only]
    ingredients_only=[i.replace("supplement. water",
                                "supplement, water") for i in ingredients_only]
    
    
    
    ingredients_only=[i.replace('natural flavor cranberries',
                                'natural flavor, cranberries') for i in ingredients_only]
    ingredients_only=[i.replace('vitamins & minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace('dicalcium phosphate minerals',
                                'dicalcium phosphate, minerals') for i in ingredients_only]
    ingredients_only=[i.replace('ground flaxseed choline chloride',
                                'ground flaxseed, choline chloride') for i in ingredients_only]
    ingredients_only=[i.replace('icelandic fish (cod',
                                '(cod') for i in ingredients_only]
    ingredients_only=[i.replace('natural hickory smoke',
                                'natural hickory smoke flavor') for i in ingredients_only]
    ingredients_only=[i.replace('pyridoxine hydrochloride,(vitamin b6)',
                                'pyridoxine hydrochloride (vitamin b6)') for i in ingredients_only]
    ingredients_only=[i.replace('vitamin e, a, b12, d3',
                                'vitamin e, vitamin a, vitamin b12, vitamin d3') for i in ingredients_only]
    ingredients_only=[i.replace('apples rice starch',
                                'apples, rice starch') for i in ingredients_only]
    
    ingredients_only=[i.replace('beef fat(preserved with mixed tocopherols and ascorbic acid)',
                                'beef fat (preserved with mixed tocopherols and ascorbic acid)') for i in ingredients_only]
    ingredients_only=[i.replace('bitoin',
                                'biotin') for i in ingredients_only]
    ingredients_only=[i.replace('calcium , pantothenate',
                                'calcium pantothenate') for i in ingredients_only]
    
    
    ingredients_only=[i.replace('. contains a source of live (viable), naturally occurring microorganisms.',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('this is a naturally preserved product',
                                '') for i in ingredients_only]
    
    ingredients_only=[i.replace('this is a naturally preserved product.',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('spearmint extract.\nthis is a naturally preserved product.',
                                'spearmint extract') for i in ingredients_only]
    ingredients_only=[i.replace('spearmint extract.this is a naturally preserved product.',
                                'spearmint extract') for i in ingredients_only]
    ingredients_only=[i.replace('spearmint extract. this is a naturally preserved product.',
                                'spearmint extract') for i in ingredients_only]
    ingredients_only=[i.replace('tomato pomace  chicken fat (mixed tocopherols)',
                                'tomato pomace, chicken fat (preserved with mixed tocopherols)') for i in ingredients_only]
    ingredients_only=[i.replace('vegetavle',
                                'vegetable') for i in ingredients_only]
    ingredients_only=[i.replace('vitamin b12 supplement) dried',
                                'vitamin b12 supplement), dried') for i in ingredients_only]
    ingredients_only=[i.replace('ï¿½',
                                ' ') for i in ingredients_only]
    ingredients_only=[i.replace(') citric acid',
                                '), citric acid') for i in ingredients_only]
    ingredients_only=[i.replace('vitamin d3 supplement) mixed tocopherols for freshness',
                                'vitamin d3 supplement), mixed tocopherols for freshness') for i in ingredients_only]
    ingredients_only=[i.replace('yeast extract (a source of prebiotics) glucosamine hydrochloride',
                                'yeast extract (a source of prebiotics), glucosamine hydrochloride') for i in ingredients_only]
    
    
    ingredients_only=[i.replace('oatmeal barley',
                                'oatmeal, barley') for i in ingredients_only]
    ingredients_only=[i.replace('ocean \x1dfish meal',
                                'ocean fish meal') for i in ingredients_only]
    ingredients_only=[i.replace('. d-2620. 15% - a source of fiber.',
                                '') for i in ingredients_only]
    
    ingredients_only=[i.replace('psyilium seed husks taurine calcium carbonate vitamin e supplement',
                                'psyllium seed husk, taurine, calcium carbonate, vitamin e supplement') for i in ingredients_only]
    ingredients_only=[i.replace('pyri- doxine hydrochloride (vitamin b6)',
                                'pyridoxine hydrochloride (vitamin b6)') for i in ingredients_only]
    ingredients_only=[i.replace(' reserved with mixed tocopherols and citric acid.',
                                'mixed tocopherols (preservative), citric acid (preservative)') for i in ingredients_only]
    ingredients_only=[i.replace('powered cellulose',
                                'powdered cellulose') for i in ingredients_only]
    ingredients_only=[i.replace('riboâ€‚avin',
                                'riboflavin') for i in ingredients_only]
    ingredients_only=[i.replace('rosemary extract supplement, ',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('zinc sulfate ferrous sulfate',
                                'zinc sulfate, ferrous sulfate') for i in ingredients_only]
    
    
    
    ingredients_only=[i.replace('.\ncontains a source of live (viable), naturally occurring microorganisms.',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('lactosaccâ„¢ probiotics:',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('mixed tocopherols (preservative ,',
                                'mixed tocopherols (preservative),') for i in ingredients_only]
    ingredients_only=[i.replace('natural vegetable flavor dicalcium phosphate',
                                'natural vegetable flavor, dicalcium phosphate') for i in ingredients_only]
    ingredients_only=[i.replace('rosemary.',
                                'rosemary') for i in ingredients_only]
    ingredients_only=[i.replace('salt vitamins',
                                'salt, vitamins') for i in ingredients_only]
    ingredients_only=[i.replace('canolia oil (preserved with mixed tocopherols)',
                                'canola oil (preserved with mixed tocopherols)') for i in ingredients_only]
    ingredients_only=[i.replace('carrageenan guar gum',
                                'carrageenan, guar gum') for i in ingredients_only]
    ingredients_only=[i.replace('cobalt amino acid, chelate',
                                'cobalt amino acid chelate') for i in ingredients_only]
    ingredients_only=[i.replace('copper proteinate sodium selenite',
                                'copper proteinate, sodium selenite') for i in ingredients_only]
    
    
    ingredients_only=[i.replace('lecithin and rosemary extract',
                                'lecithin, rosemary extract') for i in ingredients_only]
    
     
    ingredients_only=[i.replace('hydrolyzed yeast (actigenâ„¢ - prebiotic)',
                                'hydrolyzed yeast') for i in ingredients_only]
    
    ingredients_only=[i.replace('pyridoxine, hydrochloride',
                                'pyridoxine hydrochloride') for i in ingredients_only]
    ingredients_only=[i.replace('dlâ€“methionine', 'dl-methionine') for i in ingredients_only]
    
    ingredients_only=[i.replace('â ', '') for i in ingredients_only]
    ingredients_only=[i.replace('â', '').strip() for i in ingredients_only]
    
    ingredients_only=[i.replace('the facility in which this food is made also makes food that may contain other',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('animal fat, (source of omega 6 fatty acids [preserved with bha/citric acid])',
                                'animal fat (preserved with bha & citric acid)') for i in ingredients_only]
    ingredients_only=[i.replace('animal fat, (source of omega 6 fatty acids) [preserved with bha/citric acid]',
                                'animal fat (preserved with bha & citric acid)') for i in ingredients_only]
    ingredients_only=[i.replace('d-calcium pantothenate, [source of vitamin b5]',
                                'd-calcium pantothenate (source of vitamin b5)') for i in ingredients_only]
    ingredients_only=[i.replace('niacin, (vitamin b-3)',
                                'niacin (vitamin b-3)') for i in ingredients_only]
    ingredients_only=[i.replace('chicken fat (preserved with mixed natural tocopherols, a source of vitamin e)',
                                'chicken fat (preserved with mixed natural tocopherols)') for i in ingredients_only]
    ingredients_only=[i.replace('tocopherols, a source of vitamin e',
                                'tocopherols') for i in ingredients_only]
    ingredients_only=[i.replace('animal fat (source of omega 6 fatty acids) [preserved with bha and citric acid])',
                                'animal fat (preserved with bha and citric acid)') for i in ingredients_only]
    ingredients_only=[i.replace('bha and citric acid (a preservative)',
                                'bha (preservative), citric acid (preservative)') for i in ingredients_only]
    ingredients_only=[i.replace('biotin folic acid',
                                'biotin, folic acid') for i in ingredients_only]
    ingredients_only=[i.replace('€™',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('cobalt, carbonate',
                                'cobalt carbonate') for i in ingredients_only]
    ingredients_only=[i.replace('chicken by-products (organs only, source of arginine)',
                                'chicken by-products') for i in ingredients_only]
    ingredients_only=[i.replace('chicken fat (preserved with natural mixed tocopherols; a source of vitamin e)',
                                'chicken fat (preserved with natural mixed tocopherols)') for i in ingredients_only]
    ingredients_only=[i.replace('chicken meal (natural source of glucosamine and chondroitin)',
                                'chicken meal') for i in ingredients_only]
    ingredients_only=[i.replace('cobalt carbonate and cobalt glucoheptonate',
                                'cobalt carbonate, cobalt glucoheptonate') for i in ingredients_only]
    ingredients_only=[i.replace('cobalt carbonate) dried chicory root',
                                'cobalt carbonate), dried chicory root') for i in ingredients_only]
    ingredients_only=[i.replace('dl-methionine hydroxy analogue',
                                'dl-methionine') for i in ingredients_only]
    ingredients_only=[i.replace('dried bi€‚dobacterium animalis fermentation product',
                                'dried bifidobacterium animalis fermentation product') for i in ingredients_only]
    ingredients_only=[i.replace('dried lactobacillus acidophilus fermentation product rosemary extract',
                                'dried lactobacillus acidophilus fermentation product, rosemary extract') for i in ingredients_only]
    ingredients_only=[i.replace('contains a source of live naturally occuring microorganisms.',
                                '') for i in ingredients_only]
    ingredients_only=[i.replace('dried lactobacillus casei fermentation product.',
                                'dried lactobacillus casei fermentation product') for i in ingredients_only]
    ingredients_only=[i.replace('dried lactobacillus plantarum fermentation product.',
                                'dried lactobacillus plantarum fermentation product') for i in ingredients_only]
    ingredients_only=[i.replace('folic acid] dl-methionine',
                                'folic acid], dl-methionine') for i in ingredients_only]
    ingredients_only=[i.replace('i-threonine',
                                'l-threonine') for i in ingredients_only]
    ingredients_only=[i.replace('menhaden fish meal (a source of glucosamine and chondroitin)',
                                'menhaden fish meal') for i in ingredients_only]
    ingredients_only=[i.replace('mixed tocopherols (a source of vitamin e) and rosemary extract.',
                                'mixed tocopherols (a source of vitamin e), rosemary extract') for i in ingredients_only]
    ingredients_only=[i.replace(')', '),').replace(',,', ',') for i in ingredients_only]
    
    
    ingredients_only=[i.split('original:')[0] for i in ingredients_only]
    ingredients_only=[i.replace('new:', '') for i in ingredients_only]
    ingredients_only=[i.replace('essential nutrients and other ingredients:', ',') for i in ingredients_only]
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
    ingredients_only=[each.replace('"', '') for each in ingredients_only]
    ingredients_only=[each.replace('>', '') for each in ingredients_only]
    ingredients_only=[each.replace('<', '') for each in ingredients_only]
    
    
    ingredients_only=[i.replace(') vitamins (', '), (') for i in ingredients_only]
    ingredients_only=[i.replace(') minerals (', '), (') for i in ingredients_only]
#     ingredients_only=[i.split('original:')[0] for i in ingredients_list]
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
    ingredients_only=[i.replace(', and ', ', ') for i in ingredients_only]
    ingredients_only=[i.replace(', preserved with mixed tocopherols and citric acid', ', preserved with mixed tocopherols, and citric acid') for i in ingredients_only]
    #ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
    # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
    # We remove such key terms to get the actual name of ingredients
    ingredients_only=[i.replace(' minerals', '') for i in ingredients_only]
    
    ingredients_only=[i.replace('minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace(' vitamins', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace('<', '') for i in ingredients_only]
    ingredients_only=[i.replace('>', '') for i in ingredients_only]
    ingredients_only=[i.replace('(, )', ',') for i in ingredients_only]
    ingredients_only=[i.replace('*', '') for i in ingredients_only]
    
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
    
    ingredients_only=[each.replace('ingredients', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('cottage cheese (milk', 'cottage cheese, (milk ingredients').strip() for each in ingredients_only]
    
    ingredients_only=[each.replace('sa�ower oil', 'safflower oil').strip() for each in ingredients_only]
    ingredients_only=[each.replace('�', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('bonless, skinless', 'boneless skinless').strip() for each in ingredients_only]
    ingredients_only=[each.replace('contains a source of live (viable) naturally occurring microorganisms', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('\n', '').strip() for each in ingredients_only]
    ingredients_only=[each.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}') for each in ingredients_only]
    ingredients_only=[each.replace('delivered fresh or raw', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('dried bacillus coagulans fermentation product zinc proteinate',
                                   'dried bacillus coagulans fermentation product, zinc proteinate').strip() for each in ingredients_only]
    ingredients_only=[each.replace('dried chicory root (source of inulin) dried pediococcus acidilactici fermentation product',
                                   'dried chicory root (source of inulin), dried pediococcus acidilactici fermentation product').strip() for each in ingredients_only]
#     ingredients_only=[each.replace('omega 3 & 6 from fish oil', 'omega 3 & 6 from fish oil').strip() for each in ingredients_only]
    ingredients_only=[i.replace('(proteinated and)', '') for i in ingredients_only]
    ingredients_only=[i.replace('potassium, chloride', 'potassium chloride') for i in ingredients_only]
    ingredients_only=[i.replace('(l-ascorbyl-2-polyphosphate (source of vitamin c)',
                                'l-ascorbyl-2-polyphosphate (source of vitamin c)') for i in ingredients_only]
    ingredients_only=[i.replace('chicken fat, (preserved with mixed tocopherols)',
                                'chicken fat (preserved with mixed tocopherols)') for i in ingredients_only]
    ingredients_only=[i.replace('animal fat, (source of omega 6 fatty acids (preserved with bha/citric acid))',
                                'animal fat (preserved with bha & citric acid)') for i in ingredients_only]
    ingredients_only=[i.replace('. ferrous sulfate', ' ferrous sulfate') for i in ingredients_only]
    ingredients_only=[i.replace('. peas', ' peas') for i in ingredients_only]
    
    
    ingredients_only=[each.replace('\n', '').strip() for each in ingredients_only]
    ingredients_only=[each.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}') for each in ingredients_only]
    
    # ingredients_only=[i.replace('grilled chicken flavor sufficient water for processing', 'sufficient water for processing') for i in ingredients_only]
    ingredients_only=[i.replace('minerals magnesium oxide', 'magnesium oxide') for i in ingredients_only]
    # To keep the row wise(product wise) ingredient list intact, we first need a list of lists containing all the ingredients.
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
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]
    
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
                ingredients.append(('.').join(each).strip().replace(': ', ''))
            else:
                ingredients.append(each)
        new_product_wise_ingredients.append(ingredients)
        
    # new_product_wise_ingredients[0] = []
    return new_product_wise_ingredients

def ingredients_cleaning_dog_raw(ingredients_column):
    '''This function will do the initial cleaning of noises for ingredients column before the actual standardization.
    Parameters: ingredients_column - The unprocessed ingredients column from the data
    Returns: A list of lists of cleaned splitted out ingredients'''
    
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
    
#     ingredients_only=[each.replace('omega 3 & 6 from fish oil', 'omega 3 & 6 fatty acids').strip() for each in ingredients_only]
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
    #ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
    # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
    # We remove such key terms to get the actual name of ingredients
    
    ingredients_only=[i.replace('vitamins & minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace(' minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace(' vitamins', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace('<', '') for i in ingredients_only]
    ingredients_only=[i.replace('>', '') for i in ingredients_only]
    ingredients_only=[i.replace('(, )', ',') for i in ingredients_only]
    ingredients_only=[i.replace('*', '') for i in ingredients_only]
    
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
    
    ingredients_only=[each.replace('ingredients', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('sa�ower oil', 'safflower oil').strip() for each in ingredients_only]
    ingredients_only=[each.replace('bonless, skinless', 'boneless skinless').strip() for each in ingredients_only]
    ingredients_only=[each.replace('contains a source of live (viable) naturally occurring microorganisms', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('contains a source of live naturally occuring microorganisms', '').strip() for each in ingredients_only]
    
    
    
    ingredients_only=[each.replace('\n', '').strip() for each in ingredients_only]
    ingredients_only=[each.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}') for each in ingredients_only]
    ingredients_only=[each.replace('delivered fresh or raw', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('dried bacillus coagulans fermentation product zinc proteinate',
                                   'dried bacillus coagulans fermentation product, zinc proteinate').strip() for each in ingredients_only]
    ingredients_only=[each.replace('dried chicory root (source of inulin) dried pediococcus acidilactici fermentation product',
                                   'dried chicory root (source of inulin), dried pediococcus acidilactici fermentation product').strip() for each in ingredients_only]
    ingredients_only=[each.replace('omega 3 & 6 from fish oil', 'omega 3 & 6 from fish oil').strip() for each in ingredients_only]
    ingredients_only=[i.replace('(proteinated and)', '') for i in ingredients_only]
    ingredients_only=[i.replace('potassium, chloride', 'potassium chloride') for i in ingredients_only]
    
    
    
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
    
    new_tokenized_ingredients_nested_2=[[i.replace('{', '(').replace('}', ')') for i in each] for each in new_tokenized_ingredients_nested_2]

    # Removing the unnecessary trailing fullstops
    new_ingredients=[]

    for ingredients in new_tokenized_ingredients_nested_2:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)>0 and each[-1]=='.':
                ingredients_tokenized.append(each[:-1])
            # elif each[0]==':':
            #     item=each[2:]
            #     ingredients_tokenized.append(item)
            else:
                ingredients_tokenized.append(each)
        new_ingredients.append(ingredients_tokenized)
        
    # Removing the 'ID' like text in the end of ingredients
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]
    
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
                ingredients.append(('.').join(each).strip().replace(': ', ''))
            else:
                ingredients.append(each)
        new_product_wise_ingredients.append(ingredients)
        

        # Removing the unnecessary trailing fullstops
    new_product_wise_ingredients_2=[]

    for ingredients in new_product_wise_ingredients:
        ingredients_tokenized=[]
        for each in ingredients:
            if len(each)>0 and each[-1]=='.':
                ingredients_tokenized.append(each[:-1])
            # elif each[0]==':':
            #     item=each[2:]
            #     ingredients_tokenized.append(item)
            else:
                ingredients_tokenized.append(each)
        new_product_wise_ingredients_2.append(ingredients_tokenized)    
        
    return new_product_wise_ingredients_2

def ingredients_cleaning_dog_vet(ingredients_column):
    '''This function will do the initial cleaning of noises for ingredients column before the actual standardization.
    Parameters: ingredients_column - The unprocessed ingredients column from the data
    Returns: A list of lists of cleaned splitted out ingredients'''
    
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
    
    
    #ingredients_only=[i.replace(']', '') for i in ingredients_only]
    
    # Vitamins and Minerals are preceded by the key terms 'Vitamins' and 'Minerals'
    # We remove such key terms to get the actual name of ingredients
    ingredients_only=[i.replace(' minerals', '') for i in ingredients_only]
    ingredients_only=[i.replace(' vitamins', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace(' b626618-13', '') for i in ingredients_only]
    ingredients_only=[i.replace('15% - a source of fiber', '') for i in ingredients_only]
    ingredients_only=[i.replace('<', '') for i in ingredients_only]
    ingredients_only=[i.replace('>', '') for i in ingredients_only]
    ingredients_only=[i.replace('(, )', ',') for i in ingredients_only]
    ingredients_only=[i.replace('*', '') for i in ingredients_only]
    ingredients_only=[i.replace('niacin, (vitamin b-3)', 'niacin (vitamin b-3)') for i in ingredients_only]
    ingredients_only=[i.replace('. d-2620.', '') for i in ingredients_only]
    ingredients_only=[i.replace('trace zinc proteinate', 'zinc proteinate') for i in ingredients_only]
    ingredients_only=[i.replace('minerals magnesium oxide', 'magnesium oxide') for i in ingredients_only]
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
    
    ingredients_only=[each.replace('ingredients', '').strip() for each in ingredients_only]
    ingredients_only=[each.replace('\n', '').strip() for each in ingredients_only]
    ingredients_only=[each.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}') for each in ingredients_only]
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
    new_ingredients_split=[[i.split('.') for i in each] for each in new_ingredients]
    
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
                ingredients.append(('.').join(each).strip().replace(': ', ''))
            else:
                ingredients.append(each)
        new_product_wise_ingredients.append(ingredients)
    return new_product_wise_ingredients

def ingredients_initial_cleaning_dog_wet(ingredients_column):
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
    ingredients_only=[i.replace('essential nutrients and other ingredients:', ',') for i in ingredients_only]
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
    #ingredients_only=[i.replace('MINERALS', ' ') for i in ingredients_only]

    ingredients_only=[i.replace('minerals magnesium oxide', 'magnesium oxide') for i in ingredients_only]
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
    ingredients_only=[each.replace('"', '') for each in ingredients_only]
    ingredients_only=[each.replace('>', '') for each in ingredients_only]
    ingredients_only=[each.replace('<', '') for each in ingredients_only]
    
    #ingredients_only=[re.sub(r") [a-z]", r"), [a-z]", each) for each in ingredients_only]
    
    #ingredients_only=[each.replace(', (', '(') for each in ingredients_only]

    
    # This step is to take care of random newline characters between any ingredients
    # ingredients_only_final=[each.replace('ingredients', '').strip() for each in ingredients_only]
    
    # ingredients_only_final_2=[]
    # for i, each in enumerate(ingredients_only_final):
    #     if ':' not in each and '\n' in each:
    #         ingredients_only_final_2.append(each.replace('\n', ''))
    #     else:
    #         ingredients_only_final_2.append(each)
            
    # # Splitting the ingredients column by \n to get the ingredients panel for different products in combos or variety packs
    # ingredients_only_split_for_combo_products_raw=[each.split('\n') for each in ingredients_only_final_2]
    
    # # Removing the 'Ingredients' word from ingredients panel
    # ingredients_only_split_for_combo_products=[]
    # for each in ingredients_only_split_for_combo_products_raw:
    #     temp_list=[]
    #     for s in each:
    #         new_s=s.strip().lower().replace('ingredients', '').replace('[', '{').replace(']', '}')
    #         temp_list.append(new_s)
    #     ingredients_only_split_for_combo_products.append(temp_list)
    
    # # removing empty nested lists
    # ingredients_only_split_for_combo_products_final=[[a for a in each if len(a)>0] for each in ingredients_only_split_for_combo_products]
    # return ingredients_only_split_for_combo_products_final
    
    ingredients_only=[i.replace('grilled chicken flavor sufficient water for processing', 'sufficient water for processing') for i in ingredients_only]
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
                if str(each.lower())==key:
                    ingredient=each.lower().replace(key, standardized_dictionary_of_ingredients[key])
                elif str(each)=='nan':
                    ingredient=each
            ingreds.append(ingredient)
        new_standardized_ingredient_names.append(ingreds)
    return new_standardized_ingredient_names