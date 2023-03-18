resource "aws_eks_node_group" "ecom" {
  cluster_name    = aws_eks_cluster.ecom.name
  node_group_name = var.eks_node_group_name
  node_role_arn   = aws_iam_role.ecom-node.arn
  instance_types  = [var.clutser_instance_type]
  subnet_ids      = aws_subnet.ecom[*].id

  scaling_config {
    desired_size = var.desired_node_size
    max_size     = var.max_node_size
    min_size     = var.min_node_size
  }

  depends_on = [
    aws_iam_role_policy_attachment.ecom-node-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.ecom-node-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.ecom-node-AmazonEC2ContainerRegistryReadOnly,
  ]
}