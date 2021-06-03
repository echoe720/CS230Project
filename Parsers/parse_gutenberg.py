import pandas as pd
import os
import heapq

#Parses texts by the 50 most common authors into a csv file.
def main():
    dirname = "txt"
    df = pd.DataFrame(columns=["Author", "Text"])
    mapping = {}
    for filename in os.listdir(dirname):
        if filename.endswith(".txt"): 
            with open(f"{dirname}/{filename}", "rb") as f:
                text = f.read()
                author = filename[:filename.find("_")]
                if author in mapping:
                    mapping[author] += 1
                else:
                    mapping[author] = 1
                df = df.append({"Author": author, "Text": text}, ignore_index=True)
                f.close()
    
    names = []
    for author, count in mapping.items():
        names.append((author, count))

    def foo(entry):
        return entry[1]

    names.sort(reverse=True,key=foo)
    print(names[:50]) 

    top50 = []
    for i in range(50):
        if i >= len(names):
            break
        top50.append(names[i][0])

    df.sort_values(by=['Author'])
    
    author_count = {}
    for name in top50:
        author_count[name] = 0

    for index, row in df.iterrows():
        name = row['Author']
        if name in top50:
            author_count[name] += 1
        if name not in top50 or author_count[name] > 22:
            df.drop(index, inplace=True)
        
    
    df = df.sort_values(by=['Author'])
    df.to_csv("top50-22-full_text.csv")
    


if __name__ == "__main__":
    main()
