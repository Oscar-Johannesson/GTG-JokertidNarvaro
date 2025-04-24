import uvicorn

uvicorn.run(
        "Lararhemsida:run_app",  # This needs to match the function name in Lararhemsida.py
        host="172.30.0.153",          # Make it accessible from other devices
        port=443,                # Use the HTTPS port
        ssl_keyfile='./certificate/private.key',  # Path to your private key
        ssl_certfile='./certificate/certificate.crt'  # Path to your certificate
    )