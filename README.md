# CS230Project
Milestone.zip contains all code used to parse the Gutenberg dataset into our final dataset, as well as the notebook for our baseline model.
The notebook CountVectorizer Baseline.ipynb file loads the Gutenberg dataset, and then runs our baseline model on it. 
There is commented out code that would change the baseline to use manual features instead.
The other file contains our preliminary attempts at implementing a GRU/LSTM method.

The C50parser.ipynb file parses the C50 dataset into format of sentence-to-authorName, 5-sentence-to-authorName, etc., depending on the number of sentences parameter you give it.

Each of the file name indicates what each file does (e.g. lstm_gru_bilstm.ipynb contains the model with lstm, gru, bilstm networks)

Note: Much of the Gutenberg datasets had to be either zipped or not included in this repository, due to their size. But using the Gutenberg parser, the larger datasets desired could be made simply by changing the number of sentences paramter.
