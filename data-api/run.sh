# not general steps
find ./app -name '__pycache__' -print | xargs rm -rf

# docker build --no-cache -t stock_info_api .
docker build -t stock_info_api .
docker rmi $(docker images | grep '^<none>' | awk '{print $3}')
docker run --rm -it -p 5000:5000 --name stock_info_api_env stock_info_api bash
