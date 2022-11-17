"""An AWS Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_awsx as aws
import pulumi_eks as eks


repo = aws.ecr.Repository("my_repo")

image = aws.ecr.Image(
    resource_name="hello_world", repository_url=repo.url, path="./hello_world")

provider = k8s.Provider(resource_name="hello_world", namespace="hello_world")

appDeployment = k8s.apps.v1.Deployment("apps", spec=k8s.apps.v1.DeploymentSpecArgs(
    metadata=k8s.meta.v1.ObjectMetaArgs(
        labels={
            "app": "nginx",
        },
    ),
    replicas=1,
    selector=k8s.meta.v1.LabelSelectorArgs(
        match_labels={
            "app": "nginx"
        }
    )
))
