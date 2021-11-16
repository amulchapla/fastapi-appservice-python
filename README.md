# FastAPI Python app deployment to Azure App Service

This sample shows how to deploy FastAPI Python app to Azure App Service.

Key highlights of this sample:
1. The FastAPI app is in main.py
2. The required Python modules are in the vendor directory as .whl (wheel)
3. Depenency requirements are captured in requirements.txt (as usual)


## Run the code locally

1. Clone this repo. 
2. Switch to the repo directory and run `"pip install -r requirements.txt"` to get required dependencies installed locally
3. Run `"uvicorn main:app"`
4. Open browser and go to `"http://localhost:8000"` and you should get a "Hello World FastAPI" message back.
5. You can also get to API swagger doc at `"http://localhost:8000/docs"`


## Deploying sample code to Azure App Service
You can deploy your FastAPI Python app using VS Code and the Azure App Service extension. Follow instructions [Deploy your Python web app to Azure App Service on Linux](https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-app-service-on-linux-05) that explains how to deploy any Python app to Azure App Service. 

1. To deploy your FastAPI in **main.py** to Azure App Service, select the "fastapi-appservice-python" as the root folder when prompted in the VS code. You can either have VS Code create new App Service plan OR you can deploy your app to an existing app service/plan.
2. Once deployment is completed, your app will still not work as expected until you make the below change.
3. Open the App Service that you have deployed your FastAPI app to. Under `"Settings -> Configuration"` open tab `General Settings` of App Service
Give the Startup Command with the command to start FastAPI on Azure App Service.

`"gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app"`

4. Restart your app service
5. Open browser and go to `"https://<appservicename>.azurewebsites.net"` and you should get a "Hello World FastAPI" message back.
6. You can also get to API swagger doc at `"https://<appservicename>.azurewebsites.net/docs"`