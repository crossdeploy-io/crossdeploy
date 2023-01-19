<br />

<p align="center">
  <img src="https://raw.githubusercontent.com/crossdeploy-io/crossdeploy/main/assets/logo.png" alt="crossdeploy" height="60" />
</p>

---

crossdeploy is a declarative approach to manage MLOps resources.

Simply define the desired state of the resources and crossdeploy executes the required actions to get to that state. 

crossdeploy is a thin wrapper around provisioning engines such as Terraform or Pulumi (coming soon), which compares the desired state and the environment's current state to determine what resources need to be created, updated or deleted.

**Not all resources should be deleted and recreated. Some may need to be updated (a non-material change such as, a model name), while others (a material change such as, a new dataset) may need to be recreated.**

Modifications to resources are automatically updated or recreated depending on the modified attribute.

# Why crossdeploy?

## Productivity

**Eliminate boilerplate codes and the need to manually track dependencies between resources. Focus on what to do, instead of how it is done.**

Boilerplate codes are snippets of utility codes that are applied to each type of resource for various tasks, including,

- Checking if a resource exists before creating or updating them. Without these checks, simply running the same code will result in duplicate resources.

- Checking if an attribute of a resource requires it to be updated or destroyed and recreated.

- Maintaining dependencies within the MLOps pipeline to check if downstream resources needs to be updated if upstream resources have been modified.


In a typical machine learning project, resources such as models, deployments, service providers, subscriptions, monitor instances, payload records, etc, can range anywhere from tens to hundreds. Writing boilerplate codes such as the example below or manually managing state and dependencies leads to low productivity and inefficiencies.

For example, on IBM Cloud Pak for Data, when saving a model to a project space, promoting to a deployment space and creating a deployment, compare the two approaches below.

**Imperative approach**
```
# save model to project
model_details = wml_client.repository.store_model(sklearn_model, meta_props)

# promote model to deployment space
promoted_model_id = wml_client.repository.promote_model(
    model_id=model_id, 
    source_project_id=PROJECT_ID, 
    target_space_id=SPACE_ID
)

# create deployment
deployment_details = wml_client.deployments.create(promoted_model_id, meta_props=meta_props)
```
During development or a CI/CD process, running the code above multiple times will result in duplicated resources. A common practice is to check if the resource exists before deleting it, followed by creating it. 
```
# delete deployment if exists in deployment space
for x in wml_client.deployments.get_details()["resources"]:
    if x["metadata"]["name"] == DEPLOYMENT_NAME:
        wml_client.deployments.delete(x["metadata"]["id"])

# delete model if exists in deployment space
for x in wml_client.repository.get_model_details()["resources"]:
    if x["metadata"]["name"] == MODEL_NAME:
        wml_client.repository.delete(x["metadata"]["id"])
```
This assumes, that the resource will always be deleted and recreated, which may not be the best option, as some changes might be non-material change such as model name, and only require an update.



When resource attributes changes, even more code is required to check the type of attribute change as some attributes only require an update, while others may need the resource to be recreated. 

Consider the below two scenarios, where the first case is a change in model name while the second case is a change in the model's algorithm or framework.
```
# case 1: changing the model name
changes = {
    "model_name": NEW_MODEL_NAME,
}
```
```
# case 2: changing the model from an SKLearn model to a PySpark model
changes = {
    "software_spec_id": wml_client.software_specifications.get_uid_by_name("spark-mllib_3.3"),
}
```
Additional code required, to check what attribute changes, before updating or recreating.
```
# check what attribute is changed
if "model_name" in changes:
    # model_name is a non-material change, simply update the model name for the model
    wml_client.repository.update(...)

if "software_spec_id" in changes:
    # software_spec_id is a material change, the previous model needs to be destroyed and recreated

    # either update or delete and recreate deployment, depending on your requirements
    for x in wml_client.deployments.get_details()["resources"]:
        if x["metadata"]["name"] == DEPLOYMENT_NAME:
            wml_client.deployments.delete(x["metadata"]["id"])

    # delete model
    for x in wml_client.repository.get_model_details()["resources"]:
        if x["metadata"]["name"] == MODEL_NAME:
            wml_client.repository.delete(x["metadata"]["id"])
```
The amount of code required to check for existing resources and type of attributes can increase exponentially as the number of resources grow. 

On the other hand, a declarative approach, automatically takes care of all the scenarios above. 

**Declarative approach**

```
flow = CrossDeploy()

# define model attributes
model = flow.ibm.Model(sklearn_model)(
    id = "mortgage-model-rf",
    name = MODEL_NAME,
    project_id = PROJECT_ID,
)

# define which deployment space to promote the model
promoted_model = flow.ibm.PromotedModel(model)(
    project_id = PROJECT_ID,
    space_id = SPACE_ID,
    asset_id = model.id,
)

# define deployment attributes
deployment = flow.ibm.Deployment(
    name = DEPLOYMENT_NAME,
    space_id = SPACE_ID,
    asset = promoted_model.id,
    online = True,
)

flow.apply()
```

Making changes to resources is as simple as just updating the respectively attributes and calling the `apply` method.

**Case 1: Changing the model name**

```
model = flow.ibm.Model(sklearn_model)(
    id = "mortgage-model-rf",
    name = NEW_MODEL_NAME,
    project_id = PROJECT_ID,
)

flow.apply()
```
The name of the model in the project has been updated along with the promoted model.

Output for case 1:
```
Plan: 0 to add, 2 to change, 0 to destroy.
ibmcpd_model.crossdeploy_mortgagemodelrf_D0A9BA80: Modifying... [id=624f7965-7862-4412-a82c-8c2144ed7704]
ibmcpd_model.crossdeploy_mortgagemodelrf_D0A9BA80: Modifications complete after 1s [id=624f7965-7862-4412-a82c-8c2144ed7704]
ibmcpd_model.crossdeploy_mortgagemodelrfpromoted_9850AEA8: Modifying... [id=cf64ea0e-4ab0-4a0e-aa80-826009520171]
ibmcpd_model.crossdeploy_mortgagemodelrfpromoted_9850AEA8: Modifications complete after 0s [id=cf64ea0e-4ab0-4a0e-aa80-826009520171]

Apply complete! Resources: 0 added, 2 changed, 0 destroyed.
```

**Case 2: Changing the model from an SKLearn model to a PySpark model**
```
# crossdeploy automatically detects the type of model and updates the SOFTWARE_SPEC_UID and TYPE. Users have the option to overwrite this.
model = flow.ibm.Model(pyspark_model)(
    id = "mortgage-model-rf",
    name = MODEL_NAME,
    project_id = PROJECT_ID,
)

flow.apply()
```

Changing the type of model from SKLearn to PySpark is a material change, as a result the following actions are take,

- the new PySpark model is created and stored in the project
- the new PySpark model is promoted to the deployment space
- the previous deployment is updated so that the underlying asset is the new PySpark model
- the previous SKLearn model is deleted from both the deployment space and project

These actions reflect the exact desired state that was defined.

Output for case 2:
```
Plan: 2 to add, 1 to change, 2 to destroy.
ibmcpd_model.crossdeploy_mortgagemodelrf_D0A9BA80: Creating...
ibmcpd_model.crossdeploy_mortgagemodelrf_D0A9BA80: Creation complete after 2s [id=86131972-189b-49a1-9a8b-4bbc3afb7589]
ibmcpd_model.crossdeploy_mortgagemodelrfpromoted_9850AEA8: Creating...
ibmcpd_model.crossdeploy_mortgagemodelrfpromoted_9850AEA8: Creation complete after 4s [id=3f6fea77-5209-4791-b278-9dc2a6502ba5]
ibmcpd_deployment.crossdeploy_mortgagedeploymentrf_58AD9F47: Modifying... [id=c67283fc-693b-4f92-8042-6fb481e2f48d]
ibmcpd_deployment.crossdeploy_mortgagedeploymentrf_58AD9F47: Modifications complete after 1s [id=c67283fc-693b-4f92-8042-6fb481e2f48d]
ibmcpd_model.crossdeploy_mortgagemodelrfpromoted_9850AEA8 (deposed object 79774e52): Destroying... [id=cf64ea0e-4ab0-4a0e-aa80-826009520171]
ibmcpd_model.crossdeploy_mortgagemodelrfpromoted_9850AEA8: Destruction complete after 1s
ibmcpd_model.crossdeploy_mortgagemodelrf_D0A9BA80 (deposed object 23e4d89d): Destroying... [id=624f7965-7862-4412-a82c-8c2144ed7704]
ibmcpd_model.crossdeploy_mortgagemodelrf_D0A9BA80: Destruction complete after 1s

Apply complete! Resources: 2 added, 1 changed, 2 destroyed.
```


<br />

## Reusability

**Adapt an existing template to a new use case without modifying a line of code.**

In most cases, reusing an existing asset or template, on a new case often results in rewriting majority of the code due to changes in requirements and architecture.

crossdeploy abstracts operational underlying processes so that users focus on only pertinent details.

Consider the below example (simplified to demonstrate concept, refer to notebook examples for full details) of using a simple template to monitor the quality of a model on Watson OpenScale.

Pertinent details are abstracted as inputs and are seperated from the underlying codes.

```
config = {
    "provider": PROVIDER_CONFIG,
    "model": MODEL_CONFIG,
    "deployment": DEPLOYMENT_CONFIG,
    "service_provider": SERVICE_PROVIDER,
    "subscription": SUBSCRIPTION,
    "cos_data_reference": COS_DATA_REFERENCE,
    "monitors": MONITORS_CONFIG,
}
model_monitor = ModelMonitor(config)
model_monitor.apply()
```

While this approach is fairly common, the added value is when attributes of any resources change, the appropriate **update** or **delete and recreated** actions are applied.

Assuming there is a change in quality threshold, it does not make sense to delete and recreate the monitor as earlier evaluation data would have been lost leading to potential governance issues and incomplete model insights. Using a declarative approach, simply update the change in the quality monitor configuration and call the `apply` method.

```
MONITORS_CONFIG = {
    "quality": {
        "thresholds": [{
            "metric_id": "area_under_roc",
            "type": "lower_limit",
            "value": 0.7, # new threshold
        }]
    },
}
config.update({
    "monitors": MONITORS_CONFIG,
}) 
model_monitor = ModelMonitor(config)
model_monitor.apply()
```
Output:
```
Plan: 0 to add, 1 to change, 0 to destroy.
ibmcpd_monitor_instance.crossdeploy_qualitymonitor_09A65FE9: Modifying... [id=049f0563-5a63-4d92-a4d6-aa75d7e9cc02]
ibmcpd_monitor_instance.crossdeploy_qualitymonitor_09A65FE9: Modifications complete after 1s [id=049f0563-5a63-4d92-a4d6-aa75d7e9cc02]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```

A significant change would be, updating the training reference data which is used to train the drift detection model, which results in the following actions,

- the previous drift monitor is deleted, as the underlying training data has been updated 
- the existing subscription is updated with new training data reference
- the new drift monitor is created and attached to the existing subscription

```
COS_DATA_REFERENCE = {
    "type": "cos",
    "bucket_name": "data-rp",
    "file_name": "mortgage-default-v2.csv", # updated training data
    "resource_instance_id": "2bc86622-194d-4728-b280-7bd9fcfbdf80",
    "cos_api_key": COS_API_KEY,
    "cos_url": "https://s3.us.cloud-object-storage.appdomain.cloud",
    "iam_url": "https://iam.bluemix.net/oidc/token",
}
config.update({
    "cos_data_reference": COS_DATA_REFERENCE,
}) 
model_monitor = ModelMonitor(config)
model_monitor.apply()
```
Output:
```
Plan: 1 to add, 1 to change, 1 to destroy.
ibmcpd_monitor_instance.crossdeploy_driftmonitor_3089CFDB: Destroying... [id=d87508d8-4adc-4549-987a-6ba742d5c1a0]
ibmcpd_monitor_instance.crossdeploy_driftmonitor_3089CFDB: Destruction complete after 0s
ibmcpd_subscription.crossdeploy_subscription1_A3423F9C: Modifying... [id=db070682-7842-431f-9fe9-690102c9a0bb]
ibmcpd_subscription.crossdeploy_subscription1_A3423F9C: Modifications complete after 0s [id=db070682-7842-431f-9fe9-690102c9a0bb]
ibmcpd_monitor_instance.crossdeploy_driftmonitor_3089CFDB: Creating...
ibmcpd_monitor_instance.crossdeploy_driftmonitor_3089CFDB: Creation complete after 1s [id=7f22fcdd-5e91-4349-bf5a-6d7b82d5c5f9]
Apply complete! Resources: 1 added, 1 changed, 0 destroyed.
```

<br />

# How is this different from using my Python utility scripts? 

As the complexity of your project increases, the number of resources naturally increases too.

A simple project that started with model deployment can evolve to complex pipelines which includes, model monitoring, AI governance, data observability, etc., and the number of resources can easily range from tens to hundreds.

1. It is almost impossible to write boilerplate codes to check and manage if each resource and its attributes needs to be recreated or updated.

2. It is challenging to manage the state and track the lineage and dependencies between the resources.

3. It requires additional effort to maintain these utility scripts. In some cases, where each individual have their own version, this may introduce inconsistencies and errors across the organization.

crossdeploy is designed to handle all of the above challenges in a streamlined and efficient way.


# Flexible execution using Code based or Command Line Interface (CLI) based or both

1. Command Line Interface (CLI) based using Terraform or Pulumi (coming soon)

Standard way of using Terraform, with [a custom IBM Cloud Pak for Data provider](https://github.com/randyphoa/terraform-provider-ibmcpd.git).

```
# main.tf
terraform {
  required_providers {
    ibmcpd = {
      source = "randyphoa/ibmcpd"
    }
  }
}
provider "ibmcpd" {
  url = "xxx"
  username = "xxx"
  api_key = "xxx"
}
resource "ibmcpd_model" "mortgage_model" {
  name = "mortgage-model"
  type = "scikit-learn_1.1"
  software_spec = "runtime-22.2-py3.10"
  project_id = "764ffa76-8fb0-4042-a67b-cfba2ad8085b"
  model_path = "model.tar.gz"
}
```
```
# from command line
terraform apply
```

2. Code based (Typescript, Python, Java, C# and Go)

```
# using Python
flow = CrossDeploy()

model = flow.ibm.Model(sklearn_model)(
    id = "mortgage-model-rf",
    name = MODEL_NAME,
    project_id = PROJECT_ID,
    # software_spec = "runtime-22.2-py3.10", automatically inferred
    # model_path = "model.tar.gz", automatically generated
)

flow.apply()
```

3. Build using code, run using CLI

```
# using Python
flow = CrossDeploy()

model = flow.ibm.Model(sklearn_model)(
    id = "mortgage-model-rf",
    name = MODEL_NAME,
    project_id = PROJECT_ID,
    # software_spec = "runtime-22.2-py3.10", automatically inferred
    # model_path = "model.tar.gz", automatically generated
)

flow.synth()
```
```
# from command line
terraform apply
```

The above examples are exactly the same.

# Installing

crossdeploy is a polyglot library and supports Typescript, Python, Java, C# and Go, all from the same codebase. This is done by leveraging CDK for Terraform and AWS Cloud Development Kit. 

A `node` runtime is required, refer to this [link](https://aws.github.io/jsii/user-guides/lib-user) for more details on specific `node` versions.

On IBM Cloud Pak for Data (on-premise) and IBM Cloud Pak for Data as a Service, `node` is pre-installed for Jupyter Notebooks and JupyterLab. 

Simply run the below command to install crossdeploy.

```
pip install crossdeploy
```

Currently, it is only available for Linux operating systems. Mac and Windows versions will be released shortly.


# Getting started

The best way to get started is by running through some examples,

## IBM Cloud Pak for Data as a Service (IBM Cloud)

1. Understanding the basics of the declarative approach - [1-declarative-basics.ipynb](https://github.com/crossdeploy-io/crossdeploy-examples/blob/main/IBM%20Cloud/1-declarative-basics.ipynb)

2. A simple example to store, promote and deploy a model - [2-store-promote-deploy-model.ipynb](https://github.com/crossdeploy-io/crossdeploy-examples/blob/main/IBM%20Cloud/2-store-promote-deploy-model.ipynb)

3. An example on monitoring model focusing on reusability  - [3-monitor-model.ipynb](https://github.com/crossdeploy-io/crossdeploy-examples/blob/main/IBM%20Cloud/3-monitor-model.ipynb)

## IBM Cloud Pak for Data (on-premise)

1. Understanding the basics of the declarative approach - [1-declarative-basics.ipynb](https://github.com/crossdeploy-io/crossdeploy-examples/blob/main/IBM%20Cloud%20Pak%20for%20Data/1-declarative-basics.ipynb)

2. A simple example to store, promote and deploy a model - [2-store-promote-deploy-model.ipynb](https://github.com/crossdeploy-io/crossdeploy-examples/blob/main/IBM%20Cloud%20Pak%20for%20Data/2-store-promote-deploy-model.ipynb)

3. An example on monitoring model focusing on reusability  - [3-monitor-model.ipynb](https://github.com/crossdeploy-io/crossdeploy-examples/blob/main/IBM%20Cloud%20Pak%20for%20Data/3-monitor-model.ipynb)