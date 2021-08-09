from SPARQLWrapper import SPARQLWrapper, JSON
from query import drug_query, muscular_conditions_query, nervous_conditions_query
import pandas as pd
from extract_text_from_pdf import data_dir, print_options

print_options()


def base_sparql_url():
    """
    Create a string for the SPARQL endpoint
    :return: String
    """
    repository_prefix = 'http'
    repository_hostname = 'localhost'
    repository_port = '7200'
    repository_name = 'mesh'
    sparql_url_string = f"{repository_prefix}://{repository_hostname}:{repository_port}/repositories/{repository_name}"
    return sparql_url_string


def create_drug_dataframe():
    """
    Creates a dataframe with results from SPARQL query for drugs
    :return: Dataframe pickle file
    """
    sparql = SPARQLWrapper(base_sparql_url())
    sparql.setQuery(drug_query)
    sparql.setReturnFormat(JSON)
    sparql_return = sparql.query().convert()
    results = sparql_return['results']['bindings']
    data = {
        'drug_uri': [],
        'drug_label': [],
        'mesh_id': []
    }
    for result in results:
        data['drug_uri'].append(result['drug']['value'])
        data['drug_label'].append(result['Label']['value'])
        data['mesh_id'].append(result['identifier']['value'])
    df = pd.DataFrame(data=data)
    df.to_pickle(str(data_dir / 'drug_sparql_results.pkl'))


def check_drug_in_results():
    """
    Check if the words obtained from the paper exist in the dataframe
    :return: CSV file with initial results
    """
    publication_word_list = pd.read_pickle(data_dir / 'word_list.pkl')
    drug_df = pd.read_pickle(data_dir / 'drug_sparql_results.pkl')
    drug_df['drug_label'] = drug_df['drug_label'].str.lower()
    drug_df['word_list_term'] = ''
    df_list = []
    for index, row in publication_word_list.iterrows():
        word = row['word_list']
        df = drug_df[drug_df['drug_label'].str.contains(word)].copy()
        df['word_list_term'] = word
        if len(df) > 0:
            first_row = df.head(1)
            df_list.append(first_row)
    combined_df = pd.concat(df_list).reset_index(drop=True)
    combined_df.to_csv(str(data_dir / 'initial_drug_list.csv'), index=False)


def create_conditions_dataframe(query):
    """
    Creates a dataframe with results from SPARQL query for conditions
    :return: Dataframe
    """
    sparql = SPARQLWrapper(base_sparql_url())
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    sparql_return = sparql.query().convert()
    results = sparql_return['results']['bindings']
    data = {
        'condition_uri': [],
        'condition_label': [],
        'mesh_id': []
    }
    for result in results:
        data['condition_uri'].append(result['condition']['value'])
        data['condition_label'].append(result['Label']['value'])
        data['mesh_id'].append(result['identifier']['value'])
    df = pd.DataFrame(data=data)
    return df


def combine_sparql_conditions_dataframe():
    """
    Combines 2 different dataframes into a single dataframe combining Nervous and Musculoskeletal conditions
    :return: Dataframe pickle
    """
    df_1 = create_conditions_dataframe(query=muscular_conditions_query)
    df_2 = create_conditions_dataframe(query=nervous_conditions_query)
    df_list = [df_1, df_2]
    combined_df = pd.concat(df_list).reset_index(drop=True)
    combined_df.to_pickle(str(data_dir / 'condition_sparql_results.pkl'))


def check_condition_in_results():
    """
    Check if the words obtained from the paper exist in the dataframe
    :return: CSV file with initial results
    """
    publication_word_list = pd.read_pickle(data_dir / 'word_list.pkl')
    condition_df = pd.read_pickle(data_dir / 'condition_sparql_results.pkl')
    condition_df['condition_label'] = condition_df['condition_label'].str.lower()
    condition_df['word_list_term'] = ''
    df_list = []
    for index, row in publication_word_list.iterrows():
        word = row['word_list']
        df = condition_df[condition_df['condition_label'].str.contains(word)].copy()
        df['word_list_term'] = word
        if len(df) > 0:
            first_row = df.head(5)
            df_list.append(first_row)
    combined_df = pd.concat(df_list).reset_index(drop=True)
    combined_df.to_csv(str(data_dir / 'initial_condition_list.csv'), index=False)


if __name__ == '__main__':
    create_drug_dataframe()
    check_drug_in_results()
    combine_sparql_conditions_dataframe()
    check_condition_in_results()
