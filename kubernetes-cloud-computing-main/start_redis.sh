kubectl delete deployment redis
kubectl delete svc redis
kubectl apply -f redis.yaml
kubectl expose deployment redis --type=NodePort --port=6379
kubectl get svc redis