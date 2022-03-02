"""
XPCS Online GPU Flow

Summary: This flow executes new xpcs_boost GPU flow.
- Data is transfered from Clutch to Theta
- An "empty" publication is added to the index
- Nodes are "warmed"
- Eigen-Corr is applied
- Plots are made
- Gather + Publish the final data to the portal
"""
from gladier import generate_flow_definition, utils
from gladier_xpcs.flows.container_flow_base import ContainerBaseClient

# import gladier_xpcs.log  # Uncomment for debug logging


@generate_flow_definition(modifiers={
   'publish_gather_metadata': {'payload': '$.GatherXpcsMetadata.details.result[0]'}
})
class XPCSGPUFlow(ContainerBaseClient):
    # See container_base_flow.py for assigning containers.
    containers = {}
    gladier_tools = [
        'gladier_xpcs.tools.TransferFromClutchToTheta',
        'gladier_xpcs.tools.PrePublish',
        'gladier_xpcs.tools.AcquireNodes',
        'gladier_xpcs.tools.EigenCorrGPU',
        'gladier_xpcs.tools.MakeCorrPlots',
        'gladier_xpcs.tools.gather_xpcs_metadata.GatherXPCSMetadata',
        'gladier_xpcs.tools.Publish',
    ]