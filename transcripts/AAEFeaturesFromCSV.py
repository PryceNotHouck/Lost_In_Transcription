import pandas as pd

xlsx_path = r"C:\Users\pryce\OneDrive\Desktop\Lost in Transcription\Text Inputs\Samples.xlsx"
csv_path = r"C:\Users\pryce\UFL Dropbox\Pryce Houck\Interviews\AAHP 237 Booker Dwayitan 12-14-2011ufdc (1).csv"
output_path = r"C:\Users\pryce\OneDrive\Desktop\Lost in Transcription\Text Inputs\237_AAE_Features_output.xlsx"

quote_col_xlsx = "Human Transcription"
features_col_xlsx = "AAE Features"
quote_col_csv = "Text"

start_row = 63
end_row = 143

xlsx_df = pd.read_excel(xlsx_path, sheet_name = "Samples")
csv_df = pd.read_csv(csv_path)

feature_cols = [col for col in csv_df.columns if col not in [quote_col_csv]]
quote_to_features = {}
abbreviations = {"Null copula" : "NC",
                 "Person/num. agreement" : "PNA",
                 "Multiple negators" : "MN",
                 "Habitual be" : "HB",
                 "Perfect done" : "PD"}

for _, row in csv_df.iterrows():
    quote = str(row[quote_col_csv]).strip()
    present_features = [abbreviations[abbr] for abbr in feature_cols if row[abbr] == 1]
    if present_features:
        quote_to_features[quote] = ", ".join(present_features)
    else:
        quote_to_features[quote] = ""

for idx in range(start_row, end_row):
    if idx >= len(xlsx_df):
        break
    quote = str(xlsx_df.at[idx, quote_col_xlsx]).strip()
    if quote in quote_to_features:
        xlsx_df.at[idx, features_col_xlsx] = quote_to_features[quote]
    else:
        xlsx_df.at[idx, features_col_xlsx] = ""

xlsx_df.to_excel(output_path, index = False)
