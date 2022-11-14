"""An AWS Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_awsx as aws
import pulumi_eks as eks

repo = aws.ecr.Repository(
    "myrepo", image_scanning_configuration=True, image_tag_mutability="MUTABLE")

customImage = "hello_world"
appImage = repo.buildAndPushImage('./hello_world/${customImage}')

