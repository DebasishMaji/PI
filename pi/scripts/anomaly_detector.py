import configparser
import argparse


def main():
    config = configparser.ConfigParser()
    data = config.read("/settings/kafka_consumer_config.yml")


if __name__ == '__main__':
    main()