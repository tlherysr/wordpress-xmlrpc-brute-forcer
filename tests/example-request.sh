#!/bin/bash

# Define the XML payload
xml_payload='<?xml version="1.0"?>
<methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
        <param>
            <value>
                <string>USERNAME</string>
            </value>
        </param>
        <param>
            <value>
                <string>PASSWORD</string>
            </value>
        </param>
    </params>
</methodCall>'

# Send the XML payload using curl
response=$(curl -s -X POST http://lhedu.org.uk/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d "$xml_payload")

# Print the response
echo "$response"
