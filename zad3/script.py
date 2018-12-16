import numpy as np
import pandas as pd
from pprint import pprint

def main():
    new_user_attributes = create_new_user()
    print("Losowo utworzony użytkownik:")
    print(new_user_attributes)
    clustering_result = load_clustering_result()
    print(clustering_result)
    result1 = count_AND_operation(new_user_attributes, clustering_result)
    print("Przecięcia:")
    pprint(result1)
    result2 = count_OR_operation(new_user_attributes, clustering_result)
    print("Unie:")
    pprint(result2)
    true_values_result1 = count_true_values_for_columns(result1)
    true_values_result2 = count_true_values_for_columns(result2)
    print("Współczynniki Jaccarda:")
    indicators = count_Jaccard_indicators(true_values_result1, true_values_result2)
    print(indicators)
    print("Najbliższy klaster:")
    closest_cluster_index = found_closest_cluster(indicators)
    print(closest_cluster_index + 1)
    print("Numery zarekomendowanych stron:")
    print(recommend_pages(new_user_attributes, clustering_result[['Cluster '+str(closest_cluster_index)]]))


def create_new_user():
    number_of_attributes = 28
    np.random.seed(0)
    return np.random.choice(a=[False, True], size=(28))
            
def load_clustering_result():
    col_names = ['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5', 'Cluster 6']
    cluster_result = pd.read_csv('cluster_result.txt', names = col_names, sep=',')
    return cluster_result
    # print(cluster_result)

def count_AND_operation(user_attributes, clustering_result):
    result = []

    for i in range(len(clustering_result)):
        row = []
        for j in range(len(clustering_result.columns)):
            row.append(clustering_result.iat[i,j] & user_attributes[i])
        result.append(row)
    
    return result

def count_OR_operation(user_attributes, clustering_result):
    result = []

    for i in range(len(clustering_result)):
        row = []
        for j in range(len(clustering_result.columns)):
            row.append(clustering_result.iat[i,j] | user_attributes[i])
        result.append(row)
    
    return result

def count_true_values_for_columns(array):
    col_counter = len(array[0])
    result = [0] * col_counter
    for i in range(len(array)):
        for j in range(col_counter):
            if(array[i][j] == True):
                result[j] = result[j] + 1

    return result

def count_Jaccard_indicators(result_and, result_or):
    indicators = []
    for i in range(len(result_and)):
        indicators.append(result_and[i]/result_or[i])
    return indicators

def found_closest_cluster(indicators):
    max = 0
    for i in range(len(indicators)):
        if (indicators[i] > max):
            max = indicators[i]
    
    for i in range(len(indicators)):
        if (indicators[i] == max):
            return i

def recommend_pages(user_attributes, closest_cluster_result):
    pages = []
    print(type(closest_cluster_result))

    for i, row in closest_cluster_result.iterrows():
        if ((user_attributes[i] == False) & (row.bool() == True )):
            pages.append(i)



    # for i in range(len(user_attributes)):
    #     

    return pages


if __name__ == '__main__':
    main()

