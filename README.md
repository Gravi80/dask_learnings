# Dask Learning's

#### K8s cluster setup
```
if [ ! -d "$HOME/kind-config" ]; then
  mkdir $HOME/kind-config
fi
if [ ! -f "$HOME/kind-config/config" ]; then
  touch $HOME/kind-config/config
fi
export KUBECONFIG="$HOME/kind-config/config"
kubectl config view
kind create cluster --config cluster-config.yaml --name dask_learning
```

```
export KUBECONFIG="$HOME/kind-config/config"
kubectl config get-contexts
kubectl cluster-info --context kind-dask_learning
kubectl config use-context kind-dask_learning
```

