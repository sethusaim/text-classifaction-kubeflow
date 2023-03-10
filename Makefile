SHELL := /bin/bash # Use bash syntax

data_ingestion:
	bash scripts/build_and_push_component.sh ecom/data_ingestion ecom_data_ingestion

data_validation:
	bash scripts/build_and_push_component.sh ecom/data_validation ecom_data_validation

data_transformation:
	bash scripts/build_and_push_component.sh ecom/data_transformation ecom_data_transformation

model_training:
	bash scripts/build_and_push_component.sh ecom/model_training ecom_model_training

model_evaluation:
	bash scripts/build_and_push_component.sh ecom/model_evaluation ecom_model_evaluation

model_pusher:
	bash scripts/build_and_push_component.sh ecom/model_pusher ecom_model_pusher