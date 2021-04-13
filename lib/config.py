import os

DATASET_ROOT = "/data/kinetics400/"
TRAIN_ROOT = os.path.join(DATASET_ROOT, "train")
VALID_ROOT = os.path.join(DATASET_ROOT, "valid")
TEST_ROOT = os.path.join(DATASET_ROOT, "test")

TRAIN_FRAMES_ROOT = os.path.join(DATASET_ROOT, "train_frames")
VALID_FRAMES_ROOT = os.path.join(DATASET_ROOT, "valid_frames")
TEST_FRAMES_ROOT = os.path.join(DATASET_ROOT, "test_frames")

TRAIN_SOUND_ROOT = os.path.join(DATASET_ROOT, "train_sound")
VALID_SOUND_ROOT = os.path.join(DATASET_ROOT, "valid_sound")
TEST_SOUND_ROOT = os.path.join(DATASET_ROOT, "test_sound")

CATEGORIES_PATH = "resources/categories.json"
CLASSES_PATH = "resources/classes.json"
TRAIN_METADATA_PATH = os.path.join(DATASET_ROOT, "kinetics400", "train.json")
VAL_METADATA_PATH = os.path.join(DATASET_ROOT, "kinetics400", "val.json")
TEST_METADATA_PATH = os.path.join(DATASET_ROOT, "kinetics400", "test.json")
