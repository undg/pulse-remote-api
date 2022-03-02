from fastapi.middleware.cors import CORSMiddleware


# use CORSMiddleware to setup origins, credentials, methods, headers...
def setupCORS(app):
    port = "3000"
    origins = [
        "http://192.168.1.222:" + port,
        "https://192.168.1.222:" + port,
        "http://cm:" + port,
        "https://cm:" + port,
        "http://127.0.0.1:" + port,
        "https://127.0.0.1:" + port,
        "http://localhost:" + port,
        "https://loacalhost:" + port,
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


