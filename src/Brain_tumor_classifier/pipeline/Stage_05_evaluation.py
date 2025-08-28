from Brain_tumor_classifier.config.configuration import ConfigurationManager
from Brain_tumor_classifier.components.evaluation import Evaluation
from Brain_tumor_classifier import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        # Load configuration
        config = ConfigurationManager()
        # Get evaluation config with proper test dataset path
        val_config = config.get_validation_config()
        # Initialize evaluation
        evaluation = Evaluation(val_config)
        # Run evaluation
        evaluation.evaluation()
        # Save evaluation scores
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
