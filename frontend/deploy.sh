gcloud functions deploy --project=parkcath \
                        --region=us-east4 \
                        --runtime=python38 \
                        --trigger-http \
                        --security-level=secure-optional \
                        --allow-unauthenticated \
                        --env-vars-file=.env.yaml \
                        frontend
