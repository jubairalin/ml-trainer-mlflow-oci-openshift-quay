# ml-trainer-mlflow-oci-openshift-quay
ML pipeline project on OpenShift with MLflow, GitHub Actions, Terraform, and Helm

# OpenShift MLflow Model Training & Serving Pipeline

This project provides a full CI/CD pipeline for training, testing, logging, and serving a machine learning model using:
- **Python **
- **MLflow for experiment tracking**
- **FastAPI for model serving**
- **GitHub Actions for CI/CD**
- **Helm & OpenShift for deployment**
- **Terraform for infrastructure provisioning on Oracle Cloud (OCI)**

---

## 📁 Project Structure
![image](https://github.com/user-attachments/assets/5f43d434-5475-4705-9ecf-5999fc317fe9)



---

## ⚙️ Requirements

- Python 3.8+
- OpenShift Cluster on OCI
- MLflow deployed via Helm (included in Terraform)
- GitHub Actions Secrets set up for Quay and cluster access

---

## 🚀 Quick Start

### 1. Clone and Set Up

```bash
git clone https://github.com/jubairalin/ml-trainer-mlflow-oci-openshift-quay.git
cd ml-trainer-mlflow-oci-openshift-quay

2. Train Model 
bash scripts/run_train.sh

3. Serve Model
scripts.serve:app --host 0.0.0.0 --port 8000
http://techinea:8000/predict?a=1.0&b=2.0&c=3.0

🔁 CI/CD with GitHub Actions
ci.yml: Runs unit tests, installs requirements, trains model, logs to MLflow

deploy.yml: Deploys FastAPI server to OpenShift with updated image

☁️ Deploy MLflow with Terraform (on OCI)

cd terraform
terraform init
terraform apply -var-file="your.tfvars"

📦 Build & Push Image to Quay
docker build -t quay.io/techinea/modelserver:latest .
docker push quay.io/techinea/modelserver:latest

🚀 Deploy with Helm
helm upgrade --install modelserver ./charts/modelserver --namespace techineamlflow --create-namespace

🔐 Kubernetes Secrets & PVC
oc apply -f k8s/pvc-dataset.yaml
oc apply -f k8s/pvc-output.yaml
oc apply -f k8s/secret-mlflow.yaml


📊 MLflow UI
Visit your OpenShift route after deploying MLflow with Helm or Terraform:

http://mlflow.apps.techinea.openshift.example.com

🔍 Sample Dataset

The dataset.csv includes columns:
ColumnA,ColumnB,ColumnC,Label
1.0,2.0,3.0,0
4.0,5.0,6.0,1
...


🔧 GitHub Secrets to Set
QUAY_USERNAME

QUAY_PASSWORD

KUBECONFIG or OpenShift access token for oc CLI

MLFLOW_TRACKING_URI (optional override)

🧠 Authors & Acknowledgments
Maintained by: Jubair Ali
Powered by OpenShift, OCI, MLflow, Helm, GitHub Actions




