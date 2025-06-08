
module "oke" {
  source  = "oracle/oke/oci"
  version = "4.3.0"

  compartment_ocid = var.compartment_ocid
  cluster_name     = "mlflow-cluster"
  region           = var.region
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

resource "helm_release" "mlflow" {
  name       = "mlflow"
  repository = "https://community-charts.github.io/helm-charts"
  chart      = "mlflow"
  namespace  = "mlflow"
  create_namespace = true

  values = [file("${path.module}/../helm/mlflow/values.yaml")]
}
