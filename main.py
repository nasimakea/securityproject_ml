from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__ == "__main__":
    try:
        # Step 1: Create training pipeline config
        trainingpipelineconfig=TrainingPipelineConfig()

        # Step 2: Create data ingestion config (OBJECT, not class)
        dataingestionconfig = DataIngestionConfig(
            training_pipeline_config=trainingpipelineconfig
        )

        # Step 3: Create data ingestion object
        data_ingestion = DataIngestion(
            data_ingestion_config=dataingestionconfig
        )

        logging.info("Initiating data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()

        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
