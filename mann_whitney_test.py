from scipy.stats import mannwhitneyu


def perform_mann_whitney(data, col_auto, col_orig):
    data_auto = [row[col_auto] for row in data]
    data_orig = [row[col_orig] for row in data]

    stat, p_value = mannwhitneyu(data_auto, data_orig)
    return stat, p_value
