# Python Multi-threading Benchmark


## 1. Setup

Single thread   | Run job n times
Multi-threaded  | Run job n times on multiple threads using `threading.Thread`
Multi-processed | Run job n times on multiple processes using `multiprocessing.Process`

## 2. Results and observations

Test results on Intel i9-9900K processor:

```
# of threads:8
single thread  exe time:5.387233018875122
multithreaded  exe time:5.378721714019775
multiprocessed exe time:0.7446122169494629
```

`Single thread` and `Multi-threaded` methods show similar performance due to GIL.

`Multi-processed` method has much better performance due to GIL not affecting multiple processes.
