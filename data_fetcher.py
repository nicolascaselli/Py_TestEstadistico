from sqlalchemy import text
def fetch_data(session):
    query = text("""
    SELECT
        ba_a.function,
        ba_a.ejecution,
        min(ba_a.fitness) as min_ba_auto,
        min(ba_orig.fitness) as min_ba_orig
    FROM cec_results_bat_autonomo as ba_a, cec_results_bat_original as ba_orig
    WHERE ba_a.function = ba_orig.function AND ba_a.ejecution = ba_orig.ejecution
    GROUP BY ba_a.function, ba_a.ejecution
    """)
    result = session.execute(query)
    return result.fetchall()
