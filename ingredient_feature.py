import streamlit as st
import pandas as pd
import numpy as np
import utils_ingredients_cats
from utils_ingredients_cats import *
import utils_ingredients_dogs
from utils_ingredients_dogs import *
st.set_page_config(layout="wide")

ingredient_dict = pd.read_csv("ingredient_names_dictionary_17_01_23.csv", sep = '|')

col_1, space, col_2 = st.columns([2,0.2,0.9])


with col_1:
    st.markdown('#### Enter Ingredient List:')
    ing_str = st.text_area('Enter Ingredient List:', height= 220,  label_visibility = 'collapsed')
    ing_str = ing_str.lower()
    # st.write(ing_str)
    # ing_str = re.sub(r'\!', ' ', ing_str)
    # ing_str = re.sub(r'\n[\w+\s*\!*\?*\&*\s*\'*\"*\-*\`*\,*]+\:', ', ', ing_str)
    # ing_str = re.sub(r'\.\,', ',', ing_str)
    # ing_str = re.sub(r'\;', '', ing_str)

    # st.write(ing_str)

    if ing_str == '':
        st.error('Please enter the ingredient list.')
        ing_str ='.'
    ing_str_list = []
    ing_str_list.extend(ing_str.split('\n'))
    # st.write(ing_str_list)

# st.write(ing_str_list)

cleaning_function = [ingredients_initial_cleaning_cat_wet, ingredients_initial_cleaning_cat_dry,
                     ingredients_initial_cleaning_cat_raw, ingredients_initial_cleaning_cat_vet,
                     ingredients_initial_cleaning_dog_wet, ingredients_cleaning_dog_vet,
                     ingredients_cleaning_dog_raw, ingredients_cleaning_dog_dry]

# for each in ing_str_list:
#     st.write(each.split(":"))
flavor = [each.split(': ')[0].strip() if ': ' in each else '' for each in ing_str_list]
ing_str_list = [each.split(': ')[1].strip() if ': ' in each else each for each in ing_str_list]

if len(ing_str_list) > 1 :
    for each in ing_str_list:
        
        if each == '':
            ing_str_list.remove("")
            
    for each in flavor:
        if each == '':
            flavor.remove("")

    
for func in cleaning_function:
        
    new_product_wise_ingredients = func(ing_str_list)
    set_of_already_corrected_ingredient_names=set(ingredient_dict['original_ingredient'])
    
    set_of_current_ingredients=set(new_product_wise_ingredients[0])
    new_ingre = len(set_of_current_ingredients-set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients))
    remaining_set = set_of_current_ingredients-set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients)

    if (np.nan in remaining_set and '' in remaining_set and len(remaining_set)==2) or (len(remaining_set)==0):
        break
    

ing_1= {}
for ing, fla in zip(new_product_wise_ingredients, flavor):
    # st.write(fla)
    ing_pare_cat = {}
    for each in ing:
        if each in ingredient_dict['original_ingredient'].unique().tolist():
            parent_cat = (ingredient_dict[ingredient_dict['original_ingredient'] == each.lower()]['new_ingredient_parent_category'].unique()[0])
            sub_cat = (ingredient_dict[ingredient_dict['original_ingredient'] == each.lower()]['new_ingredient_sub_category'].unique()[0])
            ing_pare_cat[each] = parent_cat.capitalize()
    ing_1[fla.title()] = ing_pare_cat
        
# st.write(ing_1) 

p_set = set()
for each in ing_1.values():
    for i in each.values():
        p_set.add(i)
    
# st.write(p_set)
    
with col_2:
    st.markdown('#### Selected Category:')
    selected_p_c = st.radio('Selected Category:', p_set, label_visibility = 'collapsed')



li_1 = {}
for key, value in ing_1.items():
    li = []
    for ing, p_c in value.items():
            if p_c == selected_p_c:
                li.append(ing)
    li_1[key] = li
# st.write(li_1)

with col_1:
    st.markdown('#### Ingredients from selected categories:')
    for key, value in li_1.items():
        if key == '':
            st.write(', '.join(value).title())
        else:
            st.markdown(f"###### {key}: ")
            st.write(', '.join(value).title())
