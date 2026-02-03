from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.data_training_pipeline import DataTrainingPipeline

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

STAGE_NAME="DATA Transformation stage"
try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
logger.info(" welcome to our custom logiing datascience")

STAGE_NAME="DATA Training stage"
try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTrainingPipeline()
    obj.initiate_data_training()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
logger.info(" welcome to our custom logiing datascience")