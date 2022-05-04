# Natural Language Processing for Symptom Detection in Unstructured Provider-Patient Conversation
## Anisha Agarwal, Tiana Cui, Carlo Duffy and Pranav Murugan 
##6.871 Final Project Repository

## Instructions for Use:

### Bag of Words

### Processing 
  - Run bow_processing.py to obtain count-vectorized representations of each turn, which will be saved in `cv_data.csv`
  - This step is necessary for running Logistic Regression and XGBoost 

### XGBoost 
  - Open bow_xgb.ipynb, clear instructions for how to load and train the data exist within the notebook
  - Fitted model will be saved in `xgb_bin.pkl`

### LSTM
  - Open LSTM_and_figures.ipynb, instructions on how to load data are in the notebook
  - The first section contains code and instructions on how to train and evaluate the LSTM classifier
  - Second section has code and instructions for making ROC and performance-recall plots for all models with bootstrapped confidence intervals
  
### BERT 
  - Open bow_xgb.ipynb, clear instructions for how to load and train the data exist within the notebook
  - Fitted model will be saved in `bert_nn.h5`
  - Note that we trained BERT on Google Colab, so code for reading/mounting/saving may need to be adjusted if you are to run this on a local machine

### BioBERT:
  - Open BioBERT_Implementation.ipynb, clear instructions for how to load and train the data exist within the notebook
