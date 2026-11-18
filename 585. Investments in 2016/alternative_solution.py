import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:

    # Identify policyholders sharing the same TIV in 2015
    shared_tiv_2015 = insurance["tiv_2015"].duplicated(keep=False)

    # Identify policyholders at unique geographical locations
    unique_location = ~insurance[["lat", "lon"]].duplicated(keep=False)

    # Version 1: Calculate sum and explicitly construct the result DataFrame
    # sum_tiv2016 = insurance.loc[
    #     shared_tiv_2015 & unique_location, "tiv_2016"
    # ].sum().round(2)
    # return pd.DataFrame([sum_tiv2016], columns=["tiv_2016"])

    # Version 2: Sum and convert the result directly into a single-row DataFrame
    return (
        insurance.loc[shared_tiv_2015 & unique_location, ["tiv_2016"]]
        .sum()
        .round(2)
        .to_frame()
        .T
    )
