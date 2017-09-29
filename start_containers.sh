docker run -dt --name test-driver --network ps-bridge localhost:5000/test-driver
docker run -dt --name petstore-service --network ps-bridge localhost:5000/petstore-service
