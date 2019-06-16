# EXCEPTION SECTION

## OVERVIEW
### This project focuses on collecting data from different newspapers from a particular region so that an analysis can be made and salient topics can be extracted. These topics can be used to show relevant information about the current trends of that region.

## MODUS OPERANDI

### SCRAPING

Articles pertaining to Bangalore were used for analysis. The required articles were scraped from two different newspapers:
- Deccan Herald
- The Indian Express

Data from August 2018 to June 2019 was scraped, extracted, cleaned and stored in a CSV(Comma Separated Values) format. Special attention was taken to remove duplicates which may have occured while scraping

### MODEL TRAINING AND DATA ANALYSIS

The model used for training and clustering data is LDA(Latent Dirichlet Allocation) whose description can be found [here](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation). Clusters of the topics were formed which were then used to classify each of the articles into a given cluster using [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution) of words in a cluster. Now a frequency table corresponding to each month was created and can be used as a [Supervised Model](https://en.wikipedia.org/wiki/Supervised_learning) for future analysis.

### FRONTEND AND BACKEND

The website was created using Web Technologies. 
For Frontend, the technologies used were:
- HTML5
- CSS3
- JavaScript
- Twitter Bootstrap

For Backend, the technology used was:
- Flask

For data querying, CSV file generated from our model was used. Graphs were plotted using Bokeh Libray in Python and were rendered in the Frontend using Jinga2 Syntax. 
The Graphs used were namely:
- Frequency Distributions corresponding to each month for a given cluster.

### FUTURE SCOPE OF THIS PROJECT

Data of different places can be added and trained using the LDA model. Useful insights, hence, can be generated for those places.

## INSTALLATION NOTES
### Clone or Download this repository. For this project, Flask and Bokeh modules must be installed on the host system. Some issues may arise while running the applications which can be resolved by installing the required version of the modules.

## LICENSE
### The entirity of this project is open source and can be used by anyone. However, proper citation must be made to Exception Section.









