import pandas as pd
from sqlalchemy import create_engine

def filtrar_por_fechas(dataframe, columna, fecha_inicio, fecha_fin):
    
    dataframe[columna] = pd.to_datetime(dataframe[columna])
    

    mask = (dataframe[columna] >= fecha_inicio) & (dataframe[columna] <= fecha_fin)
    

    return dataframe.loc[mask]

def generar_reporte(dataframe, filas, columnas, valores, medida):
    
    pivot = pd.pivot_table(
        data=dataframe,
        index=filas,
        columns=columnas,
        values=valores,
        aggfunc=medida,
        fill_value=0
    )
    return pivot

def escribir_en_base_de_datos(dataframe, nombre_tabla, engine, if_exists):
    
    dataframe.to_sql(
        name=nombre_tabla,
        con=engine,
        if_exists=if_exists
    )
    print(f"Tabla '{nombre_tabla}' guardada exitosamente en la base de datos.")