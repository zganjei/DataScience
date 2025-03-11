from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

logger.info("Welcome to our custom logging for data science")


STAGE_NAME = "Data Ingestion stage"

try: 
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>> {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>> {STAGE_NAME} started <<<<<<")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.initiate_data_transformation()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training stage"
try:
    logger.info(f">>> {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f">>> {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e