sudo apt update && sudo apt upgrade -y

sudo apt install openjdk-21-jdk -y

sudo apt install python3 python3-pip -y

echo 'alias python=python3' >> ~/.bashrc

source ~/.bashrc

sudo apt update && sudo apt upgrade -y

sudo apt install scala -y

scala -version

pip3 install py4j

wget https://dlcdn.apache.org/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz

tar -xvzf spark-3.5.4-bin-hadoop3.tgz

sudo mv spark-3.5.4-bin-hadoop3 /opt/spark

Add the following lines at the end of the file:
    export SPARK_HOME=/opt/spark
    export PATH=$SPARK_HOME/bin:$PATH
    export PYSPARK_PYTHON=python3

source ~/.bashrc

pip3 install findspark

