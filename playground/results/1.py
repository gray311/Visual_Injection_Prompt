import fitz  # PyMuPDF
from pdf2image import convert_from_path

def find_pages_with_text(pdf_path, search_text):
    doc = fitz.open(pdf_path)
    pages = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        if search_text in text:
            pages.append(page_num + 1)  # 页码从1开始
    return pages

def convert_pages_to_images(pdf_path, pages):
    images = []
    for page_number in pages:
        image = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)
        images.extend(image)
    return images

# PDF 文件路径
pdf_path = './0001088v1.pdf'
# 需要搜索的文本
search_text = ["""Fig.
1""", """Fig.
2""", """FIG. 1.""", """FIG. 2."""]

# 查找包含特定文本的页面
pages = []
for text in search_text:
    pages.extend(find_pages_with_text(pdf_path, text))
print(pages)
if pages:
    # 将这些页面转换为图片
    images = convert_pages_to_images(pdf_path, pages)
    for i, image in enumerate(images):
        image.save(f'output_page_with_text_{pages[i]}.png', 'PNG')
else:
    print(f"未找到包含文本 '{search_text}' 的页面")
