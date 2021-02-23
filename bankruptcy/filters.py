import re
from typing import Optional, Dict


def filter_106_sum_lines(obj: dict) -> Optional[bool]:
    """Filter our unneeded lines in Form 106Sum

    :param obj: Pdf line
    :return: Whether to keep filtered lines
    """
    if obj["width"] < 20:
        return False
    if obj["top"] < 60:
        return False
    if obj["x0"] < 360:
        return False
    return True


def filter_106_sum_boxes(obj: dict) -> Optional[bool]:
    """Convert and return only checkboxes

    :param obj: pdf character
    :return: Whether to keep the filtered character
    """
    if "fontname" in obj.keys() and "Wingdings" in obj["fontname"]:
        if "2" in obj["text"] or obj["text"] == "\uf06e":
            obj["text"] = "[√]"
        else:
            obj["text"] = "[]"
        return True
    return False


# ------------ E/F Filters -----------
def line_filter(obj: dict) -> Optional[bool]:
    """Filter out lines with widths less than 10 pts

    :param obj: pdf character
    :return: Whether to keep the filtered character
    """

    if obj["width"] < 10:
        return False
    return True


def keys_and_input_text(obj: dict) -> Optional[bool]:
    """Filter input text and IDs on left side of page

    :param obj: pdf character
    :return: Whether to keep the filtered character
    """

    if "fontname" in obj.keys():
        if obj["x0"] < 50:
            m = re.match(r"[0-9.]", obj["text"])
            if m:
                return True
        if 9.1 > obj["size"] > 8.5:
            return obj["fontname"] != "ArialMT"


def just_text_filter(obj: dict) -> Optional[bool]:
    """Filter out all non text inputs

    :param obj: pdf character
    :return: Whether to keep the filtered character
    """

    if "fontname" in obj.keys():
        if 9.1 > obj["size"] > 8.5:
            m = re.match(r"[0-9.]", obj["text"])
            if m:
                return True


def key_filter(obj: dict) -> Optional[bool]:
    """Filter text on the left pdf page that has numbers

    :param obj: pdf character
    :return: Whether to keep the filtered character
    """
    if "fontname" in obj.keys():
        if obj["x0"] < 50:
            m = re.match(r"[0-9.]", obj["text"])
            if m:
                return True


def input_white_text_and_left_side(obj: dict) -> Optional[bool]:
    """Filter white font and section IDs

    :param obj: pdf character
    :return: Whether to keep the filtered character
    """
    if obj["non_stroking_color"] == 1 and obj["top"] > 100:
        return True
    if obj["x0"] < 50 and "text" in obj.keys() and obj["top"] > 100:
        m = re.match(r"[0-9.]", obj["text"])
        if m:
            return True


def filter_106_ab_content(obj: dict) -> Optional[bool]:
    """Convert checkboxes and keep IDs and text inputs

    :param obj: PDF character
    :return: Whether to keep filtered the character
    """
    if obj["non_stroking_color"] == 1:
        return True
    if obj["x0"] < 50 and "text" in obj.keys():
        m = re.match(r"[0-9.]", obj["text"])
        if m:
            return True
    if "text" in obj.keys() and "Wingdings" in obj["fontname"]:
        if (
            "cid:132" in obj["text"]
            or "" in obj["text"]
            or "n" in obj["text"]
        ):
            obj["text"] = "[√]"
            return True
        if (
            "cid:134" in obj["text"]
            or "" in obj["text"]
            or "o" in obj["text"]
        ):
            obj["text"] = "[]"
            return True
    if "text" in obj.keys():
        font = obj["fontname"]
        if font in ["ArialMT", "Arial-ItalicMT", "WQPAYT+LiberationSans"]:
            return False
        if 9.1 > obj["size"] > 8.5:
            return True


def filter_boxes(obj: Dict) -> True:
    """Convert all checkboxes to uniform [√] or []

    :param obj: PDF character
    :return: True
    """
    if "text" in obj.keys() and "Wingdings" in obj["fontname"]:
        if (
            "cid:132" in obj["text"]
            or "" in obj["text"]
            or "n" in obj["text"]
        ):
            obj["text"] = "\n[√] "
        if (
            "cid:134" in obj["text"]
            or "" in obj["text"]
            or "o" in obj["text"]
        ):
            obj["text"] = "\n[] "
    return True


def remove_margin_lines(obj: Dict) -> bool:
    """Remove the lines that are inside the margins

    :param obj: PDF character
    :return: True or False
    """
    """Useful  for 106 D and E/F"""
    if obj["width"] < 10:
        return False
    if 70 < obj["x0"] < 75:
        return False
    if 435 < obj["x0"] < 445:
        return False
    return True