Coinbase Candlesticks
===

This project is a quick a dirty rendering of coinbase API data using HighCharts.

**Be Warned, it may be incorrect or incomplete. Use at your own risk!**

How does it work?
----

Currently, Coinbase does not have CORS headers set in the API so you can't query for data directly in the browser. To get around this, you need a small proxy server. Enter server.py.

Written in python, it has 2 dependencies: 

```
requests
flask 
```

Once the dependencies are installed you can run the server with:

```
python server.py 
```

The server is now listening on 127.0.0.1:5000 and you can access the graph at 127.0.0.1:5000/candlesticks.

This code has only been tested on OSX 10.9.

Also included is an example nginx configuration that you could use to proxy API data through an nginx server.

License
---

Do as you please. A shoutout on twitter if you use it to do something cool or are inspired by this would be awesome.

BTC donations can be sent to:

1BWqouhd7TS3i3dM7Sv8D36GYomRFPaTX8
