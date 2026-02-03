from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME="DATA Ingestion stage"
try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
logger.info(" welcome to our custom logiing datascience")

STAGE_NAME="DATA Validation stage"
try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
logger.info(" welcome to our custom logiing datascience")