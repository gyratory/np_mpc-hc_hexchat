#np.mpc-hc.py
This script will send a message in the format `« MPC-HC v1.7.7.0 • test video file • 00:00:01/00:23:04 • 150 MB »` to your active channel.

It requires HexChat and Python 3.

##Installation
Copy np.mpc-hc.py into the `%APPDATA%\HexChat\addons` folder.

##Setup

###MPC-HC
Open MPC-HC, press `o` to open up the options.  Then under `Player->Web Interface` enable the option `Listen on Port`.

###HexChat
If you have not restarted HexChat, enter `/load np.mpc-hc.py`.

####Troubleshooting
If you get the message `Unknown file type np.mpc-hc.py`... see [here](https://hexchat.readthedocs.org/en/latest/faq.html#i-get-this-error-unknown-file-type-abc-yz-maybe-you-need-to-install-the-perl-or-python-plugin).

##Usage
`/np` sends a message to your current channel about what you are playing on MPC-HC at the moment.

##More
Originally from [MPC-HC snippets](https://github.com/mpc-hc/snippets).

Readme and filename adapted from [derekxwu](https://github.com/derekxwu/hexchat.np.mpc-hc).

##License
This script is under the MIT License.