from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 

    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data_dir: Path
    test_data_dir: Path
    img_height: int
    img_width: int
    batch_size: int
    aug_params: dict   



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path

    

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
    params_learning_rate: float       # added
    params_augmentation: Dict         # added (dict from params.yaml)


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    test_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int  