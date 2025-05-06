from ..utils.functions import getConfig, getYaml
from ..utils.logger import logger
import litellm
from dotenv import load_dotenv
import os

api_key = os.getenv("GROQ_API_KEY")
class SummaryEngine:
    def __init__(self):
        logger.info("INITIALIZING SUMMARY ENGINE")
        self.config = getConfig(os.path.join(os.getcwd(), "config.ini"))
        self.prompts = getYaml(os.path.join(os.getcwd(), "prompts.yaml"))

    def summarize(self, texts: list[str]) -> str:
   
        try:
            logger.info("Summarizing the details extracted from the images")
            allSummaries = "\n".join(texts)
            completion = litellm.completion(
                model = self.config.get("SUMMARIZER", "LLM"),
                api_key = os.environ["GROQ_API_KEY"],
                api_base = self.config["GROQ CONFIG"]["BASEURL"],
                messages = [
                    {"role": "system", "content": self.prompts["summaryEnginePrompt"]},
                    {"role": "user", "content": f"AGGREGATED SUMMARIES: {allSummaries}"}
                ],
                max_tokens = self.config.getint("SUMMARIZER", "MAXTOKENS"),
                temperature = self.config.getfloat("SUMMARIZER", "TEMPERATURE")
            )
            response = completion["choices"][0]["message"]["content"]
            logger.info("Summary generated successfully")
            return response

        except Exception as e:
            logger.exception(f"❌ Error summarizing the text: {e}")
            logger.error(f"Config used: {self.config}")
            logger.error(f"Prompt used: {self.prompts.get('summaryEnginePrompt')}")
            logger.error(f"API key present: {'GROQ_API_KEY' in os.environ}")
            return None
