Coinbase Candlesticks
===

This project is a quick a dirty rendering of coinbase API data using HighCharts.

**Be Warned, it may be incorrect or incomplete. Use at your own risk!**

How does it work?
----

Currently, Coinbase does not have CORS headers set in the API so you can't query for data directly in the browser. To get around this, you need a small proxy server. Enter server.py.

Written in python it has 2 dependencies: 

```
requests
flask 
```

Once the dependencies are installed you can run the server with 

```
python server.py 
```

in your terminal.

The page is now listening on 127.0.0.1/candlesticks and you can see your the graph!

This code has been tested only on OSX 10.9.

Also included is an example nginx configuration that you could use to host this page on an nginx server. If you do use this nginx configuration be sure to update the candlesticks.html file to query your server and not 127.0.0.1.

License
---

Do as you please. A shoutout on twitter if you use it to do something cool or are inspired by this would be awesome.

BTC donations can be sent to:

1BWqouhd7TS3i3dM7Sv8D36GYomRFPaTX8
