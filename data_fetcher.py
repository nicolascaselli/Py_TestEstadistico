from sqlalchemy import text
def fetch_data_Bat(session):
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

def get_query_Bat():
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
    return query

def get_query_PSO():
    query = text("""
        select
                pso_a.function
            , pso_a.ejecution
            , min(pso_a.fitness) as min_pso_auto
            , min(pso_orig.fitness) as min_pso_orig
        from cec_results_cs_autonomo as pso_a,
             cec_results_cs_original as pso_orig
        where pso_a.function = pso_orig.function
        and pso_a.ejecution = pso_orig.ejecution
        group by pso_a.function, pso_a.ejecution
""")
    return query

def get_query_CSA():
    query = text("""
     select
	csa_a.function
    , csa_a.ejecution
    , min(csa_a.fitness) as min_csa_auto
    , min(csa_orig.fitness) as min_csa_orig
from cec_results_cs_autonomo as csa_a,
     cec_results_cs_original as csa_orig
where csa_a.function = csa_orig.function
and csa_a.ejecution = csa_orig.ejecution
group by csa_a.function, csa_a.ejecution
     """)
    return query
