import pandas as pd
import pytest

from ml_baseline.schema import InputSchema, validate_and_align


def test_validate_and_align_fails_on_forbidden_column():
    schema = InputSchema(
        required_feature_columns=["a"],
        feature_dtypes={"a": "int"},
        optional_id_columns=[],
        forbidden_columns=["y"],
    )

    # فيه عمود ممنوع y
    df = pd.DataFrame(
        {
            "a": [1, 2],
            "y": [0, 1],
        }
    )

    with pytest.raises(AssertionError, match="Forbidden columns"):
        validate_and_align(df, schema)


def test_validate_and_align_fails_on_missing_required_column():
    schema = InputSchema(
        required_feature_columns=["a", "b"],
        feature_dtypes={"a": "int", "b": "int"},
        optional_id_columns=[],
        forbidden_columns=[],
    )

    # العمود b ناقص
    df = pd.DataFrame(
        {
            "a": [1, 2],
        }
    )

    with pytest.raises(AssertionError, match="Missing required feature columns"):
        validate_and_align(df, schema)
