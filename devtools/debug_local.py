# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# The following is intended for developers of fabric-cicd to debug locally against the github repo

import sys
from pathlib import Path

from azure.identity import ClientSecretCredential

root_directory = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_directory / "src"))

from fabric_cicd import (
    FabricWorkspace,
    append_feature_flag,
    change_log_level,
    constants,
    publish_all_items,
    unpublish_all_orphan_items,
)

# Uncomment to enable debug
# change_log_level()

# Uncomment to add feature flag
append_feature_flag("enable_shortcut_publish")

# The defined environment values should match the names found in the parameter.yml file
workspace_id = "f0e3fa10-e2d7-4ce6-a508-4e6e16ba3a27"
environment = "PPE"

# In this example, our workspace content sits within the root/sample/workspace directory
repository_directory = str(root_directory / "sample" / "workspace")

# Explicitly define which of the item types we want to deploy
item_type_in_scope = [
    # "Lakehouse",
    # "VariableLibrary",
    # "Dataflow",
    # "DataPipeline",
    # "Notebook",
    # "Environment",
    # "SemanticModel",
    # "Report",
    # "Eventhouse",
    # "KQLDatabase",
    # "KQLQueryset",
    # "Reflex",
    # "Eventstream",
    "MLExperiment",
]

# Uncomment to use SPN auth
client_id = "c34c682a-c8a1-43a6-8b27-29f0a2ff2fb9"
client_secret = "sQq8Q~nv9Pl1Lxt-Za41Uc89NyITy04yY2FORcrR"
tenant_id = "31d5acce-99ba-40b7-b2a1-f329e04fe742"
token_credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

constants.DEFAULT_API_ROOT_URL = "https://api.fabric.microsoft.com"

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    environment=environment,
    repository_directory=repository_directory,
    item_type_in_scope=item_type_in_scope,
    # Uncomment to use SPN auth
    token_credential=token_credential,
)

# Uncomment to publish
# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# Uncomment to unpublish
# Unpublish all items defined in scope not found in repository
# unpublish_all_orphan_items(target_workspace, item_name_exclude_regex=r"^DEBUG.*")
