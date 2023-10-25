from scipy.stats import mannwhitneyu


def perform_mann_whitney(data, col_auto, col_orig):
    data_auto = [row[col_auto] for row in data]
    data_orig = [row[col_orig] for row in data]

    stat, p_value = mannwhitneyu(data_auto, data_orig)
    return stat, p_value

def perform_mann_whitney_df(data, col_auto, col_orig):
    '''
    Recibe los datos en un DataFrame de Pandas
    :param data: DataFrame con datos
    :param col_auto: nombre de columna con datos de autónomo
    :param col_orig: nombre de columna con datos de original
    :return: stat y p_value de test estadístico Mann-Whitney
    '''
    data_auto = data[col_auto].values
    data_orig = data[col_orig].values

    stat, p_value = mannwhitneyu(data_auto, data_orig)
    return stat, p_value
