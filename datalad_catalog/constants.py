from .translator import CoreTranslator, StudyminimetaTranslator, CoreDatasetTranslator

# A module to store all constants (mostly field names of metalad extractors)

ATGRAPH="@graph"
ATID="@id"
ATLIST="@list"
ATTYPE="@type"
AUTHOR="author"
AUTHORS="authors"
CREATIVEWORK="CreativeWork"
DESCRIPTION="description"
DOI="doi"
DIRECTORY="directory"
DATASET="Dataset"
DATASET_ID="dataset_id"
DATASET_PATH="dataset_path"
DATASET_VERSION="dataset_version"
DIRSFROMPATH="dirs_from_path"
DISTRIBUTION="distribution"
EXTRACTED_METADATA="extracted_metadata"
EXTRACTOR_CORE="metalad_core"
EXTRACTOR_CORE_DATASET="metalad_core_dataset" # older version; core is newer version
EXTRACTOR_NAME="extractor_name"
EXTRACTOR_STUDYMINIMETA="metalad_studyminimeta"
EXTRACTOR_VERSION="extractor_version"
EXTRACTOR_TRANSLATOR_SELECTOR = {
    EXTRACTOR_CORE: CoreTranslator(),
    EXTRACTOR_CORE_DATASET: CoreDatasetTranslator(),
    EXTRACTOR_STUDYMINIMETA: StudyminimetaTranslator(),
}
HASPART="hasPart"
IDENTIFIER="identifier"
NAME="name"
ORIGIN="origin"
PATH="path"
PERSONLIST="personList"
PUBLICATION="publication"
PUBLICATIONS="publications"
PUBLICATIONLIST="#publicationList"
SAMEAS="sameAs"
SCHEMA_CORE_DATASET="core_dataset_schema.json"
SCHEMA_CORE_FOR_DATASET="core_schema_for_dataset.json"
SCHEMA_CORE_FOR_FILE="core_schema_for_file.json"
SCHEMA_STUDYMINIMETA="studyminimeta_schema.json"
STRIPDATALAD="datalad:"
STUDY="study"
SUBDATASETS="subdatasets"
TYPE="type"
TYPE_DATASET="dataset"
TYPE_DIRECTORY="directory"
TYPE_FILE="file"
URL="url"