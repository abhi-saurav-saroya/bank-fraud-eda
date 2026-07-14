import pandas as pd


EXCLUDED_COLUMNS = {
    "transaction_id",
    "customer_id",
    "transaction_datetime"
}

DISCRETE_NUMERIC_COLUMNS = {
    "hour_of_day",
    "failed_attempts",
}


def get_binary_columns(df: pd.DataFrame) -> list[str]:
    """
    Return columns containing only binary values (0/1).
    """

    binary_columns = []

    for column in df.columns:

        if column in EXCLUDED_COLUMNS:
            continue

        values = set(df[column].dropna().unique())

        if values <= {0, 1}:
            binary_columns.append(column)

    return sorted(binary_columns)


def get_numeric_columns(df: pd.DataFrame) -> list[str]:
    """
    Return numerical columns excluding binary features.
    """

    numeric = list(
        df.select_dtypes(include="number").columns
    )

    binary = get_binary_columns(df)

    return sorted(
        [
            col
            for col in numeric
            if col not in binary
            and col not in EXCLUDED_COLUMNS
            and col not in DISCRETE_NUMERIC_COLUMNS
        ]
    )


def get_categorical_columns(df: pd.DataFrame) -> list[str]:
    """
    Return categorical (object/category) columns.
    """

    categorical = list(
        df.select_dtypes(
            include=["object", "category"]
        ).columns
    )

    return sorted(
        [
            col
            for col in categorical
            if col not in EXCLUDED_COLUMNS
        ]
    )


def get_datetime_columns(df: pd.DataFrame) -> list[str]:
    """
    Return datetime columns.
    """

    datetime_cols = list(
        df.select_dtypes(
            include=["datetime", "datetimetz"]
        ).columns
    )

    return sorted(
        [
            col
            for col in datetime_cols
            if col not in EXCLUDED_COLUMNS
        ]
    )



# Master Configuration
def get_feature_groups(df: pd.DataFrame) -> dict:
    """
    Return all feature groups.
    """

    return {
        "Numerical": get_numeric_columns(df),
        "Categorical": get_categorical_columns(df),
        "Binary": get_binary_columns(df),
        "Datetime": get_datetime_columns(df),
        "Discrete Numerical": list(DISCRETE_NUMERIC_COLUMNS) 
    }