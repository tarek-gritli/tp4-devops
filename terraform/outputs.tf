output "cluster_name" {
  value = kind_cluster.tp4.name
}

output "kubeconfig" {
  value     = kind_cluster.tp4.kubeconfig
  sensitive = true
}
