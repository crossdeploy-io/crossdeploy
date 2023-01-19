import os
import gzip
import json
import joblib
import shutil
import pathlib
import tarfile
import itertools

# def create_archive(model, archive_name="model.tar.gz"):
#     temp_dir = pathlib.Path("temp")
#     tar_filename = pathlib.Path(pathlib.Path(archive_name).stem)
#     gz_filename = pathlib.Path(archive_name)
#     shutil.rmtree(temp_dir, ignore_errors=True)
#     temp_dir.mkdir()
#     joblib.dump(model, temp_dir.joinpath("scikit_model.pkl"))
#     with tarfile.open(tar_filename, "w") as tar:
#         tar.add(temp_dir, ".")
#         tar.close()
#     with open(tar_filename, "rb") as f_in, gzip.open(gz_filename, "wb+") as f_out:
#         shutil.copyfileobj(f_in, f_out)
#     tar_filename.unlink()
#     shutil.rmtree(temp_dir, ignore_errors=True)
#     return archive_name

def create_archive(model, archive_name="model.tar.gz", pickle_name="model.joblib"):
    joblib.dump(model, pickle_name)
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(pathlib.Path(pickle_name).name)
    pathlib.Path(pickle_name).unlink()
    return archive_name

def get_training_data_schema(df):
    training_data_schema = [
        [{"name": x, "type": "double", "nullable": True} for x in df.select_dtypes(include=float).columns.tolist()],
        [{"name": x, "type": "long", "nullable": True} for x in df.select_dtypes(include=int).columns.tolist()],
        [{"name": x, "type": "string", "nullable": True} for x in df.select_dtypes(include=object).columns.tolist()],
    ]
    training_data_schema = list(itertools.chain.from_iterable(training_data_schema))
    return training_data_schema

def export_payload_data(df, file_name="payload.json"):
    with open(file_name, "w") as f:
        json.dump({
            "fields": df.columns.tolist(),
            "values": df.values.tolist(),
        }, f)
    return file_name

def export_feedback_data(df, file_name="feedback.json"):
    with open(file_name, "w") as f:
        json.dump({
            "fields": df.columns.tolist(),
            "values": df.values.tolist(),
        }, f)
    return file_name

def get_sp_asset(sagemaker_model):
    return "data." + sagemaker_model.terraform_resource_type + "." + sagemaker_model.friendly_unique_id + ".sp_assets[0]"

def get_resource_by_name(name):
    with open("terraform.tfstate") as f:
        tf_state = json.load(f)
    for resource in tf_state["resources"]:
        if resource["name"] == name and resource["instances"]:
            return resource["instances"][0]["attributes"]

def clear():
    for f in [".terraform", ".terraform.lock.hcl", "terraform.tfstate", "terraform.tfstate.backup"]:
        shutil.rmtree(f, ignore_errors=True)
        pathlib.Path(f).unlink(missing_ok=True)