import os
import sys

from griptape.drivers import GriptapeCloudEventListenerDriver
from griptape.events import EventBus, EventListener
from griptape.structures import Agent

def setup_cloud_listener():
    # Are we running in a managed environment?
    if "GT_CLOUD_STRUCTURE_RUN_ID" in os.environ:
        # If so, the runtime takes care of loading the .env file
        EventBus.add_event_listener(
            EventListener(
                event_listener_driver=GriptapeCloudEventListenerDriver(),
            )
        )
    else:
        # If not, we need to load the .env file ourselves
        from dotenv import load_dotenv

        load_dotenv()
        
if __name__ == "__main__":
    args = sys.argv[1:]

    setup_cloud_listener()

    Agent().run(*args)
