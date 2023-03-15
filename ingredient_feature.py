import streamlit as st
import pandas as pd
import numpy as np
import utils_ingredients_cats
from utils_ingredients_cats import *
import utils_ingredients_dogs
from utils_ingredients_dogs import *
st.set_page_config(layout="wide")

ingredient_dict = pd.read_csv("ingredient_names_dictionary_17_01_23.csv", sep = '|')

col_1, space, col_2 = st.columns([1,0.2,1])


with col_1:
    st.markdown('#### Enter Ingredient List:')
    ing_str = st.text_area('Enter Ingredient List:', height= 250,  label_visibility = 'collapsed')

    ing_str = ing_str.replace('Vitamins', '')
    ing_str = ing_str.replace('Minerals', '')
    ing_str = ing_str.replace('vitamins', '')
    ing_str = ing_str.replace('minerals', '')

    if ing_str == '':
        st.error('Please enter the ingredient list.')
        ing_str ='.'
    ing_str_list = []
    ing_str_list.append(ing_str)


# st.write(ing_str_list)
cleaning_function = [ingredients_initial_cleaning_cat_wet, ingredients_initial_cleaning_cat_dry,
                     ingredients_initial_cleaning_cat_raw, ingredients_initial_cleaning_cat_vet,
                     ingredients_initial_cleaning_dog_wet, ingredients_cleaning_dog_vet,
                     ingredients_cleaning_dog_raw, ingredients_cleaning_dog_dry]

for func in cleaning_function:
    # st.write(func)
    # ing_str_list = ing_str_list.
    ing_str_list = [each.split(':')[1] if ':' in each else each for each in ing_str_list]
    
    new_product_wise_ingredients=func(ing_str_list)
    # st.write(new_product_wise_ingredients)
    set_of_already_corrected_ingredient_names=set(ingredient_dict['original_ingredient'])
    set_of_current_ingredients=set(new_product_wise_ingredients[0])
    new_ingre = len(set_of_current_ingredients-set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients))
    remaining_set = set_of_current_ingredients-set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients)
    # st.write((set_of_current_ingredients-set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients)))
    
    # new_product_wise_ingredients[0]=[each.split(':')[1] if ':' in each else each for each in new_product_wise_ingredients[0]]
    
    
    if np.nan in remaining_set and '' in remaining_set and len(remaining_set)==2:
        break
    
    # if new_ingre < 3:
    #     break
    
        
    

# st.write(f"New Ingredients not present in dictionary: {(set_of_current_ingredients-set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients))}")
# st.write(f"Total Unique Ingredients: {len(set_of_current_ingredients)}")
# st.write(new_product_wise_ingredients[0])

ing_pare_cat = {}
for each in  new_product_wise_ingredients[0]:
    if each in ingredient_dict['original_ingredient'].unique().tolist():
        parent_cat = (ingredient_dict[ingredient_dict['original_ingredient'] == each.lower()]['new_ingredient_parent_category'].unique()[0])
        sub_cat = (ingredient_dict[ingredient_dict['original_ingredient'] == each.lower()]['new_ingredient_sub_category'].unique()[0])
        # st.write(parent_cat, sub_cat)
        ing_pare_cat[each] = parent_cat.capitalize()
    

# ing_pare_cat = {}
# for each in  ingredient_dict['original_ingredient'].unique().tolist():
#     for ingre in ing_str.split(', '):
#         if each == ingre.lower():
#             parent_cat = (ingredient_dict[ingredient_dict['original_ingredient'] == each.lower()]['new_ingredient_parent_category'].unique()[0])
#             sub_cat = (ingredient_dict[ingredient_dict['original_ingredient'] == each.lower()]['new_ingredient_sub_category'].unique()[0])
#             ing_pare_cat[ingre] = parent_cat.capitalize()
        
# print(set(ing_pare_cat.values()))

with col_2:
    st.markdown('#### Selected Category:')
    selected_p_c = st.radio('Selected Category:', set(ing_pare_cat.values()), label_visibility = 'collapsed')

    if len(set(ing_pare_cat.values())) < 3:
        st.error('Please enter proper ingredient list.')
# for each in set(ing_pare_cat.values()):
#     st.button(each)

li = []
for ing, p_c in ing_pare_cat.items():
        if p_c == selected_p_c:
            li.append(ing)
        
# ing_li = ingredient_dict[ingredient_dict['original_ingredient'].isin(li)]['ingredient'].unique().tolist()

# ing_li = [each.title()]
with col_1:
    st.markdown('#### Ingredients from selected categories:')
    st.write(', '.join(li).title())
# for i in ng_li:
#     st.write(i)