
#!/bin/bash
MLFLOW_TRACKING_URI=${MLFLOW_TRACKING_URI:-http://mlflow.techinea.svc.cluster.local:5000}
python3 script.py --mode train --mlflow-uri $MLFLOW_TRACKING_URI
