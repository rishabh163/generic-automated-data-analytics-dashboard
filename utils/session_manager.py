import streamlit as st


DATAFRAME_KEY = "df"
FILENAME_KEY = "file_name"


def save_dataset(dataframe, file_name):
    """
    Save the uploaded dataset and file name
    in Streamlit session state.
    """

    st.session_state[DATAFRAME_KEY] = dataframe
    st.session_state[FILENAME_KEY] = file_name


def get_dataset():
    """
    Return the uploaded dataset.

    Returns
    -------
    DataFrame | None
    """

    return st.session_state.get(DATAFRAME_KEY)


def get_file_name():
    """
    Return uploaded file name.

    Returns
    -------
    str | None
    """

    return st.session_state.get(FILENAME_KEY)


def dataset_exists():
    """
    Check whether a dataset is available.

    Returns
    -------
    bool
    """

    return DATAFRAME_KEY in st.session_state


def clear_dataset():
    """
    Remove dataset information from session state.
    """

    st.session_state.pop(DATAFRAME_KEY, None)
    st.session_state.pop(FILENAME_KEY, None)