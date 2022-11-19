"""An AWS Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_awsx as aws
import pulumi_eks as eks


repo = aws.ecr.Repository("my_repo")

appImage = "hello_world"
customImage = aws.ecr.Image(
    resource_name=appImage, repository_url=repo.url, path="./hello_world")

provider = k8s.Provider(resource_name=appImage, namespace=appImage)

appDeployment = k8s.apps.v1.Deployment("apps", spec=k8s.apps.v1.DeploymentSpecArgs(
    metadata=k8s.meta.v1.ObjectMetaArgs(
        labels={
            "app": appImage,
        },
    ),
    replicas=1,
    selector=k8s.meta.v1.LabelSelectorArgs(
        match_labels={
            "app": appImage,
        }
    ),
    template=k8s.core.v1.PodTemplateSpecArgs(
        metadata=k8s.meta.v1.ObjectMetaArgs(
            labels={
                "app": appImage,
            }
        ),
        spec=k8s.core.v1.PodSpecArgs(
            containers=[k8s.core.v1.ContainerArgs(
                name=appImage,
                image=customImage,
                ports=[k8s.core.v1.ContainerPortArgs(
                    name="http",
                    container_port=80,
                )],
            )],
        ),
    ),
),)
