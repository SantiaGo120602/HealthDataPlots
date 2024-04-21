import os
from typing import Final

WFDB_DATA_ROOT: Final[str] = "wfdb_data/"
WFDB_TO_RECORD: Final[dict[str, list[str]]]
WFDB_BASES_NAMES: Final[tuple[str]]

def _generate_db_paths(folder_path: str) -> list[str]:
    folders = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            folders.append(item_path)
        else:
            raise Exception("Non-wfdb file found")
    return folders

def _generate_record_paths_dict(dbs_paths: list[str]) -> dict[str, list[str]]:
    record_paths_dict = {}
    for dbs_path in dbs_paths:
        record_paths = []
        for item in os.listdir(dbs_path):
            file, extension = os.path.splitext(item)
            if extension == ".hea":
                record_paths.append(dbs_path + "/" + file)
        record_paths_dict[dbs_path.split("/")[1]] = record_paths
    return record_paths_dict

WFDB_TO_RECORD = _generate_record_paths_dict(_generate_db_paths(WFDB_DATA_ROOT))
WFDB_BASES_NAMES = tuple(WFDB_TO_RECORD.keys())

def get_bases_and_path_dict() -> tuple[tuple[str], dict[str, list[str]]]:
    return WFDB_BASES_NAMES, WFDB_TO_RECORD
