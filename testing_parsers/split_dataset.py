import pandas as pd

#Splits dataset into training, test, and validation sets (80/10/10 split).
def main():
    filename = "dataset_7sentence.csv"
    df = pd.read_csv(filename)
    split = .2
    
    num_rows = len(df.index)
    print(num_rows)
    df = df.sample(frac=1).reset_index(drop=True)

    test_size = int(num_rows * split / 2)

    df[: test_size].to_csv("test7.csv")
    print("Finished test set.")
    df[test_size : 2 * test_size].to_csv("validation7.csv")
    print("Finished validation set.")
    df[2 * test_size :].to_csv("training7.csv")
    print("Finished!")



if __name__ == "__main__":
    main()
