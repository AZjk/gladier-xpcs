from gladier import GladierBaseTool, generate_flow_definition


def make_corr_plots(event):
    """
    Plot the results of a corr run, given the result hdf file.
    REQUIRES globus-automation to be INSTALLED
    """
    import json
    with open(event['parameter_file']) as f:
        event = json.load(f)
    import os
    from XPCS.tools import xpcs_plots
    os.chdir(os.path.join(event['proc_dir'], os.path.dirname(event['hdf_file'])))
    try:
        xpcs_plots.make_plots(os.path.join(event['proc_dir'], event['hdf_file']))
    except (Exception, SystemExit) as e:
        return str(e)
    return [img for img in os.listdir('.') if img.endswith('.png')]


@generate_flow_definition(modifiers={
    make_corr_plots: {'WaitTime': 1200}
})
class MakeCorrPlots(GladierBaseTool):
    """Plot the results of a corr run, given the result hdf file."""

    required_input = [
        'proc_dir',
        'hdf_file',
        'funcx_endpoint_compute',
    ]

    funcx_functions = [
        make_corr_plots
    ]