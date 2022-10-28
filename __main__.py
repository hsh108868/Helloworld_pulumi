"""An AWS Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_docker as docker
import pulumi_eks as eks


stack = pulumi.get_stack()

cluster = eks.Cluster('app-cluster')

pulumi.export('kubeconfig', cluster.kubeconfig)
