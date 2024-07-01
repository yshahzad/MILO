#MILO: a Multimodal Integrative Lifting Overview

#This is the main script for running the backend of the website
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug = True)
