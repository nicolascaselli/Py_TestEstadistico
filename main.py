import database_connector
import data_fetcher
import mann_whitney_test

# Configuración de la base de datos MySQL
db_url = "mysql+pymysql://root:123456789@localhost/pd_dbscan_bat_cec"

engine, session = database_connector.connect_to_mysql(db_url)

# Obtención de datos desde la base de datos
data = data_fetcher.fetch_data(session)

# Realización del test estadístico de Mann-Whitney U
col_auto = 'min_ba_auto'
col_orig = 'min_ba_orig'

stat, p_value = mann_whitney_test.perform_mann_whitney(data, col_auto, col_orig)

print(f"Estadístico U de Mann-Whitney: {stat}")
print(f"Valor p: {p_value}")

# Cierre de la sesión
session.close()
