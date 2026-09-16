from src.data.cleaner import build_main_table

df = build_main_table()
print(df.columns)
print(df.dtypes["Posting Date"])   # doit afficher datetime64[ns], pas object/str
print("company" in df.columns)      # doit être True
print("company_x" in df.columns)    # doit être False