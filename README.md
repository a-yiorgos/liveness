# liveness
A small container that you can use for Kubernetes liveness test. It reports HTTP 500 30% of the time.

For the first 10 seconds that the container of `k8s.gcr.io/liveness` is alive, the `/healthz` handler returns a status of 200. After that, the handler returns a status of 500.  However, you may want to run a container that randomly responds with 500 status, 30% of the time. You can use this container instead.

It now can also be used to simulate failures for liveness, readiness and startup probes, with the desired percentage failure, depending the pathname:

- `/liveness/36`
- `/rediness/48`
- `/startup/12`
