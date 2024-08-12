import os
import shutil
from pathlib import Path
from typing import Callable

import py7zr


def make_archive(dir_path: str, output_path: str, archive_format: str, on_success: Callable,
                 on_failure: Callable) -> None:
    archive_formats = ["zip", "tar", "gztar", "bztar", "xztar", "7z", "rar"]

    if not os.path.exists(dir_path):
        on_failure(f"Input folder {dir_path} does not exists.")
        return

    if not os.path.exists(output_path):
        on_failure(f"Output folder {output_path} does not exists.")
        return

    if archive_format.lower() not in archive_formats:
        on_failure(f"Unsupported format: {archive_format}. Supported formats are:\n{archive_formats}")
        return

    folder_name = os.path.basename(os.path.dirname(dir_path))
    folder_path = str(Path(output_path) / folder_name)
    input_folder = Path(dir_path)

    try:
        if archive_format in ["7z", "rar"]:
            with py7zr.SevenZipFile(f"{folder_path}.{archive_format}", 'w') as archive:
                archive.writeall(input_folder, arcname=os.path.basename(input_folder))
        else:
            shutil.make_archive(folder_path, archive_format.lower(), dir_path)
        on_success(f"Archive {archive_format} created, and saved as:\n{folder_path}")
    except Exception as e:
        on_failure(f"Error while creating archive file for {dir_path}:\n{e}")


def extract_archive(archive_path: str, extraction_dir: str, on_success: Callable, on_failure: Callable) -> None:
    if not os.path.exists(archive_path):
        on_failure(f"Archive folder {archive_path} does not exists.")
        return

    if not os.path.exists(extraction_dir):
        on_failure(f"Extraction folder {extraction_dir} does not exists.")
        return

    filename, extension = os.path.splitext(os.path.basename(archive_path))

    try:
        if extension in [".7z", ".rar"]:
            with py7zr.SevenZipFile(archive_path, mode='r') as archive:
                archive.extractall(path=extraction_dir)
        else:
            shutil.unpack_archive(archive_path, extraction_dir)
        on_success(f"Your files have been successfully extracted to:\n{extraction_dir}")
    except Exception as e:
        on_failure(f"Error while extracting archive file for {archive_path}: {e}")
