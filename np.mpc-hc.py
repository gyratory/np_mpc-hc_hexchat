# -*- coding: utf-8 -*-

#/**
#* mpc.hc.np.py, snippet to display now-playing info for MPC-HC
#* Released under the terms of MIT license
#*
#* https://github.com/gyratory/np_mpc-hc_hexchat
#*
#* Copyright (C) 2013 MPC-HC Team
#* Copyright (C) 2015 gyratory
#*/


__module_name__ = "MPC-HC NP snippet"
__module_version__ = "0.3"
__module_description__ = "Displays MPC-HC Player Info!"

import hexchat
import urllib.request
import re

###############################################################################
# Setup

MPC_HC_PORT = "13579"      # Default port
MPC_HC_PAGE = "info.html"  # Page where "now playing" info is displayed

###############################################################################

MPC_HC_URL = "http://{0}:{1}/{2}".format("localhost", MPC_HC_PORT, MPC_HC_PAGE)

MPC_HC_REGEXP = re.compile(r"\<p\ id\=\"mpchc_np\"\>(.*)\<\/p\>")


def mpc_hc(caller, callee, helper):
    data = urllib.request.urlopen(MPC_HC_URL).read()
    mpc_hc_np = MPC_HC_REGEXP.findall(data.decode())[0].replace("&laquo;", "«")
    mpc_hc_np = mpc_hc_np.replace("&raquo;", "»")
    mpc_hc_np = mpc_hc_np.replace("&bull;", "•")
    hexchat.command("say %s" % mpc_hc_np)
    return hexchat.EAT_ALL

hexchat.hook_command(
    "np",
    mpc_hc,
    help="Use: /np :: Setup: Options -> Player -> Web Interface -> Listen on port"
)