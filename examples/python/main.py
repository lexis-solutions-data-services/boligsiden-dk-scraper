"""
Example: How to call the boligsiden-dk-scraper actor using Apify API Client

For full documentation of the Apify Client for Python, see: https://docs.apify.com/api/client/python
For full documentation of the actor, see: https://apify.com/lexis-solutions/boligsiden-dk-scraper

Note: This example uses the Apify API Client (apify-client) to call actors from external code.
If you want to create Actors, use the Apify SDK (apify) instead:
https://docs.apify.com/sdk/python/docs/overview/introduction
"""

import os
from apify_client import ApifyClient


def run_actor():
    """Run the boligsiden-dk-scraper actor and retrieve results."""
    # Initialize the ApifyClient with your API token
    # Get your API token from https://console.apify.com/account/integrations
    client = ApifyClient(token=os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))

    # Start the actor run and wait for it to finish
    # The .call() method starts the actor and waits for completion automatically
    actor_id = "lexis-solutions/boligsiden-dk-scraper"
    print(f"Starting actor: {actor_id}")

    run = client.actor(actor_id).call(
        run_input={
            "startUrls": [{"url":"https://www.boligsiden.dk/kommune/aarhus/tilsalg/ejerlejlighed?sortAscending=True&mapBounds=9.94494,55.992485,10.390982,56.3328&splitViewPage=1&priceMin=5800000&priceMax=20400000&areaMin=120&areaMax=250"}],
            "housingType": "all",
            "propertyStatus": "on_market",
            "maxItems": 15,
            "proxyConfiguration": {"useApifyProxy":False,"apifyProxyGroups":[]},
        }
    )

    # Get the dataset ID from the completed run
    dataset_id = run["defaultDatasetId"]
    print(f"Actor run completed! Dataset ID: {dataset_id}")

    # Get the results from the dataset
    dataset_items = client.dataset(dataset_id).list_items()
    items = dataset_items.items
    print(f"Retrieved {len(items)} items from the dataset.")
    print("Results:", items)
    return items


if __name__ == "__main__":
    run_actor()
