from pyscript import document

MAX_QUANTITY = 999


def generate_sku(event):

    category = document.querySelector("#category").value
    style = document.querySelector("#style").value
    raw_quantity = document.querySelector("#quantity").value
    output = document.querySelector("#output")

    if category == "uncolored_sketch":
        category_code = "US"
    elif category == "bust_up_artwork":
        category_code = "BU"
    elif category == "half_body_artwork":
        category_code = "HB"
    elif category == "full_body_artwork":
        category_code = "FB"

    if style == "chibi":
        style_code = "CHI"
    elif style == "semi_realistic":
        style_code = "SEM"
    elif style == "realistic":
        style_code = "REA"
    elif style == "cartoon":
        style_code = "CAR"
    elif style == "pixel_art":
        style_code = "PIX"
    else:
        output.innerText = "Unknown style selected."
        return

    if not raw_quantity.isdigit():
        output.innerText = "Quantity must be a whole number."
        return

    quantity = int(raw_quantity)

    if quantity < 1 or quantity > MAX_QUANTITY:
        output.innerText = "Quantity must be from 1 to " + str(MAX_QUANTITY) + "."
        return

    quantity_part = str(quantity).zfill(3)

    sku = category_code + style_code + quantity_part
    output.innerText = sku
