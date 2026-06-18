import re


class IOCAgent:

    def extract(self, text):

        ips = re.findall(
            r"(?:\d{1,3}\.){3}\d{1,3}",
            text
        )

        domains = re.findall(
            r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
            text
        )

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        return {
            "ips": list(set(ips)),
            "domains": list(set(domains)),
            "emails": list(set(emails))
        }
