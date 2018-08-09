1. Extract the data from Entrez database using the "1.data_extraction.py" script. 
2. Run the "2.xml_to_subsets_data.py" script in the same directory as the extracted xml files.
	Copy the files created and paste it in the the directory where geniass was downloaded
3. Download the genia Sentence splitter api.
	Follow the geniass README file in the geniass folder to split the abstract text into sentences.
	The sentences obtained should be copied to the folder where we will execute the next steps.

Used ipython notebook to execute the following scripts
4. Sentence tokenization,building Word2Vec and using t-SNE to plot is done using "4.Tokenization_Word2Vec_t-SNE.ipynb"
	The script "4.Tokenization_Word2Vec_t-SNE.ipynb" should be performed for all the time periods individually.
	Once the word2vec model is trained we can load the model and then perform the plotting of t-sne to reduce time consuption. 

5. "model_saved" folder will be created after running "4.Tokenization_Word2Vec_t-SNE.ipynb" and contains the trained word2vec model.