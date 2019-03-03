import pandas as pd


def wash_data():
    data = pd.read_excel("./data/data.xlsx")
    data["food"] = data["food"].str.capitalize()  # 首字母大写
    data.fillna(0, inplace=True)
    data.drop_duplicates("food", inplace=True)  # 删除重复行

    data.to_excel("./data/re_data.xlsx")


if __name__ == '__main__':
    wash_data()
