# -*- coding: utf-8 -*-

import boto3
from time import sleep

# S3
BUCKET_NAME = "dev-dn-s3-ap-02"
TARGET_DIR = "batch"
FILE_CONTENTS = ""

# Timer
#MAX_ITER = 10
MAX_ITER = 2
#SEC = 60
SEC = 1

def PutS3(i):
      s3 = boto3.resource('s3')
        bucket = s3.Bucket(BUCKET_NAME)
          filename = str(i+1)

            obj = bucket.put_object(ACL='private', Body=FILE_CONTENTS, Key=TARGET_DIR + "/" + filename, ContentType='text/plain')
              return str(obj)

          def count(i):
                print("{}秒経過しました。".format((i+1)*SEC))

                if __name__ == '__main__':
                      for i in range(MAX_ITER):
                              sleep(SEC)
                                  count(i)
                                      PutS3(i)
