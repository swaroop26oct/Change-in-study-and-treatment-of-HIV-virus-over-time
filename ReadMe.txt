Step1:

Using the CSV file prepared from the data extraction phase. The csv had extra empty rows. Using "1.Clean CSV code" to remove the empty rows. 

Step2: 
Manually Split the data(CSV files), using excel filters, to two different time framse: Articles published before 2000 and Articles published after 2000

Step3:
For each Files, Created and Saved the Dictionary and Corpus using the Code "1.TopicModeling_Code_Corpus and Dictionary"

Step4: (Used Jupyter NoteBook for this)
Using the Saved Dictionary and Corpus, created an LDA model using gensim library and saved the same

Step5:
Using the saved model, ran the Visualizations using pyLDAvis library


