resource "aws_eks_cluster" "ecom" {
  name     = var.cluster-name
  role_arn = aws_iam_role.ecom-cluster.arn

  vpc_config {
    security_group_ids = [aws_security_group.ecom-cluster.id]
    subnet_ids         = aws_subnet.ecom[*].id
  }

  depends_on = [
    aws_iam_role_policy_attachment.ecom-cluster-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.ecom-cluster-AmazonEKSVPCResourceController,
  ]
}