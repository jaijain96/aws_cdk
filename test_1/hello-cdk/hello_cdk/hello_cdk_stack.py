from aws_cdk import (
    Bucket,
    Stack,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_lambda_event_sources as lambda_event_source,
)
from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_function = _lambda.Function(
            self, "HelloWorldFunction", 
            runtime = _lambda.Runtime.NODEJS_20_X, # Provide any supported Node.js runtime
            handler = "index.handler",
            code = _lambda.Code.from_inline(
                """
                exports.handler = async function(event) {
                return {
                    statusCode: 200,
                    body: JSON.stringify('Hello World!'),
                };
                };
                """
            ),
            )
        my_bucket=s3.Bucket(
            self, 
            id="vks_bucket_123", 
            bucket_name="vks-bucket123"
        )

        queue = sqs.Queue(
            self,
            "cdk_vks_sqs",
            queue_name="VksCdkQueue",  
        )

        sqs_event_source = lambda_event_source.SqsEventSource(queue)
        my_function.add_event_source(sqs_event_source)

# class DeleteBucketStack(Stack):
#     def __init__(self, scope: Construct, id: str, **kwargs) -> None:
#         super().__init__(scope, id, **kwargs)

#         Bucket(
#             self,
#             "vks_bucket_123",
#             bucket_name="vks-bucket123",
#             removal_policy=RemovalPolicy.DESTROY,
#             auto_delete_objects=True,
#         )
