#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:18:38 2019

@author: raghav
"""

from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACd5eputyourownthinghere"
# Your Auth Token from twilio.com/console
auth_token  = "asdw123rputyourownthinghere!"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="---thenumber---", 
    from_="twilionumber",
    body="THIS IS RIDICULOUS!")

print(message.sid)
