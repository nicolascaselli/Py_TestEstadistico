import database_connector
import data_fetcher
import mann_whitney_test
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def guardar_resultados_como_csv(resultados, nombre_archivo):
    # Crea un DataFrame de pandas a partir de los resultados
    df = pd.DataFrame(resultados, columns=["Columna1", "Columna2", "OtrasColumnas"])

    # Guarda el DataFrame en un archivo CSV
    df.to_csv(nombre_archivo, index=False)
# Configuración de la base de datos MySQL
db_url = "mysql+pymysql://root:123456789@localhost/pd_dbscan_bat_cec"
MH = {"BA": data_fetcher.get_query_Bat(),
      "PSO": data_fetcher.get_query_PSO(),
      "CSA":data_fetcher.get_query_CSA()
    }
for mh, query in MH.items():

    engine, session = database_connector.connect_to_mysql(db_url)

    # Obtención de datos desde la base de datos
    #data = data_fetcher.fetch_data(session)
    data = pd.read_sql(query, con=engine)
    # Realización del test estadístico de Mann-Whitney U
    col_auto = 'min_'+str(mh).lower()+'_auto'
    col_orig = 'min_'+str(mh).lower()+'_orig'
    funciones = data['function'].unique()
    resultados_df = pd.DataFrame(columns=['Funcion', 'Algoritmos', 'Stat', 'P-Value'] )
    #recorremos las funciones
    for funcion_recorrida in funciones:
        #Extraemos los datos de la primera función
        datos_test = data[data['function'] == funcion_recorrida]
        #Corregimos los outliers
        # Calcula los cuartiles Q1 y Q3, y el rango intercuartílico (IQR) de la columna A
        Q1 = datos_test[col_auto].quantile(0.25)
        Q3 = datos_test[col_auto].quantile(0.75)
        IQR = Q3 - Q1
        # Definir las condiciones para reemplazo
        condicion = (datos_test[col_auto] < (Q1 - 1.5 * IQR)) | (datos_test[col_auto] > (Q3 + 1.5 * IQR))
        # Reemplazar los valores en la columna A con NaN si cumplen con la condición
        datos_test.loc[condicion, col_auto] = datos_test[col_auto].quantile(0.50)
        stat, p_value = mann_whitney_test.perform_mann_whitney_df(datos_test, col_auto, col_orig)
        resultados_df.loc[len(resultados_df)] = [funcion_recorrida, mh+" Auto vs Orig", stat, p_value]
        #graficamos
        datos_grafico = datos_test[[col_auto, col_orig]]
        datos_grafico.columns = ["SWEVOH-"+mh, mh]
        #datos_grafico.plot.box().figure.savefig("Graficos/Box/SWEVOHBA_BA_"+str(funcion_recorrida)+"Box.png")
        sns.violinplot(data=datos_grafico)
        plt.xlabel("Algorithms")
        plt.ylabel("Execution Fit.")
        plt.title("SWEVOH-"+mh+" vs "+mh+" - Function "+str(funcion_recorrida))
        plt.savefig("Graficos/Violin/SWEVOH"+mh+"_"+mh+"_" + str(funcion_recorrida) + "Violin.png")
        plt.close()
    #agregamos la columna con los resultados de la significancia (si es menor a 0.05) del test estadístico
    resultados_df['resultPvalue'] = resultados_df['P-Value'].apply(lambda x: x<= 0.05)
    #guardamos resultados en CSV
    resultados_df.to_csv("ResultadosTestCSV/SWEVO_"+mh+"_VS_"+mh+"ResultadosTestEstadistico.csv")

    # Cierre de la sesión
    session.close()
print("Fin de la ejecución")
