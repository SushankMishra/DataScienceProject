from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_training_pipeline import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataIngestionPipeline()
    pipeline.initiate_data_ingestion()
    pipeline.data_ingestion.download_data()
    pipeline.data_ingestion.unzip_data()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataValidationPipeline()
    pipeline.initiate_data_validation()
    pipeline.data_validation.validate_all_columns()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataTransformationPipeline()
    pipeline.initiate_data_transformation()
    pipeline.data_transformation.train_test_splitting()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training stage"
try:
    logger.info(">>> Starting Model Training Pipeline <<<")
    pipeline = ModelTrainingPipeline()
    pipeline.initiate_model_training()
    pipeline.model_training.train_model()
    logger.info(">>> Model Training Pipeline Completed <<<")
except Exception as e:
    logger.exception(e)
    raise e