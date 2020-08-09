### Notes

```bash
kubectl apply -f app_deploy.yaml
kubectl get deployments

kubectl rollout status deployment.v1.apps/test-requestor-deployment
```

To View replica set

```bash
kubectl get rs
```

if issue get the state of the pods

```bash
kubectl get pods
kubectl desribe pod <pod> # will tell you what' going on with the pulling
```


-----
Job

```bash
pods=$(kubectl get pods --selector=job-name=test-requestor-batch-job --output=jsonpath='{.items[*].metadata.name}')
echo $pods
kubectl describe jobs/test-requestor-batch-job
```

# .spec.completions 

For fixed completion count.  Done when one successful pod for each value in 1 to complections.  Can leave out when parallelism is set

# .spec.parallelism

 - with a work queue don't set .spec.completions default to .slec.parallelism
 - each Pod is independently capable of determining whether or not all its peers are done, and thus that the entire Job is done.
 - any job terminates succesffuly no new pods created
 - looks like if parallelism is not set then it will start a job until the number is met.
 - spec.completions make sure that 50 complete with success. So if one fails it will start up another one.  