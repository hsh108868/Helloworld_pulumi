"""An AWS Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_awsx as aws
import pulumi_eks as eks


repo = aws.ecr.Repository("my_repo")

image = aws.ecr.Image(
    "hello_world", repository_url=repo.url, path="./hello_world")

provider = k8s.Provider("hello_world", config.kubeconfig)
