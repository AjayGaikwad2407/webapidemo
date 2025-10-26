# Prometheus Installation on AKS using Helm

## Prerequisites
1. **Azure CLI** installed and logged in.
2. **kubectl** installed and configured for your AKS cluster.
3. **Helm** installed.

---

## Steps

### 1. Add the Prometheus Helm Repository
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

### 2. Create a Namespace for Prometheus
```bash
kubectl create namespace monitoring
```

### 3. Install Prometheus using Helm
```bash
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring
```

### 4. Verify the Installation
```bash
kubectl get all -n prometheus
```

### 5. Access the Grafana Dashboard
1. Forward the Grafana service port:
    ```bash
    kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80
    ```
2. Open your browser and navigate to `http://localhost:3000`.

---

### 5. Access the Prometheus UI
1. Forward the Grafana service port:
    ```bash
    kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090:9090
    ```
2. Open your browser and navigate to `http://localhost:9090`.

---
