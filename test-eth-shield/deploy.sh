gcloud functions deploy --project=parkcath \
                        --region=us-east4 \
                        --runtime=python39 \
                        --trigger-http \
                        --security-level=secure-optional \
                        --allow-unauthenticated \
                        test_eth_shield
