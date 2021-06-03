import pandas as pd
import os


#Reads in csv file containing full texts by the 50 most common authors 
#in the dataset and splits the texts into 5 sentence chunks.
def main():
    filename = "top50-full_text.csv"
    x_size = 7

    full = pd.read_csv(filename)
    full = full.sample(frac=1).reset_index(drop=True)
    para = pd.DataFrame(columns=["Author", "Text"])
    counts = {}
    for index, row in full.iterrows():
        name = row['Author']
        if name not in counts:
            counts[name] = 0
        if counts[name] > 800:
            continue
        full_text = row['Text']
        idx = 0
        nl_count = 0
        while idx < len(full_text) and nl_count < 200:
            if full_text[idx] == '\\':
                if full_text[idx + 2] == '\\':
                    idx += 2
                nl_count += 1
            idx += 1

        while idx < len(full_text) - 1000:
            num_sentences = 0
            start = idx
            while idx < len(full_text) - 1000 and num_sentences < x_size:
                if full_text[idx] == '.':
                    num_sentences += 1
                idx += 1
            example = full_text[start : idx]
            para = para.append({"Author": name, "Text": example}, ignore_index=True)
            counts[name] += 1
        
        if index % 10 == 0:
            #print(f"Parsed text by {name} in index {index}.")
            print(f"Index {index}. {counts}")
        if index % 200 == 0:
            para.to_csv("top50-7sentence.csv")

    para.to_csv("top50-7sentence.csv")



if __name__ == "__main__":
    main()
