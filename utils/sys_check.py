import os
import sys

def get_env_variables():
    key = None
    endpoint = None
    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
    if key is None or endpoint is None:
        print("\nSet the COMPUTER_VISION_ENDPOINT and/or COMPUTER_VISION_SUBSCRIPTION_KEY environment variables. Restart your shell after defining them!")
        sys.exit()
    return endpoint, key
