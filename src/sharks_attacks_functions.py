import numpy as np

"""
This function (nameconvention) changes the default columns names into a proper name convention style (snake_case)
Input: a list of strings
This funtion does:
- First: removes spaces before and after the column name
- Second: replaces spaces with an underscore of the column name
- Third: lowers cases of the column name
Output: a dictionary with the old column name as a key and the new one as the value
"""
def nameconvention(columnas):
    diccio_rename = {columna: columna.strip().replace(" ","_").lower() for columna in columnas}
    return diccio_rename







"""
This function (get_dup_columns) finds duplicate columns in a Pandas DataFrame.
Input: dataframe
This funtion does: 
- First: It iterates over DataFrame column wise and for every column it will search if any other column exists in DataFrame with same contents
- Second: If yes then then that column name will be stored in duplicate column list.
Output: In the end API will return the list of column names of duplicate columns 
"""
#source: https://thispointer.com/how-to-find-drop-duplicate-columns-in-a-dataframe-python-pandas/

def get_dup_columns(data):
    duplicateColumnNames = set()
    # Iterate over all the columns in dataframe
    for x in range(data.shape[1]):
        # Select column at xth index.
        col = data.iloc[:, x]
        # Iterate over all the columns in DataFrame from (x+1)th index till end
        for y in range(x + 1, data.shape[1]):
            # Select column at yth index.
            otherCol = data.iloc[:, y]
            # Check if two columns at x 7 y index are equal
            if col.equals(otherCol):
                duplicateColumnNames.add(data.columns.values[y])
 
    return list(duplicateColumnNames)





"""
This function (mpare_rows) detects percentage of similitud among 2 columns 
Input: dataframe (df), dataframe columns(col1), dataframe columns again(col2) 
This funtion does: detects percentage of similitud among 2 columns 
Output: a correlation matrix where you can find the percentage similarity between two columns
"""
def compare_rows(df, col1, col2):
    eq_row = np.where(df[col1] == df[col2], 1, 0).sum()
    rows = df.shape[0] - df[col1].isnull().sum()
    per_row = round((eq_row / rows) * 100,2)
    return per_row


