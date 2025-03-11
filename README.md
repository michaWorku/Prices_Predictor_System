# **Price Predictor System: End-to-End Machine Learning Pipeline with MLOps**

Welcome to the **Price Predictor System**! This project is designed to predict prices (e.g., house prices, product prices) using a structured, reproducible, and scalable machine learning (ML) pipeline. The project emphasizes **best practices** in both **core ML** and **MLOps**, making it a great example for building production-ready ML systems.


## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Installation and Setup](#installation-and-setup)
4. [Pipeline Design](#pipeline-design)
5. [How to Run the Pipeline](#how-to-run-the-pipeline)
6. [Experiment Tracking with MLflow](#experiment-tracking-with-mlflow)
7. [Model Deployment](#model-deployment)
8. [Contributing](#contributing)
9. [License](#license)


## **Project Overview**

The **Price Predictor System** is an end-to-end ML project that demonstrates how to build, train, evaluate, and deploy a machine learning model for price prediction. The project uses **ZenML** for pipeline orchestration and **MLflow** for experiment tracking and model deployment. The pipeline is modular, scalable, and reproducible, making it a great template for other ML projects.

### **Key Objectives**
- **Data Handling**: Ingest and preprocess data from various sources.
- **Exploratory Data Analysis (EDA)**: Understand the dataset and identify key insights.
- **Feature Engineering**: Transform raw data into meaningful features.
- **Model Building**: Train and evaluate a machine learning model.
- **Model Deployment**: Deploy the trained model as a REST API for real-time predictions.
- **MLOps Integration**: Automate the ML lifecycle using ZenML and MLflow.


## **Key Features**

- **Modular Pipeline Design**: The pipeline is divided into reusable steps (e.g., data ingestion, feature engineering, model training).
- **Experiment Tracking**: MLflow is used to track experiments, log metrics, and compare model versions.
- **Model Deployment**: The trained model is deployed as a REST API using MLflow.
- **CI/CD Integration**: Continuous Integration and Continuous Deployment (CI/CD) pipelines are implemented for automated testing and deployment.
- **Design Patterns**: The project uses **Factory**, **Strategy**, and **Template** design patterns for modular and reusable code.


## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/price-predictor-system.git
cd price-predictor-system
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up ZenML and MLflow**
```bash
zenml init
zenml integration install mlflow -y
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow_deployer --flavor=mlflow
```


## **Pipeline Design**

The ML pipeline is structured into the following **key steps**:

1. **Data Ingestion**:
   - Fetch and preprocess data from various sources (e.g., `.zip`, `.csv`).
   - Use the **Factory Pattern** to dynamically handle different file formats.

2. **Exploratory Data Analysis (EDA)**:
   - Perform data inspection, missing value analysis, univariate analysis, bivariate analysis, and multivariate analysis.
   - Use the **Strategy Pattern** for flexible and modular analysis.

3. **Feature Engineering**:
   - Handle missing values, detect outliers, and apply transformations (e.g., log transformation, one-hot encoding).
   - Use the **Template Pattern** for structured handling of missing values and feature engineering.

4. **Model Building**:
   - Train a machine learning model (e.g., linear regression, Random Forest).
   - Use MLflow to log model parameters, metrics, and artifacts.

5. **Model Evaluation**:
   - Evaluate the model's performance using metrics like RMSE, MAE, and R².
   - Log evaluation results using MLflow.

6. **Model Deployment**:
   - Deploy the trained model as a REST API using MLflow.
   - Implement continuous deployment and inference pipelines.


## **How to Run the Pipeline**

### **1. Run the Pipeline**
```bash
zenml pipeline run
```

### **2. Start MLflow UI**
```bash
mlflow ui
```

### **3. Test the Deployment**
```bash
python sample_predict.py
```


## **Experiment Tracking with MLflow**

MLflow is used to track experiments, log metrics, and compare model versions. To view the experiment results:

1. Start the MLflow UI:
   ```bash
   mlflow ui
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. View logged metrics, parameters, and artifacts for each experiment run.


## **Model Deployment**

The trained model is deployed as a **REST API** using MLflow. You can interact with the deployed model by sending POST requests to the API endpoint.

### **1. Run the Deployment Pipeline**
```bash
python run_deployment.py
```

### **2. Test the Deployed Model**
```bash
python sample_predict.py
```


## **Contributing**

We welcome contributions to the **Price Predictor System**! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request with a detailed description of your changes.


## **Acknowledgments**

- **ZenML**: For pipeline orchestration and MLOps integration.
- **MLflow**: For experiment tracking and model deployment.
- **Scikit-learn**: For model training and evaluation.


Thank you for exploring the **Price Predictor System**! If you have any questions or feedback, feel free to open an issue or contact the maintainers. Happy coding! 🚀
