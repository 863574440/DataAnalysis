from efficient_apriori import apriori
import csv


def load_data(path):
    lists = csv.reader(open(path, "r", encoding='utf-8'))
    data = []
    for names in lists:
        name_new = []
        if names:
            for name in names:
                name_new.append(name.strip())
            data.append(tuple(name_new[1:]))

    return data


def train_model(data):
    itemsets, rules = apriori(data, min_support=0.05, min_confidence=1)
    print(itemsets)
    print(rules)


def main():
    path = './data/data.csv'
    data = load_data(path)
    train_model(data)


if __name__ == '__main__':
    main()
