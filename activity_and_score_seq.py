#!/usr/bin/env python3
import pandas as pd
import re
import sys
from Bio.Align import substitution_matrices

'''This script takes data from a csv file and using pandas and python3, makes a dataframe, makes calculations on that dataframe, sorts that dataframe, and builds a dictionary based on that dataframe. We used as an example data from doi.org/10.7554/eLife.5988 looing at human TRIM5a vs HIV-1.'''

def parse_dataset(url_csv):
    #create a dataframe (df) from a csv file
    # dms = pd.read_csv("testdata.csv") #this was for testing
    dms = pd.read_csv(url_csv) #could replace with sys.argv[1]

    #create version of data with only sequence and the functional data
    data = dms[['seq_aa', 'InputA', 'InputB', 'SortA', 'SortB']]
    
    #search for just those rows that have GnnnnnYQVNF
    pattern = re.compile(r"G.{5}YQTFV", re.IGNORECASE)

    filtered_data = data[data['seq_aa'].str.contains(pattern, na=False, regex = True)]
    #case=False is case-insensitive
    #na=False treats missing values as not matching
    #regex = True says the pattern is a regex 

    #remove those rows that have Input Values of 0 (can't divide by 0)
    # all means either input as 0 is removed
    columns_to_check = ['InputA', 'InputB']
    mask = (filtered_data[columns_to_check] != 0).all(axis=1)
    clean_data = filtered_data[mask].copy()

    #calculate the Enrichment and average Enrichment, which I am calling Activity
    clean_data["EnrichA"] = clean_data["SortA"] / clean_data["InputA"]
    clean_data["EnrichB"] = clean_data["SortB"] / clean_data["InputB"]
    clean_data["Activity"] = (clean_data["EnrichA"]+clean_data["EnrichB"])/2

    #Clean up the Activity to 3 decimal places
    clean_data["Activity"] = clean_data["Activity"].round(decimals = 3)

    #Sort the data based on Enrichment - highest to lowest
    sorted_data = clean_data.sort_values(by="Activity", ascending = False)

    #df with the data we need - sequence and Enrichment
    game_dataset = sorted_data[['seq_aa', 'Activity']].copy()

    # Writes the df to a new csv file
    # game_dataset.to_csv("dms_df.csv", index=False)

    return game_dataset

#Calculate similarity scores
#see count_score(peak,seq)
#Peak is GERGTRYQTFVNF with Activity of 21.200
def sim_score(seq):
    peak = 'GERGTRYQTFVNF'
    score=0
    matrix=substitution_matrices.load("BLOSUM62")
    for i in range(len(peak)):
        aa_1=peak[i]
        aa_2=seq[i]
        if aa_1==aa_2:
            continue
        else:
            try:
                score+=matrix[(aa_1,aa_2)]
            except:
                score+=matrix[(aa_2,aa_1)]
                # print(i)
    return score


def score_act_dict():
    url_csv = "https://raw.githubusercontent.com/jtenthor/T5DMS_data_analysis/refs/heads/master/Data/Hs-HIV1_summary.csv"

    game_dataset = parse_dataset(url_csv)

    # print(game_dataset)

    # creates dictionary with seq as key and Activity as values
    # dms_dict = pd.Series(game_dataset["Activity"].values, index=game_dataset['seq_aa']).to_dict()

    # uses BLOSUM62 to figure out Score for each seq_aa
    game_dataset['Score'] = game_dataset['seq_aa'].apply(sim_score)

    # creates dictionary with seq as key and [Activity, Score] as values
    dict_withScoreAct = {}
    for index, row in game_dataset.iterrows():
        key = row['seq_aa']
        value_list = [row['Score'], row['Activity']]
        
        if key not in dict_withScoreAct:
            dict_withScoreAct[key] = [value_list]
        #else:
            #dms_dict_withScore[key].append(value_list)

    return dict_withScoreAct

if __name__ == "__main__":
    main()
    




    


    #Writes the dict to a new tsv file
    # with open("dms_dict.tsv", "w") as file: #check name of file!
    #     for k, v in dms_dict.items(): #check name of dictionary!
    #         file.write(F"{k}\t{v}\n")

    # #takes the tsv file and creates a dictionary
    # game_dict = {}
    # with open("dms_dict.tsv", "r") as file: #check name of file!
    #     for line in file: #check name of dictionary!
    #         line = line.rstrip()
    #         seq_aa,average = line.split('\t')
    #         game_dict[seq_aa] = average



