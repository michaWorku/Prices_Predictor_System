from zenml import Model, pipeline, step


@pipeline(
    model=Model(
        # The name uniquely identifies this model
        name="prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion Step
    

    # Handling Missing Values Step
    

    # Feature Engineering Step
    

    # Outlier Detection Step


    # Data Splitting Step


    # Model Building Step


    # Model Evaluation Step

    return model


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()
