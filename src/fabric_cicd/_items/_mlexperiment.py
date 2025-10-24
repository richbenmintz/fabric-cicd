# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""Functions to process and deploy Notebook item."""

import logging

from fabric_cicd import FabricWorkspace

logger = logging.getLogger(__name__)


def publish_mlexperiments(fabric_workspace_obj: FabricWorkspace) -> None:
    """
    Publishes all experiment items from the repository.
    Only Publishes the Shell item, as only type and name are supported for MLExperiment items through api.

    Args:
        fabric_workspace_obj: The FabricWorkspace object containing the items to be published.
    """
    item_type = "MLExperiment"

    for item_name in fabric_workspace_obj.repository_items.get(item_type, {}):
        fabric_workspace_obj._publish_item(item_name=item_name, item_type=item_type)
