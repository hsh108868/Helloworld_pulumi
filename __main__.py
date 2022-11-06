"""An AWS Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_aws as aws
import pulumi_eks as eks


stack = pulumi.get_stack()

repo = aws.ecr.Repository(
    "myrepo", image_scanning_configuration=True, image_tag_mutability="MUTABLE")

cluster = eks.Cluster('app-cluster')

pulumi.export('kubeconfig', cluster.kubeconfig)
