# Use nmcli to show the available wireless networks SSID, mode, channel, transfer rate, signal strength,
# bars and security used using: nmcli dev wifi

# subprocess allows us to use system commands & re allows making use of regular expressions

import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

profile_names = (re.findall("All profiles: (.*)\r", command_output))

wifi_list = list()

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

        if re.search("Security key: Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                               capture_output=True).stdout.decode()
            password = re.search("Key Content (.*)\r", profile_info_pass)

            if password is None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)

                for x in range(len(wifi_list)):
                    print(wifi_list[x])