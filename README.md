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

#### Local setup
Setup pyenv
```
curl https://pyenv.run | bash
pyenv install 3.7
pyenv local 3.7
pyenv versions
python -m venv .venv
source .venv/bin/activate
pip install pip-tools --index-url https://pypi.org/simple/
pip-compile --no-emit-index-url --no-emit-trusted-host --output-file=requirements.txt requirements.in -vvv --index-url https://pypi.org/simple/
pip install -r requirements.txt --index-url https://pypi.org/simple/
```

###### References
https://www.youtube.com/watch?v=v7famjsXdUY
