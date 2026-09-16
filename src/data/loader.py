import pandas as pd
RAW_PATH = "data/raw"

def load_commandes() : 
    return pd.read_excel(f"{RAW_PATH}/commandes.xlsx")

def load_lignes():
    return pd.read_excel(f"{RAW_PATH}/lignes.xlsx")

def load_gps():
    return pd.read_excel(f"{RAW_PATH}/gps.xlsx")
