class BasePipeline:
    def process_item(self, item, spider):
        command = item.get("command", "MUST_HAVING")
        payload = item.get("payload")
        method = getattr(self, command, None)
        if method:
            method(payload, item, spider)
        return item
