from cnnClassifier import logger
from cnnClassifier.pipeline.training_pipeline import TrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   train_pipeline = TrainingPipeline()
   train_pipeline.dataingestiontrainingpipeline()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
