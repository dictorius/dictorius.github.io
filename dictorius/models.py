class Highlight(object):
    def __init__(self, text: str, bold: bool):
        self.text = text
        self.bold = bold


class Feature(object):
    def __init__(self, title: str, description: bool):
        self.title = title
        self.description = description


class Index(object):
    def __init__(self, json: dict):
        self.slogan = json["main"]["title"]
        self.download_text = json["main"]["text"]
        self.highlights = []
        for obj in json["main"]["items"]:
            self.highlights.append(Highlight(obj["text"], obj["bold"]))

        self.why_title = json["why"]["title"]
        self.why_text = json["why"]["text"]

        self.features_title = json["features"]["title"]
        self.features_text = json["features"]["text"]
        self.features_mailto_text = json["features"]["mailto_text"]
        self.features = []
        for obj in json["features"]["items"]:
            self.features.append(Feature(obj["title"], obj["description"]))


class Config(object):
    def __init__(self, json: dict):
        self.support_email = json["support_email"]


class Footer(object):
    def __init__(self, json: dict):
        self.title = json["title"]
        self.text = json["text"]
        self.mailto_text = json["mailto_text"]
        self.copyright_text = json["copyright_text"]


class SEO(object):
    def __init__(self, json: dict):
        self.title = json["title"]
        self.description = json["description"]
        self.keywords = json["keywords"]
        self.author = json["author"]
        self.copyright = json["copyright"]


class Support(object):
    def __init__(self, json: dict):
        self.title = json["title"]
