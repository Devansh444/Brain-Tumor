from Brain_tumor_classifier.config.configuration import ConfigurationManager
from Brain_tumor_classifier.components.data_transformation import DataTransformation
from Brain_tumor_classifier import logger

def run_data_transformation_pipeline():
    try:
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        train_gen, test_gen = data_transformation.get_data_generators()
        logger.info("✅ Data Transformation completed successfully.")
        return train_gen, test_gen
    except Exception as e:
        logger.exception(e)
        raise e
