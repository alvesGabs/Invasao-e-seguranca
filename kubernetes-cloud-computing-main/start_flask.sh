kubectl delete deployment flask-app
kubectl delete svc flask-app
kubectl delete configmap flask-app-code
kubectl create configmap flask-app-code --from-file=formulario.py
envsubst < flask-app.yaml | kubectl apply -f -
kubectl expose deployment flask-app --type=NodePort --port=5000
kubectl get svc flask-app