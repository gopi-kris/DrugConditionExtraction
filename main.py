from extract_text_from_pdf import remove_small_words
from query_mesh import create_drug_dataframe, check_drug_in_results, combine_sparql_conditions_dataframe, check_condition_in_results

"""
Run this file to obtain initial results. Filter the results further using the word_list_term column to obtain final results.
"""

if __name__ == '__main__':
    remove_small_words()
    create_drug_dataframe()
    check_drug_in_results()
    combine_sparql_conditions_dataframe()
    check_condition_in_results()
