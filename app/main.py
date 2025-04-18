name: CI/CD Pipeline

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      working-directory: ./app
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Build Docker image
      run: docker build -t 9740516294/iris-fastapi-app:latest ./app

    - name: Push to Docker Hub
      run: |
        echo "${{ secrets.DOCKERHUB_TOKEN }}" | docker login -u ${{ secrets.DOCKERHUB_USERNAME }} --password-stdin
        docker push 9740516294/iris-fastapi-app:latest

    - name: Deploy to EC2 and restart container
      uses: appleboy/ssh-action@v1.0.0
      with:
        host: 3.110.27.223
        username: ec2-user
        key: ${{ secrets.EC2_PRIVATE_KEY }}
        script: |
          docker stop $(docker ps -q) || true
          docker rm $(docker ps -a -q) || true
          docker pull 9740516294/iris-fastapi-app:latest
          docker run -d -p 8000:8000 9740516294/iris-fastapi-app:latest

