# Sustc-keeponline
automatically sign in the network portal in SUSTech. Designed for lakeside??? students

# Purpose
It's annoyed to be disconnected and have to try a thousand times for the cas login page to show itself.....

# Requirements
Developed by **python3**, "requests", "bs4" and "pyyaml" are required.

If you are a pip user, you can simply install all the requirements by following command.
``` bash
pip install -r requirements.txt
```

# Usage
## Normal Usage
1. Copy or rename [config.yaml.example] to [config.yaml]
2. Replace the balabalas by your network account fields.
3. At root, run `python3 index.py` to start the main process and keep you online. 

## Service usage[Only for linux/unix users]
If you want to deploy it as a system service, you can follow this
1. Simply copy [keeponline.service] to /etc/systemd/system
2. Modify keeponline.service, correct WorkingDirectory, ExecStart, User filed.
3. Run `sudo systemctl enable keeponline`
4. Run `sudo systemctl start keeponline`


