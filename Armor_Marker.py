import pandas as pd
import os

def checkForBetter(data):
    condition =\
            (df["Type"] == data["Type"]) &\
            (df["Id"] != data["Id"]) &\
            (df["Tier"] == data["Tier"]) &\
            (df["Equippable"] == data["Equippable"]) &\
            (df["Resilience (Base)"] >= data["Resilience (Base)"]) &\
            (df["Recovery (Base)"] >= data["Recovery (Base)"]) &\
            (df["Discipline (Base)"] >= data["Discipline (Base)"]) &\
            (df["Intellect (Base)"] >= data["Intellect (Base)"]) &\
            (df["Strength (Base)"] >= data["Strength (Base)"])

    if data["Equippable"]=="Hunter":
        condition = condition&(df["Mobility (Base)"] >= data["Mobility (Base)"])

    processed = df[condition]
    if(not processed.empty):
        print("--------------------------------------")
        print(data[['Name']].to_string(index=False, header=False), data[['Id']].to_string(index=False, header=False))
        print(processed[['Name']].to_string(index=False, header=False), processed[['Id']].to_string(index=False, header=False))
    return

if __name__ == '__main__':
    global df
    if os.path.exists(os.getcwd()+"\destinyArmor.csv"):
        df = pd.read_csv ((os.getcwd()+"\destinyArmor.csv"),\
            usecols=['Name','Id','Type','Equippable','Mobility (Base)','Resilience (Base)','Recovery (Base)','Discipline (Base)','Intellect (Base)','Strength (Base)', 'Tier', 'Tag'])
        condition =\
                (df["Tier"] != "Exotic") &\
                (pd.isna(df["Tag"])) &\
                (df["Type"] != "Titan Mark") &\
                (df["Type"] != "Warlock Bond") &\
                (df["Type"] != "Hunter Cloak")
        df[condition].apply(checkForBetter, axis=1)
        input('Press ENTER to exit')
    else:
        input('destinyArmor.csv not found. Press ENTER to exit.')