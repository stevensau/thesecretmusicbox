  # Import the DDP package.
import ddp

  # Create a client, passing the URL of the server.
#client = ddp.ConcurrentDDPClient('ws://127.0.0.1:3000/websocket')
client = ddp.ConcurrentDDPClient('ws://45.55.57.220/websocket')

  # Once started, the client will maintain a connection to the server.
client.start()


jsonfile = '{"status":{"msg":"Success","code":0,"version":"1.0"},"metainfos":[{"play_offset":36620,"title":"Why dont you go that way","album":"Infinity","acrid":"392e609029b1591609f27df38e79b378","artist":"One Direction[###]One Direction"}],"result_type":0}'
  # ... Do something with it ...
future = client.call('storeSong', jsonfile)

  # ... Do something else ...

  # Block until the result message is received.
result_message = future.get()

  # Check if an error occured else print the result.
if result_message.has_error():
    print result_message.error
else:
    print result_message.result

  # Ask the client to stop and wait for it to do so.
client.stop()
client.join()
