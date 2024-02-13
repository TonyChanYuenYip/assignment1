import sys
import pandas as pd

def clean_data(in1, in2, out1):
    df1 = pd.read_csv(in1)
    df2 = pd.read_csv(in2)

    clean = pd.merge(df1, df2, left_on = 'respondent_id', right_on = 'id')
    clean.drop(columns = ['id'], inplace = True)
    clean.dropna(inplace = True)
    clean = clean[~ clean['job'].str.contains('insurance', case = False)]
    clean.to_csv(out1, index = False)

    df_shape = clean.shape
    print("File Shape:", df_shape)

if __name__ == "__main__":
    input1, input2, output = sys.argv[1], sys.argv[2], sys.argv[3]
    clean_data(input1, input2, output)
