from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
from zenml import Model, pipeline, step


@pipeline(
    model=Model(
        # The name uniquely identifies this model
        name="prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""
    model = Model(name="prices_predictor")
    
    # Data Ingestion Step
    raw_data = data_ingestion_step(
        file_path=".../data/archive.zip"
    )

    # Handling Missing Values Step
    filled_data = handle_missing_values_step(raw_data)

    # Feature Engineering Step
    

    # Outlier Detection Step


    # Data Splitting Step


    # Model Building Step


    # Model Evaluation Step

    return model


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()
