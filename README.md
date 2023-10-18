# Repository "Credit Risk Detector and Bad Risk Analysis"

## Description
This project aims to reduce the percentage of customers who fail to make payments by predicting whether a customer is a "Bad Risk" or a "Good Risk" using a classification model. Additionally, the project involves a clustering model to assess "Bad Risk" customers. The entire process includes data extraction from PostgreSQL, data cleaning, and validation. Apache Airflow is used to orchestrate and automate the Data Engineering tasks. Furthermore, this project encompasses data analysis to understand common customer characteristics.

## Project Structure
The project consists of several folders and files:

1. `data_engineering/`: This folder contains Apache Airflow DAG files for orchestrating the Data Engineering tasks. 

2. `data_science/`: This folder contains Jupyter Notebook files (`.ipynb`) for the Data Science process. Additionally, there are two inference files:
   - `classification_model.ipynb`: A notebook to train a classification model that predicts "Bad Risk" or "Good Risk."
   - `clustering_model.ipynb`: A notebook to train a clustering model to identify "Bad Risk" customers.
   - `inference_classification.ipynb`: A notebook for making inferences with the classification model.
   - `inference_clustering.ipynb`: A notebook for making inferences with the clustering model.

3. `data_analysis/`: This folder contains notebooks or scripts for the Exploratory Data Analysis (EDA) process used by Data Analysts. Additionally, it includes:
   - `url.txt`: A text file containing a URL link to a Tableau dashboard or visualization.

4. `data/`: This folder contains data required for analysis and modeling, including both raw data from PostgreSQL and cleaned data.

5. `README.md`: This file, which contains documentation about this project.

## Usage Instructions
To use this project, you can follow these steps:

### Data Engineering with Apache Airflow
1. Install and configure Apache Airflow.
2. Place the provided Apache Airflow DAG files from the `data_engineering/` folder into your Airflow DAG folder.
3. Start the Airflow webserver and scheduler.
4. Access the Airflow web interface to trigger and monitor the DAGs to perform data extraction, data cleaning, and data insertion tasks.

### Data Science
1. Open the Jupyter Notebook files in the `data_science/` folder, including `classification_model.ipynb` and `clustering_model.ipynb`, to train the models.
2. For model inference, use `inference_classification.ipynb` and `inference_clustering.ipynb`.

### Data Analysis
For data analysis, you can access the Tableau dashboard or visualization by following the link in `url.txt` in the `data_analysis/` folder.

## Contribution
If you wish to contribute to this project, please follow these guidelines:
1. Fork this repository.
2. Make the necessary changes or additions, especially to the Data Science notebooks in the `data_science/` folder.
3. Create a pull request to merge your changes into the main repository.


## Link Data Set
link : https://www.kaggle.com/datasets/ppb00x/credit-risk-customers

## Contact
If you have any questions or need further assistance, please contact me at hararinetanya@gmail.com

**Happy coding on your project!**
