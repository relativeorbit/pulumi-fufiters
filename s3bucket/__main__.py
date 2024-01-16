"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
specific_name = 'fufiters' 
bucket = s3.Bucket(specific_name,
                    bucket=specific_name #otherwise appends random string for uniqueness
                    )

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
