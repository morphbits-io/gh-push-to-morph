import os
import requests
import pytest
import zipfile
import tempfile
from urllib.parse import urljoin


def download_to_tempfile(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with open(temp_file.name, "wb") as f:
        f.write(response.content)
    return temp_file.name


def list_all_files(directory: str) -> list:
    all_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, directory)
            all_files.append(relative_path)

    return all_files


def compare_regular_files(file_path_1: str, file_path_2: str) -> bool:
    with open(file_path_1, "r") as file1, open(file_path_2, "r") as file2:
        return file1.read() == file2.read()


def test_file_content(url, report_dir):
    if url is None:
        pytest.fail("url is not provided. Provide it using --url option.")

    if report_dir is None or not os.path.exists(report_dir):
        pytest.fail("report_dir is not provided. Provide it using --report_dir option.")

    all_files = list_all_files(report_dir)

    for file in all_files:
        print(f"file: {file}")

        temp_file_path = download_to_tempfile(url)

        assert compare_regular_files(
            temp_file_path, os.path.join(report_dir, file)
        ), f"Contents of {url} and {file} do not match."

        os.remove(temp_file_path)
