"""An AWS Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s
import pulumi_aws as aws
import pulumi_eks as eks


cluster = eks.Cluster('app-cluster')

pulumi.export('kubeconfig', cluster.kubeconfig)
