import serviceinitializer

def createBucket(name):
    s3client = serviceinitializer.getS3Client()
    if (s3client.bucket_exists(bucket_name=name)):
        s3client.make_bucket(bucket_name=name)
        return 'Bucket created'
    
    else:
        return 'Bucket already exists'