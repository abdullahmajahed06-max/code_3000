import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    keys = ["age", "zip3", "gender"]

    matches = pd.merge(anon_df, aux_df, on=keys)

    counts = matches["anon_id"].value_counts()
    unique_ids = counts[counts == 1].index

    matches = matches[matches["anon_id"].isin(unique_ids)]

    return matches[["anon_id", "name"]].rename(columns={"name": "matched_name"})


def deanonymization_rate(matches_df, anon_df):
    return len(matches_df) / len(anon_df)