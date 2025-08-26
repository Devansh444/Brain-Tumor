from Brain_tumor_classifier.config.configuration import ConfigurationManager
from Brain_tumor_classifier.components.data_transformation import DataTransformation
from Brain_tumor_classifier import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        
        # Get train and test generators
        train_gen, test_gen = data_transformation.get_data_generators()
        logger.info("✅ Data Transformation completed successfully.")
        
        return train_gen, test_gen


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        train_gen, test_gen = obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
