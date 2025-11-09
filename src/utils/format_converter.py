import json
import csv
import io
import xml.etree.ElementTree as ET
import pandas as pd

class FormatConverter:
    def convert(self, data, fmt: str) -> str:
        fmt = fmt.lower()
        if fmt == "json":
            return json.dumps(data, indent=2)
        elif fmt == "csv":
            return self.to_csv(data)
        elif fmt in ["xls", "xlsx", "excel"]:
            return self.to_excel(data)
        elif fmt == "xml":
            return self.to_xml(data)
        else:
            raise ValueError(f"Unsupported format: {fmt}")

    def to_csv(self, data) -> str:
        if isinstance(data, dict):
            data = [data]
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        return output.getvalue()

    def to_excel(self, data) -> str:
        if isinstance(data, dict):
            data = [data]
        df = pd.DataFrame(data)
        output = io.BytesIO()
        df.to_excel(output, index=False)
        return output.getvalue().decode("latin1")

    def to_xml(self, data) -> str:
        if isinstance(data, dict):
            data = [data]
        root = ET.Element("Items")
        for item in data:
            elem = ET.SubElement(root, "Item")
            for k, v in item.items():
                child = ET.SubElement(elem, k)
                child.text = str(v)
        return ET.tostring(root, encoding="unicode")