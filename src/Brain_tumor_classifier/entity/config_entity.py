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