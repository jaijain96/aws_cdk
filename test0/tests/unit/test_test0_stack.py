import aws_cdk as core
import aws_cdk.assertions as assertions

from test0.test0_stack import Test0Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in test0/test0_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Test0Stack(app, "test0")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
