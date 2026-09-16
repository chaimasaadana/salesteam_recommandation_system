import pandas as pd

from src.data.loader import load_commandes , load_lignes , load_gps

def build_main_table():
    commandes = load_commandes()
    lignes = load_lignes()
    gps = load_gps()

    main_table = lignes.merge(
        commandes,
        left_on="Document No_",
        right_on="No_",
        how="inner"
    )

    main_table["company"] = main_table["company_x"]

    main_table = main_table.drop(columns=["company_x" , "company_y" , "No_"])


    main_table = main_table.merge(
    gps,
    left_on="client_code",
    right_on="clientCode",
    how="left"
    )

    main_table["Posting Date"] = pd.to_datetime(main_table["Posting Date"])

    main_table = main_table.drop(columns=["clientCode"])


    return main_table 
    