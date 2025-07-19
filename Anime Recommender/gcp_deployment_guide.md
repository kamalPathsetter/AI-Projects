
# 🚀 LLMOps App Deployment & Monitoring Setup  
_Cloud: GCP · Orchestration: Minikube · Monitoring: Grafana_

---

## ✅ 1. Initial Setup

### 🔗 Push Code to GitHub

Ensure your code is version-controlled and pushed to a public or private GitHub repository:

```bash
git init
git remote add origin https://github.com/<your-username>/<your-repo>.git
git add .
git commit -m "Initial commit"
git push origin main
```

### 🐳 Create a `Dockerfile`

Ensure your project contains a `Dockerfile` at the root to containerize your application.

### ☸️ Kubernetes Deployment

Create a Kubernetes deployment YAML file:

```bash
touch llmops-k8s.yaml
```

Configure it to deploy your app container and expose a service.

---

## 🌐 2. Create a VM Instance on Google Cloud

1. Go to **Compute Engine → VM Instances** → Click **Create Instance**
2. Use these recommended settings:

| Setting        | Value                |
|----------------|----------------------|
| Name           | `<your-vm-name>`     |
| Series         | `E2`                 |
| Machine Type   | `Standard (16 GB RAM)` |
| Boot Disk      | `Ubuntu 24.04 LTS (256 GB)` |
| Networking     | Allow **HTTP** & **HTTPS** |

3. Click **Create** and connect using browser SSH.

---

## ⚙️ 3. Configure the VM

### 🧬 Clone Your Repo

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 🐳 Install Docker

Follow the official steps for [Docker installation](https://docs.docker.com/engine/install/ubuntu/):

```bash
# Post-install test
docker run hello-world
```

### ⚙️ Docker Without `sudo`

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

### 🔁 Enable Docker on Boot

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

---

## ☸️ 4. Setup Minikube on the VM

### 📥 Install Minikube

Follow the official [Linux Binary installation guide](https://minikube.sigs.k8s.io/docs/start/).

### 🟢 Start Cluster

```bash
minikube start
```

### 🧰 Install `kubectl`

```bash
sudo snap install kubectl --classic
kubectl version --client
```

### ✅ Verify Everything

```bash
minikube status
kubectl get nodes
kubectl cluster-info
docker ps
```

---

## 💻 5. Link GitHub to VM

```bash
git config --global user.email "<your-email>"
git config --global user.name "<your-name>"
```

Commit & push changes:

```bash
git add .
git commit -m "commit"
git push origin main
```

> 🔐 Use your GitHub **username** and **access token** when prompted.

---

## 🚢 6. Build & Deploy the App

### 🔄 Point Docker to Minikube

```bash
eval $(minikube docker-env)
```

### 🧱 Build Docker Image

```bash
docker build -t llmops-app:latest .
```

### 🔐 Kubernetes Secrets

```bash
kubectl create secret generic llmops-secrets   --from-literal=GROQ_API_KEY="your_groq_key"   --from-literal=HUGGINGFACEHUB_API_TOKEN="your_hf_token"
```

### 📦 Apply Deployment

```bash
kubectl apply -f llmops-k8s.yaml
kubectl get pods
```

### 🌐 Expose App

- **Terminal 1**:

```bash
minikube tunnel
```

- **Terminal 2**:

```bash
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

> Access at: `http://<external-ip>:8501`

---

## 📊 7. Grafana Cloud Monitoring

### 📁 Create Namespace

```bash
kubectl create ns monitoring
```

### 👤 Create Grafana Cloud Account

1. Go to [https://grafana.com](https://grafana.com)
2. Go to: **Observability → Kubernetes → Start Sending Data**
3. Fill:
   - Cluster: `minikube`
   - Namespace: `monitoring`
   - Installation method: **Helm**
4. Generate and **copy access token**

---

### 🪖 Install Helm

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version
```

### ✏️ Create `values.yaml`

```bash
vi values.yaml
```

Paste Grafana agent config (from your cloud dashboard) into the file. Remove any `EOF` markers.

Exit with `ESC + :wq`

---

### 🚀 Deploy Grafana Agent

```bash
helm repo add grafana https://grafana.github.io/helm-charts &&
helm repo update &&
helm upgrade --install --atomic --timeout 300s grafana-k8s-monitoring grafana/k8s-monitoring   --namespace "monitoring" --create-namespace --values values.yaml
```

### ✅ Confirm Everything

```bash
kubectl get pods -n monitoring
```

> Return to Grafana Cloud to view dashboards and metrics.

---

## 🧹 Optional Cleanup

```bash
kubectl delete ns monitoring
minikube delete
gcloud compute instances delete <your-vm-name>
```

---

## ✅ Success!

You’ve:

- 🚀 Deployed an app on Minikube inside a GCP VM  
- 📦 Used Docker + Kubernetes  
- 📊 Monitored it with Grafana Cloud  

> Happy hacking! 🧠💡🛠️
