import pandas as pd
import ast


def get_lst(lst):
    return ast.literal_eval(lst)


char = '. '


def get_str_steps(x):
    return char.join(get_lst(x)).replace(' , ', ', ')


def main():
    df = pd.read_csv('../datasets/food.com_dataset/RAW_recipes.csv')

    df['steps_str'] = df['steps'].apply(get_str_steps)
    df['ingredients_str'] = df['ingredients'].apply(lambda x: ','.join(get_lst(x)))
    df[['steps_str', 'ingredients_str']].to_csv('converted_ds/steps_and_ingredients.csv', index=False)


if __name__ == '__main__':
    main()
