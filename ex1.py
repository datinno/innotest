import numpy as np
import pandas as pd

data = {
    "t": [
        "2023-05-1",
        "2023-05-2",
        "2023-05-3",
        "2023-05-4",
        "2023-05-5",
        "2023-05-6",
        "2023-05-7",
        "2023-05-8",
        "2023-05-9",
        "2023-05-10",
        "2023-05-11",
        "2023-05-12",
        "2023-05-13",
        "2023-05-14",
        "2023-05-15"
    ],
    "o": [
        1207.42,
        1211.77,
        1230.38,
        1252.05,
        1246.12,
        1241.59,
        1235.59,
        1245.06,
        1244.31,
        1240.88,
        1257.81,
        1240.54,
        1178.52,
        1192.11,
        1206.61
    ],
    "h": [
        1223.94,
        1231.42,
        1250.68,
        1254.21,
        1248.52,
        1243.16,
        1240.77,
        1245.96,
        1244.62,
        1257.57,
        1259.50,
        1243.69,
        1178.53,
        1195.97,
        1207.84
    ],
    "l": [
        1207.43,
        1211.77,
        1230.38,
        1243.84,
        1235.87,
        1225.00,
        1221.03,
        1234.41,
        1236.55,
        1240.88,
        1247.82,
        1187.03,
        1178.54,
        1158.60,
        1191.69
    ],
    "c": [
        1210.80,
        1231.42,
        1250.68,
        -2,
        1239.84,
        1226.20,
        1240.77,
        1243.43,
        1241.24,
        1256.95,
        1247.82,
        1190.10,
        1190.32,
        1193.51,
        1192.59
    ],
    "v": [
        264562500.0,
        321004800.0,
        284030100.0,
        232457500.0,
        249111600.0,
        204527400.0,
        234807300.0,
        228144000.0,
        185981200.0,
        248293000.0,
        281533700.0,
        424012300.0,
        259164600.0,
        266991500.0,
        -1
    ],
}

df = pd.DataFrame.from_dict(data)

df.set_index("t", inplace=True)


def Check1(df: pd.DataFrame):
    result = []

    cols = ['o', 'h', 'l', 'c', 'v']

    filter_df =  df[df[cols]<0].dropna(how="all").dropna(axis=1, how="all")


    for index in filter_df.index:
        for col in filter_df.columns:
            value = filter_df.loc[index, col]
            if not np.isnan(value):
                result.append((index, col, value))
    return result

def Check2(df: pd.DataFrame):

    def appendValue(df: pd.DataFrame, how: str):
        for index in df.index:
            new_cols.setdefault(index, []).append(how)

    new_cols = {}

    # Check l <= o,h,c
    for col in ['o', 'h', 'c']:
        check_df =  df[df['l'] > df[col]]
        how = f"l > {col}"
        appendValue(check_df, how=how)

    # Check h >= o,c
    for col in ['o', 'c']:
        check_df =  df[df['h'] < df[col]]
        how = f"h < {col}"
        appendValue(check_df, how=how)

    df['error'] = new_cols
    df.dropna(inplace=True, subset=["error"])

    return df

result = Check2(df)

print(result)
