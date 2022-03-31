#!/usr/bin/env python3
import pandas as pd
import sys

def hero_attributes_per_team(match, hero_data):
    """Convenience function that adds hero attributes.
    Returns a dataframe with 10 new columns.
    """

    # Initialize empty series (basically an ordered dictionary)
    att = pd.Series(data={
        "radiant_str" : 0.0,
        "radiant_int" : 0.0,
        "radiant_agi" : 0.0,
        "radiant_melee": 0.0,
        "radiant_ranged": 0.0,
        "dire_str" : 0.0,
        "dire_int" : 0.0,
        "dire_agi" : 0.0,
        "dire_melee": 0.0,
        "dire_ranged": 0.0,
    })    

    # Filter on Radiant and select column of interest:
    attributes_radiant = hero_data.loc[match[match == 1].index.tolist()]['PrimaryAttribute'].values
    attack_type_radiant = hero_data.loc[match[match == 1].index.tolist()]['AttackType'].values

    # Filter on Dire and select column of interest:
    attributes_dire = hero_data.loc[match[match == -1].index.tolist()]['PrimaryAttribute'].values
    attack_type_dire = hero_data.loc[match[match == -1].index.tolist()]['AttackType'].values

    # Merge the two lists and iterate over them:
    # Add a value if we found the category
    for val in [*attributes_radiant, *attack_type_radiant]:
        if val == "Intelligence":
            att['radiant_int'] += 0.2
        if val == "Agility":
            att['radiant_agi'] += 0.2
        if val == "Strength":
            att['radiant_str'] += 0.2
        if val == "Melee":
            att['radiant_melee'] += 0.2
        if val == "Ranged":
            att['radiant_ranged'] += 0.2

    # Merge the two lists and iterate over them:
    # Add a value if we found the category
    for val in [*attributes_dire, *attack_type_dire]:
        if val == "Intelligence":
            att['dire_int'] += 0.2
        if val == "Agility":
            att['dire_agi'] += 0.2
        if val == "Strength":
            att['dire_str'] += 0.2
        if val == "Melee":
            att['dire_melee'] += 0.2
        if val == "Ranged":
            att['dire_ranged'] += 0.2

    return att


def main():
    if len(sys.argv) != 4:
        print("Invalid number of arguments! This script expects three arguments!\n", file=sys.stderr)
        print("Usage:", file=sys.stderr)
        print("add_hero_attributes.py <match_info> <hero_attributes> <output>", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print("python src/models/add_hero_attributes.py data/jan_2021_to_feb_2022_linear_output.csv data/hero_attributes.txt jan_2021_to_feb_2022_linear_output_with_attributes.txt\n\n", file=sys.stderr)
    else:
        match_file = sys.argv[1]
        hero_file = sys.argv[2]
        output = sys.argv[3]

        # Load files:
        match_data = pd.read_csv(match_file)
        hero_data = pd.read_csv(hero_file, sep="\t", index_col=0)

        # Drop unneeded columns for a bit:
        match_data2 = match_data.drop(['match_result', 'match_id'], axis=1)
        
        # Add hero attributes:
        res = match_data2.apply(lambda x: hero_attributes_per_team(x, hero_data), axis=1)

        # Column concat the two dataframes:
        match_data_with_att = pd.concat([match_data, res], axis=1).reindex(match_data.index)

        # Write result to file:
        match_data_with_att.to_csv(output, sep=",", index=False)

    

if __name__ == "__main__":
    main()