import pymupdf

doc = pymupdf.open("./First 10/filled_flat/f1099b_filled-flat.pdf")
page = doc[0]
# words = page.get_text("words", sort=True)
# words = page.get_text("blocks")

boxes = page.get_text("words")
# lines = page.get_text("lines")

# for i, line in enumerate(lines):
#     print(line)

for i, box in enumerate(boxes):
    print(box)
