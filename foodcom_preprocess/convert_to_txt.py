import pandas as pd


def create_txt_file(start: int, end: int):
    df = pd.read_csv('converted_ds/steps_and_ingredients.csv')

    with open(f'converted_ds/steps_and_ingredients_{start}_{end}.txt', 'w') as fobj:
        for index, row in df.iterrows():
            if start > index >= end:
                break
            steps_str = row['steps_str']
            fobj.write(steps_str + '.\n')


if __name__ == '__main__':
    create_txt_file(0, 1000)  # get first 1K steps
