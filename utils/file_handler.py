import pandas as pd


SUPPORTED_FILE_TYPES = {
    ".csv": pd.read_csv,
    ".xlsx": pd.read_excel,
    ".json": pd.read_json,
}


def load_uploaded_file(uploaded_file):
    """
    Load an uploaded CSV, Excel, or JSON file.

    Parameters
    ----------
    uploaded_file : UploadedFile
        File uploaded using Streamlit's file uploader.

    Returns
    -------
    tuple
        (dataframe, file_name)
    """

    if uploaded_file is None:
        return None, None

    file_name = uploaded_file.name

    for extension, reader in SUPPORTED_FILE_TYPES.items():
        if file_name.endswith(extension):
            dataframe = reader(uploaded_file)
            return dataframe, file_name

    return None, None