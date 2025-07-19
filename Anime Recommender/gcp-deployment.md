
# 🚀 LLMOps App Deployment & Monitoring Setup (GCP + Minikube + Grafana)

---

## ✅ 1. Initial Setup

### 🔗 Push Code to GitHub
Ensure your project code is pushed to a GitHub repository.

### 🐳 Create a `Dockerfile`
Add a `Dockerfile` to the root of your project to containerize the app.

### 📦 Create Kubernetes Deployment
Create a Kubernetes deployment file named:

```
anime-recommender-k8s.yaml
```

---

## 🌐 2. Create a VM Instance on Google Cloud

- Go to **VM Instances** → Click **Create Instance**
- Fill in:
  - **Name**: (choose a name)
  - **Machine Type**:
    - Series: `E2`
    - Preset: `Standard`
    - Memory: `16 GB RAM`
  - **Boot Disk**:
    - Size: `256 GB`
    - Image: `Ubuntu 24.04 LTS`
  - **Networking**:
    - Enable: **HTTP** & **HTTPS** traffic
- Click **Create**
- Use **SSH** to connect to your VM from the browser

---

## ⚙️ 3. Configure VM Instance

### 🧬 Clone Your GitHub Repo

```bash
git clone https://github.com/data-guru0/TESTING-9.git
cd TESTING-9
```

### 🐳 Install Docker

- Visit [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)
- Run the command blocks in order (as per official site):

```bash
# Test Docker
docker run hello-world
```

### ⚙️ Allow Docker Without `sudo`

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

### ✅ Verify Docker Setup

```bash
systemctl status docker
docker ps
docker ps -a
```

---

## ☸️ 4. Setup Minikube on the VM

### 📥 Install Minikube

- Go to: [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)
- Select:
  - OS: **Linux**
  - Arch: **x86_64**
  - Use: **Binary download** method

Paste the commands from the site into the terminal.

### 🟢 Start Minikube Cluster

```bash
minikube start
```

### 🧰 Install `kubectl`

```bash
sudo snap install kubectl --classic
kubectl version --client
```

### ✅ Check Minikube Status

```bash
minikube status
kubectl get nodes
kubectl cluster-info
docker ps  # Minikube container should be visible
```

---

## 💻 5. Link GitHub to VSCode & VM

```bash
git config --global user.email "gyrogodnon@gmail.com"
git config --global user.name "data-guru0"

git add .
git commit -m "commit"
git push origin main
```

> 🔐 Use your GitHub **username** and **access token** (not password) when prompted.

---

## 🚢 6. Build & Deploy Your App

### 🔄 Point Docker to Minikube

```bash
eval $(minikube docker-env)
```

### 🧱 Build Docker Image

```bash
docker build -t llmops-app:latest .
```

### 🔐 Create Kubernetes Secrets

```bash
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="your_key_here" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN="your_token_here"
```

### 📦 Apply Deployment

```bash
kubectl apply -f llmops-k8s.yaml
kubectl get pods
```

> ✅ Ensure your pods are running.

### 🌐 Expose App to Internet

- In **Terminal 1**:

```bash
minikube tunnel
```

- In **Terminal 2**:

```bash
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

> Open browser: `http://<external-ip>:8501` to access your app.

---

## 📊 7. Grafana Cloud Monitoring Setup

### 📁 Create Namespace

```bash
kubectl create ns monitoring
kubectl get ns
```

### 👤 Create Grafana Cloud Account

1. Go to: [https://grafana.com](https://grafana.com)
2. Navigate: **Observability** → **Kubernetes** → **Start Sending Data**
3. Fill:
   - **Cluster Name**: `minikube`
   - **Namespace**: `monitoring`
4. Choose:
   - Installation method: `Helm`
   - Generate and **save the access token**

### 🪖 Install `helm`

Search: `Install Helm Ubuntu` and run the official 3-command installation block.

---

### 📝 Create `values.yaml` file

In terminal:

```bash
vi values.yaml
```

- Paste the YAML config from Grafana Cloud
- **Remove**:
  - The `EOF` line at the end
  - The initial Helm script lines (save them separately)

Exit with: `ESC + :wq`

### 🚀 Deploy Grafana Agent with Helm

```bash
helm repo add grafana https://grafana.github.io/helm-charts &&
helm repo update &&
helm upgrade --install --atomic --timeout 300s grafana-k8s-monitoring grafana/k8s-monitoring \
  --namespace "monitoring" --create-namespace --values values.yaml
```

### ✅ Check Deployment

```bash
kubectl get pods -n monitoring
```

> All pods should be running.

### 📈 View Metrics

1. Go to Grafana Cloud → Homepage
2. Refresh the page
3. Explore real-time Kubernetes cluster metrics

---

## 🧹 Cleanup (Optional)

Remember to clean up resources if no longer needed:

```bash
kubectl delete ns monitoring
minikube delete
gcloud compute instances delete <vm-name>
```

---

### ✅ You're All Set!

You've now:
- 🚀 Deployed an app with Docker, Minikube, and Kubernetes
- 📊 Monitored your cluster using Grafana Cloud

Happy Hacking! 🧠💻🌐
