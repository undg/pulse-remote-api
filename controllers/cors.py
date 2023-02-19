from fastapi.middleware.cors import CORSMiddleware


# use CORSMiddleware to setup origins, credentials, methods, headers...
def setupCORS(app):
    ports = {"dev": "3000", "prod": "9553"}
    urls = {
        "name0": "http://192.168.1.222",
        "name1": "https://192.168.1.222",
        "name2": "http://cm",
        "name3": "https://cm",
        "name4": "http://127.0.0.1",
        "name5": "https://127.0.0.1",
        "name6": "http://localhost",
        "name7": "https://loacalhost",
    }
    origins = []
    for url in urls.values():
        for port in ports.values():
            origins.append(url + ":" + port)

    for origin in origins:
        print(origin)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
