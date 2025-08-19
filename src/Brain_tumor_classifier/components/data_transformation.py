from tensorflow.keras.preprocessing.image import ImageDataGenerator

class DataTransformation:
    def __init__(self, config):
        self.config = config

    def get_data_generators(self):
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=self.config.aug_params['rotation_range'],
            width_shift_range=self.config.aug_params['width_shift_range'],
            height_shift_range=self.config.aug_params['height_shift_range'],
            shear_range=self.config.aug_params['shear_range'],
            zoom_range=self.config.aug_params['zoom_range'],
            horizontal_flip=self.config.aug_params['horizontal_flip'],
            fill_mode='nearest'
        )

        test_datagen = ImageDataGenerator(rescale=1./255)

        train_generator = train_datagen.flow_from_directory(
            directory=str(self.config.train_data_dir),
            target_size=(self.config.img_height, self.config.img_width),
            batch_size=self.config.batch_size,
            class_mode='categorical'
        )

        test_generator = test_datagen.flow_from_directory(
            directory=str(self.config.test_data_dir),
            target_size=(self.config.img_height, self.config.img_width),
            batch_size=self.config.batch_size,
            class_mode='categorical'
        )

        return train_generator, test_generator
