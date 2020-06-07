from minio import Minio
import os

S3Client = None

def getS3Client():
    if S3Client is None:
        return Minio(
        os.environ['AWS_S3_ENDPOINT'],
        os.environ['AWS_ACCESS_KEY_ID'],
        os.environ['AWS_SECRET_KEY_ID'],
        secure=False)
    return S3Client
    