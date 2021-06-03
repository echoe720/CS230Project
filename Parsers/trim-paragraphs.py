import pandas as pd

#Reads in csv of authors to paragraphs and preprocesses paragraphs
#before putting 10,000 paragraphs for each author into a csv file.
def main():
    filename = "top50-7sentence.csv"
    df = pd.read_csv(filename)
    counts = {}
    final = pd.DataFrame(columns=["Author", "Text"])
    num_rows = len(df.index)
    for index, row in df.iterrows():
        name = row['Author']
        if name in counts.keys():
            counts[name] += 1
        else:
            counts[name] = 1
            print(f"Reached books by {name}.")
        if counts[name] > 500: #49 of 50 authors have 9500 or more paragraphs, so 10000 per author was chosen.
            continue
        paragraph = row['Text']
        #if len(paragraph) < 100 or paragraph.find("..") != -1 or paragraph.find("     ") != -1:
            #counts[name] -= 1
            #continue
        if counts[name] == 1:
            paragraph = paragraph[1:]
        paragraph = paragraph.replace("\\r\\n", " ")
        paragraph = paragraph.replace("\\", "")
        final = final.append({"Author": name, "Text": paragraph}, ignore_index=True)
        if index % 20000 == 0:
            final.to_csv("dataset_7sentence.csv")
            print(f"{round(100 * index / num_rows, 2)}% done.")

    print(counts)
    print(min(counts.items(), key=lambda x: x[1]) )
    print({k: v for k, v in sorted(counts.items(), key=lambda item: item[1])})

    final.to_csv("dataset_7sentence.csv")








if __name__ == "__main__":
    main()
