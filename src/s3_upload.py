import boto3

s3 = boto3.client("s3")

bucket_name = "retail-data-engineering-keerthana"

s3.upload_file(
    "data/curated/retail_master_curated.csv",
    bucket_name,
    "curated/retail_master_curated.csv"
)

print("Upload Successful")