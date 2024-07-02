import os
import shutil
from pathlib import Path

import py7zr


class UnsupportedArchiveFormatError(Exception):
    def __init__(self, archive_format: str):
        super().__init__(f"Unsupported archive format: {archive_format}")


def path_exists(path: str) -> bool:
    return os.path.exists(path)


def make_archive(dir_path: str, output_path: str, archive_format: str) -> bool:
    """
        Create an archive (ZIP, tar, gztar, bztar, xztar, 7z, or RAR) from the specified directory.

        Args:
            dir_path (str): Path to the input directory.
            output_path (str): Path to the output folder where the archive will be saved.
            archive_format (str): Desired archive format ("zip", "tar", "gztar", "bztar", "xztar", "7z", "rar").

        Returns:
            bool: True if the archive was created successfully, False otherwise.
        """
    archive_formats = ["zip", "tar", "gztar", "bztar", "xztar", "7z", "rar"]

    if not path_exists(dir_path):
        raise NotADirectoryError(f"Input folder {dir_path} does not exists.")

    if not path_exists(output_path):
        raise NotADirectoryError(f"Output folder {output_path} does not exists.")

    if archive_format.lower() not in archive_formats:
        raise UnsupportedArchiveFormatError(archive_format)

    folder_name = os.path.basename(os.path.dirname(dir_path))
    folder_path = str(Path(output_path) / folder_name)
    input_folder = Path(dir_path)

    try:
        if archive_format in ["7z", "rar"]:
            with py7zr.SevenZipFile(f"{folder_path}.{archive_format}", 'w') as archive:
                archive.writeall(input_folder, arcname=os.path.basename(input_folder))
        else:
            shutil.make_archive(folder_path, archive_format.lower(), dir_path)
        return True
    except Exception as e:
        print(f"Error creating archive file for {dir_path}: {e}")
        return False


def extract_archive(archive_path: str, extraction_dir: str) -> bool:
    """
        Extracts files from an archive (ZIP, tar, gztar, bztar, xztar, 7z, or RAR) to the specified directory.

        Args:
            archive_path (str): Path to the archive file.
            extraction_dir (str): Directory where the contents will be extracted.

        Returns:
            bool: True if extraction is successful, False otherwise.
        """
    if not path_exists(archive_path):
        raise NotADirectoryError(f"Archive folder {archive_path} does not exists.")

    if not path_exists(extraction_dir):
        raise NotADirectoryError(f"Extraction folder {extraction_dir} does not exists.")

    filename, extension = os.path.splitext(os.path.basename(archive_path))

    try:
        if extension in [".7z", ".rar"]:
            with py7zr.SevenZipFile(archive_path, mode='r') as archive:
                archive.extractall(path=extraction_dir)
        else:
            shutil.unpack_archive(archive_path, extraction_dir)
        return True
    except Exception as e:
        print(f"Error extracting archive file for {archive_path}: {e}")
        return False
