#!/usr/bin/python3
import asyncio
import websockets

connected = set()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    finally:
        # Unregister.
        connected.remove(websocket)
    

start_server = websockets.serve(server, "151.248.113.144", 7501)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()