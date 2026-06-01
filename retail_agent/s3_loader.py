import boto3
import pandas as pd
from io import BytesIO


def load_from_s3():

    bucket_name = "retail-data-engineering-keerthana"
    file_key = "curated/retail_master_curated.csv"

    s3 = boto3.client("s3")

    obj = s3.get_object(
        Bucket=bucket_name,
        Key=file_key
    )

    df = pd.read_csv(obj["Body"])

    return df