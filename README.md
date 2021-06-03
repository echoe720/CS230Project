# CS230Project
The repository is divided into four different folders.

The parsers/ folder contains all code used to parse the datasets. Some files were used to process texts into a set of training examples, and others were used to set the columns of those datasets into a format that could feed into our models. 

The datasets/ folder contains the datasets that we constructed. In particular, it contains example of sets with different size training examples, such as 1-sentence, 5-sentence, and 10-sentence. For Gutenberg, some datasets we created were not included due to file size restrictions. They could be created by running the parser file.

The graphs/ folder contains some of the graphs and plots that we produced, along with the files that were used to produce those graphs. Note that in the case of the graphs for the RNN architectures, these were produced by a file in the models/ folder.

The models/ folder contains the three models we created in our project. There are two files for the ANN, as the different datasets required slightly different preprocessing. Note that the ANN and RNNs were used on multiple datasets, but the files in their current iterations are just examples of them being used on one dataset. Our manual feature baseline was also created in the same file as the ANN_Gutenberg. You can see commented out lines that were used to do this.
