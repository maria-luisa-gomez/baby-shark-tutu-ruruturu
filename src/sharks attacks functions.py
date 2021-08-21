"""
This function (nameconvention) changes the default columns names into a proper name convention style (snake_case)
This funtion does:
- First: removes spaces before and after the column name
- Second: replaces spaces with an underscore
- Third: lowers cases
"""
def nameconvention(columnas):
    diccio_rename = {columna: columna.strip().replace(" ","_").lower() for columna in columnas}
    return diccio_rename