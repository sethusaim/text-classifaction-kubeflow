LABEL_DICT: dict = {
    "Electronics": 0,
    "Household": 1,
    "Books": 2,
    "Clothing & Accessories": 3,
}

ARTIFACTS_BUCKET_NAME: str = "41644ecom-artifacts"

TARGET_COL: str = "label"

ARTIFACT_DIR: str = "artifacts"

DATA_VALIDATION_DIR: str = "data_validation"

DATA_VALIDATION_VALIDATED_DIR: str = "validated"

DATA_VALIDATION_TRAIN_FILE_NAME: str = "ecom_train.csv"

DATA_VALIDATION_TEST_FILE_NAME: str = "ecom_test.csv"

DATA_TRANSFORMATION_DIR: str = "data_transformation"

DATA_TRANSFORMATION_TRAIN_FILE_NAME: str = "ecom_transformed_train.csv"

DATA_TRANSFORMED_TRANSFORMED_DIR: str = "transformed"

DATA_TRANSFORMATION_TEST_FILE_NAME: str = "ecom_transformed_test.csv"

SPLIT_KWARGS: dict = {"test_size": 0.3, "random_state": 42}

DATA_TRANSFORMATION_CONFIG_FOLDER: str = "config"

DATA_TRANSFORMATION_CONFIG_BUCKET_NAME: str = "41644ecom-config"

DATA_TRANSFORMATION_ACRONYMS_CONFIG_FILE: str = "english_acronyms.json"

DATA_TRANSFORMATION_CONTRACTIONS_CONFIG_FILE: str = "english_contractions.json"

TRANSFORMED_FEATURES_TRAIN_FILE: str = "transformed_train_features"

TRANSFORMED_FEATURES_VAL_FILE: str = "transformed_val_features"

TRANSFORMED_FEATURES_TEST_FILE: str = "transformed_test_features.pkl"

TRANSFORMED_TARGETS_TRAIN_FILE: str = "transformed_train_targets.pkl"

TRANSFORMED_TARGETS_VAL_FILE: str = "transformed_val_targets.pkl"

TRANSFORMED_TARGETS_TEST_FILE: str = "transformed_test_targets.pkl"

TRANSFORMED_VECTORIZED_FILE_PATH: str = "vectorizer.pkl"

DATA_TRANSFORMATION_STOP_WORDS: list = [
    "among",
    "onto",
    "shall",
    "thrice",
    "thus",
    "twice",
    "unto",
    "us",
    "would",
]

DATA_TRANSFORMATION_KEEP_TAGS = [
    "NN",
    "NNS",
    "NNP",
    "NNPS",
    "FW",
    "PRP",
    "PRPS",
    "RB",
    "RBR",
    "RBS",
    "VB",
    "VBD",
    "VBG",
    "VBN",
    "VBP",
    "VBZ",
    "WDT",
    "WP",
    "WPS",
    "WRB",
]

ALPHABETS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


PREPOSITIONS = [
    "about",
    "above",
    "across",
    "after",
    "against",
    "among",
    "around",
    "at",
    "before",
    "behind",
    "below",
    "beside",
    "between",
    "by",
    "down",
    "during",
    "for",
    "from",
    "in",
    "inside",
    "into",
    "near",
    "of",
    "off",
    "on",
    "out",
    "over",
    "through",
    "to",
    "toward",
    "under",
    "up",
    "with",
]

PREPOSITIONS_LESS_COMMON = [
    "aboard",
    "along",
    "amid",
    "as",
    "beneath",
    "beyond",
    "but",
    "concerning",
    "considering",
    "despite",
    "except",
    "following",
    "like",
    "minus",
    "onto",
    "outside",
    "per",
    "plus",
    "regarding",
    "round",
    "since",
    "than",
    "till",
    "underneath",
    "unlike",
    "until",
    "upon",
    "versus",
    "via",
    "within",
    "without",
]

COORDINATING_CONJUNCTIONS = ["and", "but", "for", "nor", "or", "so", "and", "yet"]

CORRELATIVE_CONJUNCTIONS = [
    "both",
    "and",
    "either",
    "or",
    "neither",
    "nor",
    "not",
    "only",
    "but",
    "whether",
    "or",
]

SUBORDINATING_CONJUNCTIONS = [
    "after",
    "although",
    "as",
    "as if",
    "as long as",
    "as much as",
    "as soon as",
    "as though",
    "because",
    "before",
    "by the time",
    "even if",
    "even though",
    "if",
    "in order that",
    "in case",
    "in the event that",
    "lest",
    "now that",
    "once",
    "only",
    "only if",
    "provided that",
    "since",
    "so",
    "supposing",
    "that",
    "than",
    "though",
    "till",
    "unless",
    "until",
    "when",
    "whenever",
    "where",
    "whereas",
    "wherever",
    "whether or not",
    "while",
]

OTHERS = [
    "ã",
    "å",
    "ì",
    "û",
    "ûªm",
    "ûó",
    "ûò",
    "ìñ",
    "ûªre",
    "ûªve",
    "ûª",
    "ûªs",
    "ûówe",
]
