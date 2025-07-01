import requests
import os

class Hypothesizer:
    """
    Generates research hypotheses.
    """
    def _fetch_web_content(self, url: str):
        """
        Simulates fetching web content using Firecrawl. In a real scenario, this would make an API call to Firecrawl.
        """
        firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
        if not firecrawl_api_key:
            print("Warning: FIRECRAWL_API_KEY environment variable not set.")
            print("Please get an API key from firecrawl.dev and set it.")
            return ""

        headers = {"Authorization": f"Bearer {firecrawl_api_key}"}
        firecrawl_url = f"https://api.firecrawl.dev/v0/scrape?url={url}"
        try:
            response = requests.get(firecrawl_url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get("data", {}).get("content", "")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from Firecrawl: {e}")
            return ""

    def generate(self, topic: str):
        """
        Generates a research hypothesis based on a given topic.
        """
        print(f"Generating hypothesis for topic: {topic}...")
        sample_url = "https://en.wikipedia.org/wiki/" + topic.replace(" ", "_")
        web_content = self._fetch_web_content(sample_url)

        if web_content:
            # Simulate processing the web content to extract a summary or key points
            # In a real scenario, you would use NLP techniques here.
            summary = web_content.split('.')[0] + "."
            print(f"Processed content summary: {summary}")
            return f"Based on information about {topic} (e.g., {summary}), we hypothesize that its impact on global climate change is significant."
        else:
            return f"The impact of {topic} on global climate change (no web content fetched)."
