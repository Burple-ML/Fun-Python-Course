#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:18:38 2019

@author: raghav
"""

from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACd5e3cba76781872cac463fbef052e0e1"
# Your Auth Token from twilio.com/console
auth_token  = "af82e6001fbe36b7b6dfba64f16ed6f1"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+4550275477", 
    from_="+18508088326",
    body="THIS IS RIDICULOUS!")

print(message.sid)