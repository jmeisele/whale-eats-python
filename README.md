[![Build Status](https://travis-ci.com/jmeisele/whale-eats-python.svg?branch=master)](https://travis-ci.com/jmeisele/whale-eats-python)

# Whale Eats Python
Starter kit for serving incoming http requests to multiple python API endpoints via nginx load balancer. All services contained in their own respective Docker containers.

__To install__:

1. Clone the project
    ```bash
    git clone https://github.com/jmeisele/whale-eats-python.git
    ```
2. Change directories into the repo
    ```bash
    cd whale-eats-python
    ```
3. Run docker compose
    ```bash
    docker-compose up --build
    ```
4. Open up a new browser window and go to your localhost native port 80
    ```bash
    http://localhost
    ```
5. Refresh the window to see different return messages from the different flask apps

If you found this repo helpful, a [small donation](https://www.buymeacoffee.com/VlduzAG) would be greatly appreciated. 
All proceeds go towards coffee, and all coffee goes towards more code.
